from flask import Flask, jsonify, request
import json

app = Flask(__name__) 

data ={
    'objeto':[
        {
            'message': 'Hello Wolrd'
        }
    ]
}

# Comando para abrir e escrever no json
with open('objeto.json', 'w') as json_file:
    json.dump(data, json_file)

# Funcao para ler os dados do json
def read_message():
    with open('objeto.json', 'r') as json_file:
        return json.load(json_file)

# Criando rota raiz com o método GET
@app.route('/', methods=['GET']) 
def get_message(): 
    message = read_message()['objeto']
    return jsonify(message)                  

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)