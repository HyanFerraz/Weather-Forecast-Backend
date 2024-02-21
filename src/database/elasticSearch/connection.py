from elasticsearch import Elasticsearch
from errors.error_handler import error_handler
from drivers.dot_env_loader import get_dotenv_values

config = get_dotenv_values()

def connect_to_elasticsearch():
    try:
        return Elasticsearch(
            f"http://elastic:{config['ELASTIC_PASSWORD']}@elasticsearch_container:{config['ELASTIC_PORT']}/"
        )
    except Exception as exception:
        response = error_handler(exception)
