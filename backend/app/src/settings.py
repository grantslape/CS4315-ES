from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

ENVIRONMENT = os.getenv('FLASK_ENV')
ES_HOST = os.getenv('ES_HOST')
ES_PORT = os.getenv('ES_PORT')
