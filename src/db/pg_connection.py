from loguru import logger
import psycopg

class pgConnection:
    def __init__(self, pg_config):
        self.pg_config = pg_config

    def pg_connect(self):
        try:
            pg_connection = psycopg.connect(
                host = self.pg_config["host"],
                port = self.pg_config["port"],
                dbname = self.pg_config["dbname"],
                user = self.pg_config["user"],
                password = self.pg_config["password"]
            )
        except Exception as e:
            logger.info(f"error connecting to the pg database: {e}")
            raise Exception

        logger.info("successfully connected to the pg database")
        return pg_connection



