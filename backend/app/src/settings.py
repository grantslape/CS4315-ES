from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../.env')

ENVIRONMENT = os.getenv('ENVIRONMENT')