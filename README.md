# Análise de Crédito utilizando Machine Learning

## 1. Objetivo
Avaliar o risco de concessão de crédito à compra de um veículo.

## 2. Introdução
Este "deployment" contempla a criação de um modelo que avalie as informações do futuro comprador para saber se será um bom ou um mau pagador com uma dada probabilidade. 

Para tal objetivo, foi utilizado um banco de dados Postgres com as informações de todos os clientes. As informações do banco de dados foram retiradas e tratadas com o Python (CRUD).

Após a obtenção desses dados, foi efetuada a Análise Exploratória dos dados para tratar valores nulos e Outliers.

Posteriormente foi executado a normalização dos dados, padronização para as variáveis núméricas e codificação para as variáveis categóricas, este tratamento é fundamental para a criação do modelo.

Após os ajustes dos dados, foi criado o modelo baseado em uma rede neural artificial com camada oculta que foi treinada e validada com os dados tratados.

Foi utilizado o LIME para fazer a Explicabilidade dos resultados, isto faz com que as informações obtidas pela previsão do modelo sejam mais facilmente entendidas.

Uma API foi criada com o objetivo de fornecer informações a uma aplicação web (simples) para simular qualquer análise de novo cliente.
