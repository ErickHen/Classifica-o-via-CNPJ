# model/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
import joblib
import os

def evaluate_model(model, X_test, y_test):
    """
    Exibe precisão, recall e F1-score médio do modelo.
    Evita warnings quando alguma classe não possui amostras previstas ou reais.
    """
    y_pred = model.predict(X_test)

    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

    print("\n=== Métricas de Avaliação ===")
    print(f"Precisão média: {precision:.4f}")
    print(f"Recall médio:   {recall:.4f}")
    print(f"F1-score médio: {f1:.4f}")


def training_model():
    dataset_path = "model/dataset_empresas.csv"
    if not os.path.exists(dataset_path):
        print(f"Dataset não encontrado em: {dataset_path}")
        return

    df = pd.read_csv(dataset_path)

    X = df.drop("classificacao", axis=1)
    y = df["classificacao"]

    # Separar treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Avaliação
    evaluate_model(model, X_test, y_test)

    # Salvar modelo treinado
    joblib.dump(model, "model/modelo.pkl")
    print("\nModelo treinado e salvo em model/modelo.pkl")

if __name__ == "__main__":
    training_model()
