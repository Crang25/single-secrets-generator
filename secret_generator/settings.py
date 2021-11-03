import os
import yaml
import pathlib
from dotenv import load_dotenv


BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config/config.yaml'

load_dotenv()

def get_config(path):
    with open(path) as f:
        parsed_conf = yaml.safe_load(f)
        return parsed_conf


def load_env(config):
    env_db_data = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }


    config['postgres']['database_url'] = config['postgres']['database_url'].format(**env_db_data)


config = get_config(config_path)
load_env(config)
