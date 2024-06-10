import os
import dotenv

dotenv.load_dotenv()

# redis config
REDIS_DB_HOST = "47.120.17.92"  # your redis host
REDIS_DB_PWD = os.getenv("REDIS_DB_PWD", "jiahaoz7456.123")  # your redis password

# mysql config
RELATION_DB_PWD = os.getenv("RELATION_DB_PWD", "jiahaoz7456.123")
RELATION_DB_USER = os.getenv("RELATION_DB_USER", "wjhz7456")
RELATION_DB_HOST = os.getenv("RELATION_DB_HOST", "47.120.17.92")
RELATION_DB_PORT = os.getenv("RELATION_DB_PORT", "3306")
RELATION_DB_NAME = os.getenv("RELATION_DB_NAME", "media_crawler")


RELATION_DB_URL = f"mysql://{RELATION_DB_USER}:{RELATION_DB_PWD}@{RELATION_DB_HOST}:{RELATION_DB_PORT}/{RELATION_DB_NAME}"

# sqlite3 config
# RELATION_DB_URL = f"sqlite://data/media_crawler.sqlite"
