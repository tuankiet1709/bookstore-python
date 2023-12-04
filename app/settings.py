import os
from dotenv import load_dotenv

load_dotenv()

def get_connection_string():
   db_engine = os.environ.get('DB_ENGINE')
   db_driver = os.environ.get('DB_DRIVER')
   db_host = os.environ.get('DB_HOST')
   db_username = os.environ.get('DB_USERNAME')
   db_password = os.environ.get('DB_PASSWORD')
   db_name = os.environ.get('DB_NAME')
   db_port = os.environ.get('DB_PORT')
   return f'{db_engine}+{db_driver}://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'

SQLALCHEMY_DATABASE_URL = get_connection_string()
ADMIN_DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")
