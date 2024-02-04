from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 27248258))
    API_HASH = env.get("TELEGRAM_API_HASH", "7bddc3e66acfc2679592796cecb9eb8a")
    OWNER_ID = int(env.get("OWNER_ID", 6708682548))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "6708682548").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "hstream_file2stream_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6940035846:AAGNjrQo1z6PSJPjjbEpqBUt1u1KqoraxXM")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID",-1002134502479))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://whispering-brook-15151-caf2581340e6.herokuapp.com/")
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
