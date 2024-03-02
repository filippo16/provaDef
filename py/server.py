from flask import Flask, jsonify
from flask_cors import CORS
import json
import create_jsonData as cjd
import createDF as cdf

app = Flask(__name__)
CORS(app)

@app.route('/formation', methods=['GET'])
def get_formation():
    # Qui puoi inserire i dati dei tuoi giocatori
    players = [
        { 'r': 'P', 'nome': 'Donnarumma' },
        { 'r': 'D', 'nome': 'Bonucci' },
        { 'r': 'D', 'nome': 'Chiellini' },
        { 'r': 'D', 'nome': 'De Ligt' },
        { 'r': 'D', 'nome': 'Sandro' },
        { 'r': 'C', 'nome': 'Pogba' },
        { 'r': 'C', 'nome': 'Verratti' },
        { 'r': 'C', 'nome': 'Kante' },
        { 'r': 'A', 'nome': 'Giroud' },
        { 'r': 'A', 'nome': 'Messi' },
        { 'r': 'A', 'nome': 'Ronaldo' },
        # Aggiungi altri giocatori come necessario
    ]
    return jsonify(players)

@app.route('/list', methods=['GET'])
def get_list():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    cjd.createJsonData(cdf.create_df('data.csv'), 'data')
    app.run(port=3000)