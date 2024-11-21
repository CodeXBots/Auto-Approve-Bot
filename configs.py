from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
 
    ADMIN = list(map(int, getenv("ADMIN", "").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    FORCE_SUB = int(getenv("FORCE_SUB", ""))

    # database configs
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")

rkn1 = Config()
