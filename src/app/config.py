from pathlib import Path

from platformdirs import user_data_dir

APP_NAME = "personal-assistant"
APP_AUTHOR = "neoversity"

DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
DB_PATH = DATA_DIR / "assistant.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"
