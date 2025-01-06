from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import pandas as pd
import joblib # carregar objetos salvos
from utils import *


# inicilizar a aplicação Flask

app = Flask(__name__)

model = load_model('meu_modelo.keras')
selector_carregado = joblib.load('./objects/selector.joblib')

# criação da rota
# decorador @
@app.route('/predict', methods=['POST'])

def predict():
    input_data = request.get_json()

    df = pd.DataFrame(input_data)

    df = load_scalers(df,  ['tempoprofissao','renda','idade','dependentes',
                            'valorsolicitado','valortotalbem','proporcaosolicitadototal'])
    
    df = load_encoders(df,  ['profissao', 'tiporesidencia','escolaridade','score',
                             'estadocivil','produto'])
    
    # processo de seleção de atributos
    df = selector_carregado.transform(df)

    predictions = model.predict(df)

    return jsonify(predictions.tolist())


# Inicializar a aplicação

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    #app.run(debug=True)

