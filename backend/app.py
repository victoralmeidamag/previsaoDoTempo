from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
 
app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json(force=True)
        city = data.get('city','')
        api_key = "5e92b0ea44f8dcdf5a2577ada1a1d0ed"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=pt_br"
        retorno = requests.get(link)
        requisicao = retorno.json() 
        descricao = requisicao['weather'][0]['description']
        temperatura = round(requisicao['main']['temp'] - 273.15)
        return jsonify({'descricao' : descricao, 'temperatura' : temperatura})
    except Exception as e:
        print(f"erro {str(e)}")
        return jsonify({'result' : 'error'})

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0" )