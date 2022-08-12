from flask import Flask, jsonify
import pandas as pd
import csv
import json
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def homepage():
  tabela = pd.read_csv('dados.csv', sep=',', encoding='ISO-8859-1')
  amido = tabela['Amido'].to_json()
  stud_obj = json.loads(amido)

  print(type(stud_obj))
  return stud_obj

@app.route('/')
def test():
    return 'test'

if __name__ == '__main__':
    app.run(port=3001)