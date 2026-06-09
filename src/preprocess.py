import re
from typing import Iterable, List

try:
    import jieba
except ModuleNotFoundError:
    jieba = None

from src.config import STOPWORDS


URL_PATTERN = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
HTML_PATTERN = re.compile(r"<[^>]+>")
NON_TEXT_PATTERN = re.compile(r"[^\u4e00-\u9fa5a-zA-Z]+")


def clean_text(text: str) -> str:
    """Normalize noisy review text before tokenization."""
    if not isinstance(text, str):
        return ""

    text = HTML_PATTERN.sub(" ", text)
    text = URL_PATTERN.sub(" ", text)
    text = NON_TEXT_PATTERN.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def tokenize(text: str) -> List[str]:
    cleaned = clean_text(text)
    if jieba is not None:
        words = jieba.lcut(cleaned)
    else:
        words = re.findall(r"[a-zA-Z]+|[\u4e00-\u9fa5]", cleaned)
    return [word for word in words if word.strip() and word not in STOPWORDS]


def preprocess_text(text: str) -> str:
    return " ".join(tokenize(text))


def preprocess_many(texts: Iterable[str]) -> List[str]:
    return [preprocess_text(text) for text in texts]
