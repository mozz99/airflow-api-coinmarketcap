import pandas as pd
from pathlib import Path
import json

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
path_name = Path(__file__).parent.parent / 'data' / 'usd_data.json'


def create_dataframe(path_name: str) -> pd.DataFrame:
    logging.info("→ Criando DataFrame do arquivo JSON...")

    path = Path(path_name)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    with open(path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # A chave principal é "data"
    df = pd.json_normalize(json_data["data"])

    
    logging.info(f"✓ DataFrame criado com {len(df)} linha(s)")
    return df

def data_transformations():
    df = create_dataframe(path_name)
    df['quote.BRL.last_updated'] = pd.to_datetime(df['quote.BRL.last_updated'], utc=True).dt.tz_convert('America/Sao_Paulo')

    df['last_updated'] = pd.to_datetime(df['last_updated'], utc=True).dt.tz_convert('America/Sao_Paulo')
    logging.info("✓ Transformações concluídas\n")
    return df
