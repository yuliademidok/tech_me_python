from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    'URL': f"sqlite:///{BASE_DIR / 'web_shop.db'}",
}
