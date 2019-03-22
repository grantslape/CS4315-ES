from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

ENVIRONMENT = os.getenv('PYTHON_ENV')
ES_HOST = os.getenv('ES_HOST')
