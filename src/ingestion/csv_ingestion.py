from db.database import DBManagement
from src.utils.query_loader import QueryLoader
from config import DATA_DIR, INGESTION_QUERIES_FOLDER
from src.utils.logger import logger

class CSVIngestion:

    def __init__(self, db: DBManagement):
        self.db = db
    
    def ingest_all_files(self, dict_files:dict):

        logger.info("Starting CSV ingestion process")

        sql_path = INGESTION_QUERIES_FOLDER/"csv_ingestion.sql"

        for filename, table_name in dict_files.items():
            self.ingest_file(table_name=table_name, filename=filename, sql_path=sql_path)
            
        logger.info("CSV ingestion completed succesfully")

    def ingest_file(self, table_name:str, filename:str, sql_path:str):

        file_path = DATA_DIR / filename

        try:

            if not file_path.exists():
                raise FileNotFoundError(
                    f"Missing file: {file_path}"
                )
            
            query_template = QueryLoader.load(path=sql_path)
            query = query_template.format(
                table_name=table_name,
                file_path=file_path
            )
            
            self.db.execute(query=query)
        
        except Exception:
            
              logger.exception(
                f"Failed ingesting {filename} into {table_name}"
            )
              raise 
    