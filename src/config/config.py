import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")

pg_config = {
    "host": host,
    "port": port,
    "dbname": dbname,
    "user": user,
    "password": password
}

source_path = os.getenv("source_path")

source_config = {
    "source_path": source_path
}