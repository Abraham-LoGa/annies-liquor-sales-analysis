import duckdb
from config import DB_PATH
from src.utils.logger import logger

class DBManagement:
    
    def __init__(self):

        self.db_path = str(DB_PATH)
        self.connection = None
    
    def connect(self):

        try:
            logger.info("Connecting to DB ...")
            if self.connection is None:
                self.connection = duckdb.connect(self.db_path)
                self._configure_db()
                logger.info("Database connection established ...")
            return self.connection
        except Exception as e:
            logger.exception(f"Database connection failed: {e}")

    
    def _configure_db(self):

        try:
            self.connection.execute(""" SET memory_limit='4GB' """)
            self.connection.execute(""" SET threads=4 """)
        except Exception as e:
            logger.exception(f"Database configuration failed: {e}")
            raise
    
    def execute(self, query:str = None):

        if not query:
            raise ValueError("Query cannoy be empty")
        try:
            return self.connect().execute(query)
        except Exception as e:
            logger.exception(f"Query execution failed: {e}")
            raise
    
    def fetch_all(self, query:str = None):

        try:
            return self.execute(query).fetchall()
        except Exception as e:
            logger.exception(f"Fetch all failed: {e}")
            raise
    
    def fetch_df(self, query:str = None):

        try:
            return self.execute(query).df()
        except Exception as e:
            logger.exception(f"Fetch df failed: {e}")
            raise
    
    def close(self):
        
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
                logger.info("Database connection closed")

        except Exception as e:
            logger.exception(f"Error closing database: {e}")
            raise