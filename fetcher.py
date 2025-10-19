import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

def fetch_cnpj_data(cnpj: str):
    url = f"{BASE_URL}{cnpj}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Falha ao buscar {cnpj} (status {response.status_code})")
