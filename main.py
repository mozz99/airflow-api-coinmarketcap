from src.extract_data import extract_usd_to_brl_data
from src.load_data import load_usd_data
from src.transform_data import data_transformations

import os
from pathlib import Path
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

table_name = 'usd_data'

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


def pipeline():
    try:
        logging.info("ETAPA 1: EXTRACT")
        extract_usd_to_brl_data(url, parameters, headers)

        logging.info("ETAPA 2: TRANSFORM")
        df = data_transformations()

        logging.info("ETAPA 3: LOAD")
        load_usd_data(table_name, df)

        print("\n" + "="*60)
        print("✅ Pipeline concluído com sucesso!")
        print("="*60)

    except Exception as e:
        logging.error(f"❌ ERRO no Pipeline: {e}")
        import traceback
        traceback.print_exc()


pipeline()
