import os
from dotenv import load_dotenv

load_dotenv()

# TODO: Update readme with all environment variables needed
class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False