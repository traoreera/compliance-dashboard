import os
import uuid
from pathlib import Path

PROJECT_ROOT = Path("./").resolve().absolute()
DOWNLOAD_DIR = PROJECT_ROOT / "download"

session_id = uuid.uuid4().hex[:8]

env = os.environ
user = env.get("user")
password = env.get("pass")
