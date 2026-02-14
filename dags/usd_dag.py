from datetime import datetime, timedelta
from airflow.decorators import dag, task
from pathlib import Path
import sys
import os

sys.path.insert(0, '/opt/airflow/src')

from transform_data import data_transformations
from load_data import load_usd_data
from extract_data import extract_usd_to_brl_data
from dotenv import load_dotenv


env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

API_KEY = os.getenv('API_KEY')
url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
parameters = {
    "amount": 1,
    #  "id":1,
    "symbol": "USD",
    "convert": "BRL"

}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}
table_name = 'usd_data'


@dag(
    dag_id='api_coinmarketcap_pipeline',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
    },
    description='Pipeline ETL - USD to BRL',
    schedule='0 */1 * * * ',
    start_date=datetime(2026, 2, 13),
    catchup=False,
    tags=['currency', 'etl']
)
def usd_pipeline():

    @task
    def extract():
        extract_usd_to_brl_data(url, parameters,headers)

    @task
    def transform():
        df = data_transformations()
        df.to_parquet('/opt/airflow/data/usd_data.parquet', index=False)

    @task
    def load():
        import pandas as pd
        df = pd.read_parquet('/opt/airflow/data/usd_data.parquet')
        load_usd_data(table_name, df)

    extract() >> transform() >> load()


usd_pipeline()
