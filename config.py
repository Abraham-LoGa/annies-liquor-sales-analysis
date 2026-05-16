from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

BASE_DIR = Path(__file__).resolve().parent

DATA_FOLDER = os.getenv("DATA_FOLDER", "")
REPORT_QUERIES_FOLDER = os.getenv("REPORT_QUERIES_FOLDER","")
INGESTION_QUERIES_FOLDER = os.getenv("INGESTION_QUERIES_FOLDER","")
DB_FOLDER = os.getenv("DB_FOLDER", "")
DB_FILE = os.getenv("DB_FILE", "")

DATA_DIR = BASE_DIR/DATA_FOLDER
DB_DIR = BASE_DIR/DB_FOLDER
DB_PATH = DB_DIR/DB_FILE
QUERIES_PATH = BASE_DIR/REPORT_QUERIES_FOLDER
TEMPLATES = BASE_DIR/"src/templates"

