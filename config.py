from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 28824298)  # api id
API_HASH = environ.get("API_HASH", "8db28909cc19fe75f0fa3864ef3fee11")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "6440840485:AAHYAfBgwF_Jzm0jdyh0_KjVd1Q4a03nDu4")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "localhost")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 11364)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "ZLoqCubOWQTMmLv5xzF7xEJSWIASdnMn"
)  # redis password


ADMINS = [6801198172]
OWNER_ID = 6801198172  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002123012501  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002117984599
DUMP_CHANNEL = -1002038700004


# Config
COOKIE = environ.get("COOKIE", "")
