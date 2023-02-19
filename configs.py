from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "your api id"))
    API_HASH = getenv("API_HASH", "your api hash")
    BOT_TOKEN = getenv("BOT_TOKEN", "your bot token")
    FSUB = getenv("FSUB", "your channel username")
    CHID = int(getenv("CHID", "your channel id"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb url")
    
cfg = Config()
