# Análise de Crédito utilizando Machine Learning

## 1. Objetivo
Avaliar o risco de concessão de crédito à compra de um veículo.

## 2. Introdução
Este "deployment" contempla a criação de um modelo que avalie as informações do futuro comprador para saber se será um bom ou um mau pagador com uma dada probabilidade. 

### 2.1. Banco de dados - Postgres
Para tal objetivo, foi utilizado um banco de dados Postgres com as informações de todos os clientes. As informações do banco de dados foram retiradas e tratadas com o Python (CRUD).

### 2.2. Análise exploratória de dados (EDA)
Após a obtenção desses dados, foi efetuada a análise exploratória de dados para tratar valores nulos e Outliers.

### 2.3. Normalização dos dados
Posteriormente foi executado a normalização dos dados, padronização para as variáveis núméricas e codificação para as variáveis categóricas, este tratamento é fundamental para a criação do modelo.

### 2.4 Modelo de Machine Learning
Após os ajustes dos dados, foi criado o modelo baseado em uma rede neural artificial com camada oculta que foi treinada e validada com os dados tratados.

### 2.5 Explicabilidade
Foi utilizado o LIME para fazer a Explicabilidade dos resultados, isto faz com que as informações obtidas pela previsão do modelo sejam mais facilmente entendidas.

### 2.6 API
Uma API foi criada com o objetivo de fornecer informações a uma aplicação web (simples) para simular qualquer análise de novo cliente.
