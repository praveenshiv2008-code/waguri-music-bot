import os

API_ID = int(os.getenv("API_ID", "33024906"))
API_HASH = os.getenv("API_HASH", "186ccd86463624521cffc814f8e0fe82")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_STRING = os.getenv("ASSISTANT_SESSION") or os.getenv("STRING_SESSION")
MAIN_OWNER = int(os.getenv("OWNER_ID", "7195555305"))
DEPLOYED_OWNER_ID = int(os.getenv("OWNER_ID", "7195555305"))
SEARCH_API_URL = os.getenv("SEARCH_API_URL", "https://search-api.kustbotsweb.workers.dev")
DOWNLOAD_API_BASE = os.getenv("DOWNLOAD_API_BASE", "").rstrip("/")
COOKIES_FILE = os.getenv("COOKIES_FILE", "cookies.txt")
YOUTUBE_COOKIES = os.getenv("YOUTUBE_COOKIES", "")
RATE_LIMIT_COUNT = 4
RATE_LIMIT_WINDOW = 6
MAX_TITLE_LEN = 30
PORT = int(os.getenv("PORT", "8080"))
