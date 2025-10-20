from main import run
import time
import random

def process_batch(file_path: str, max_retries: int = 5, base_delay: float = 2.0):
    """
    Processa um arquivo contendo uma lista de CNPJs, chamando a função run(cnpj)
    para cada linha, com tratamento de erros e controle de taxa.
    """
    try:
        with open(file_path, 'r') as f:
            cnpjs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return

    total = len(cnpjs)
    for idx, cnpj in enumerate(cnpjs, start=1):
        print(f"\n[{idx}/{total}] Processando CNPJ: {cnpj}")

        for attempt in range(1, max_retries + 1):
            try:
                run(cnpj)
                break  # sucesso → sai do loop de retry
            except Exception as e:
                if "429" in str(e):  # erro de limite de requisições
                    wait = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 1)
                    print(f"⚠️  Erro 429 detectado. Tentativa {attempt}/{max_retries}. Aguardando {wait:.1f}s...")
                    time.sleep(wait)
                else:
                    print(f"❌ Falha ao processar {cnpj}: {e}")
                    break
        else:
            print(f"⛔ Não foi possível processar {cnpj} após {max_retries} tentativas.")

        # pequena pausa entre CNPJs para evitar sobrecarga
        time.sleep(random.uniform(1.5, 3.5))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python batch_processor.py <arquivo.txt>")
    else:
        process_batch(sys.argv[1])
