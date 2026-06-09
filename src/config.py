from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODEL_DIR / "fake_review_detector.joblib"
REPORT_PATH = MODEL_DIR / "metrics_report.txt"
CONFUSION_MATRIX_PATH = MODEL_DIR / "confusion_matrix.png"

TEXT_COLUMN = "text"
LABEL_COLUMN = "label"

STOPWORDS = {
    "的",
    "了",
    "和",
    "是",
    "我",
    "也",
    "就",
    "都",
    "而",
    "及",
    "与",
    "着",
    "或",
    "一个",
    "没有",
}
