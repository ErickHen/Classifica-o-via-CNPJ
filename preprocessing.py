from datetime import datetime

def extrair_features(data):
    today = datetime.now()
    
    # Converte data de abertura para calcular idade
    establishment_date = data.get("founded")
    if establishment_date:
        try:
            establishment = datetime.strptime(establishment_date, "%Y-%m-%d")
            company_age = (today - establishment).days // 365
        except:
            company_age = 0
    else:
        company_age = 0
        
    # Status de atividade
    status = data.get("status", "")
    if isinstance(status, dict):
        status = status.get("text", "")
	
    # Simples Nacional
    simples = data.get("simples", {})
    if isinstance(simples, dict):
        simples_ativo = 1 if simples.get("optant") else 0
    else:
        simples_ativo = 0
    
    # Capital Social
    company = data.get("company") or {}
    capital_social = company.get("equity", 0)

    return {
        "status_ativa": 1 if status.upper() == "ATIVA" else 0,
        "idade_empresa": company_age,
        "capital_social": capital_social,
        "simples_ativo": simples_ativo
    }
