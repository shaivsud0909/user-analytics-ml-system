from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

port=8000

# Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent



# DB Params
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "user_analytics_ml_system")

# Build DATABASE_URL
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60