from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID",  1234))
    API_HASH = env.get("TELEGRAM_API_HASH", "7bddc3e66acfc2679592796ceeb8a")
    OWNER_ID = int(env.get("OWNER_ID", 12345678))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "userid").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "bot name")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6940035846:token no")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID",-1002134502479))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080") # change your url name or else leave as it to localhost 
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
