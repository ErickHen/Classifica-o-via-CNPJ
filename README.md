## 🧠 CNPJ Classifier – Analisador Inteligente de Empresas

Um projeto de classificação automática de empresas com base em dados do CNPJ, utilizando Machine Learning e integração com a API pública da OpenCNPJa.

O sistema permite:

Analisar um único CNPJ via linha de comando;

Processar vários CNPJs em lote;

Fazer logs estruturados das análises;

Treinar e avaliar um modelo de IA com Random Forest.


# ⚙️ Instalação

Instalar dependências

pip install -r requirements.txt

</br>

📄 Exemplo de requirements.txt:

pandas
scikit-learn
joblib
requests

</br>

# 🚀 Uso
🔹 Analisar um único CNPJ

python main.py 12345678000195

</br>

🧩 Exemplo de saída:

Analisando CNPJ 12345678000195 com IA...

Resultado da Análise:
{
  "classificacao": "Aprovado",
  "score": 92.5,
  "features_usadas": {
    "status_ativa": 1,
    "idade_empresa": 12,
    "capital_social": 50000.0,
    "simples_ativo": 0
  }
}

</br>

🔹 Processar vários CNPJs em lote

Crie um arquivo cnpjs.txt contendo uma lista de CNPJs (um por linha):

12345678000195

45987321000110

09876543000120

</br>

E execute:

python batch_processor.py cnpjs.txt

</br>

O script irá:

Processar cada CNPJ individualmente;

Registrar todos os resultados no arquivo log.txt.

</br>

# 🧩 Treinamento do Modelo

Para treinar novamente o modelo de IA com seus próprios dados:

python model/train_model.py

</br>

Requisitos:

Um dataset CSV chamado dataset_empresas.csv com colunas semelhantes a:

status_ativa,idade_empresa,capital_social,simples_ativo,classificacao

1,12,50000,1,Aprovado

0,3,0,0,Reprovado

</br>

O modelo treinado será salvo em model/modelo.pkl.

</br>

Durante o treino, são exibidas métricas:

=== Métricas de Avaliação ===

Precisão média: 0.89

Recall médio: 0.88

F1-score médio: 0.88

</br>

# 📊 Logs

Todos os resultados de análises são salvos no arquivo log.txt com timestamp:

{
  "timestamp": "2025-10-19T18:42:10.123456",
  "result": {
    "cnpj": "12345678000195",
    "classificacao": "Reprovado",
    "score": 70.0,
    "features_usadas": {
      "status_ativa": 0,
      "idade_empresa": 15,
      "capital_social": 0.0,
      "simples_ativo": 0
    }
  }
}

</br>

# 🧠 Tecnologias Utilizadas

Python 3.9+

Scikit-learn – Machine Learning

Pandas – Manipulação de dados

Joblib – Serialização de modelos

Requests – Consumo de API REST

CLI – Interface via terminal

</br>

🧾 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e contribuir.

</br>

👨‍💻 Autor

Erik Henrique

Desenvolvedor Python & IA
