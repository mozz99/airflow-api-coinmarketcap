from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import logging
from pathlib import Path
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

api_key = os.getenv('API_KEY')

url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'
parameters = {
  "amount":1,
#  "id":1,
  "symbol":"USD",
  "convert":"BRL"

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

def extract_usd_to_brl_data(url: str, parameters: dict, headers: dict):
    session = Session()
    session.headers.update(headers)

    try:
        logging.info("Realizando requisição para CoinMarketCap API...")
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        output_path = 'data/usd_data.json'
        output_dir = Path(output_path).parent
        output_dir.mkdir(parents=True, exist_ok=True)
            
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
            
            logging.info(f"Arquivo salvo em {output_path}")  
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        logging.error("Erro ao realizar requisição: %s", e)