from loguru import logger
from db.pg_connection import pgConnection
from config.config import pg_config
from pipeline.pipeline import run_pipeline


logger.info("main file is running")

pg_connection = pgConnection(pg_config)
pg_connection = pg_connection.pg_connect()

run_pipeline(pg_connection)

