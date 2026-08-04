from loguru import logger
from db.pg_connection import *
from config.config import *
from pipeline.pipeline import *


logger.info("main file is running")

pg_connection = pgConnection(pg_config)
pg_connection = pg_connection.pg_connect()

run_pipeline(pg_connection)

