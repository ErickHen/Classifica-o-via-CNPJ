from main import run

def process_batch(file_path: str):
    try:
        with open(file_path, 'r') as f:
            cnpjs = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return

    for idx, cnpj in enumerate(cnpjs, start=1):
        cnpj = cnpj.strip()
        if not cnpj:
            continue 
        try:
            print(f"\n[{idx}/{len(cnpjs)}] Processando CNPJ: {cnpj}")
            run(cnpj)
        except Exception as e:
            print(f"Falha ao processar {cnpj}: {e}")
            continue

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python batch_processor.py <arquivo.txt>")
    else:
        process_batch(sys.argv[1])
