# model/predictor.py
import joblib
import pandas as pd
from preprocessing import extrair_features

model = joblib.load("model/modelo.pkl")

def prever_classificacao(dados_api):
    features = extrair_features(dados_api)
    X = pd.DataFrame([{
        "status_ativa": features["status_ativa"],
        "idade_empresa": features["idade_empresa"],
        "capital_social": features["capital_social"],
        "simples_ativo": features["simples_ativo"]
    }])

    classify = model.predict(X)[0]
    prob = model.predict_proba(X).max()

    return {
        "classificacao": classify,
        "score": round(float(prob) * 100, 2),
        "features_usadas": features
    }
