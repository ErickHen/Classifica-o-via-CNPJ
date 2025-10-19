import sys
from fetcher import fetch_cnpj_data
from model.predictor import prever_classificacao
from logger import log_result

def run(cnpj):
    print(f"Analisando CNPJ {cnpj} com IA...")
    data = fetch_cnpj_data(cnpj)
    result = prever_classificacao(data)

    print("\n=== Resultado da Análise ===")
    print(result)

    log_result({
        "cnpj": cnpj,
        **result
    })

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <CNPJ>")
    else:
        run(sys.argv[1])
