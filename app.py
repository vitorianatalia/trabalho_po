from flask import Flask, jsonify
from solver_v2 import solve_model
import pandas as pd
import csv
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
  pathname = r'C:\\Users\\vitor\\Desktop\\trabalho-po\\trabalho-po\\dados.csv'
  outpath = r'C:\\Users\\vitor\\Desktop\\trabalho-po\\trabalho-po\\output.json'
  data = pd.read_csv(pathname, sep=',')

  componente = data.Componente
  unidade = data.Unidade
  exigencias = data.Exigencias
  limInf = data.LimInf
  limSup = data.LimSup
  algodao = data.Algodao_Farelo_39
  amido = data.Amido
  arrozFarelo = data.Arroz_Farelo
  arrozFareloDeseng = data.Arroz_Farelo_Deseng
  carneOssos = data.Carne_e_Ossos_Farinha_50
  polpa = data.Citrus_Polpa
  mandioca = data.Mandioca_Integral_Raspa
  milho7 = data.Milho_7_88
  milhoGluten = data.Milho_Farelo_de_Glúten_60
  oleoSoja = data.oleo_de_Soja
  sojaFarelo = data.Soja_Farelo_48
  trigoFarelo = data.Trigo_Farelo
  lisina = data.Lisina_HCL
  metionina = data.Metionina
  fosfato = data.Fosfato_BicAlcico
  calcario = data.CalcArio_Calcitico
  sal = data.Sal_Comum
  excipiente = data.Excipiente



  algodaoCont = {}
  amidoCont = {}
  arrozFareloCont = {}
  arrozFareloDesengCont = {}
  carneOssosCont = {}
  polpaCont = {}
  mandiocaCont = {}
  milho7Cont = {}
  milhoGlutenCont = {}
  oleoSojaCont = {}
  sojaFareloCont = {}
  trigoFareloCont = {}
  lisinaCont = {}
  metioninaCont = {}
  fosfatoCont = {}
  calcarioCont = {}
  salCont = {}
  excipienteCont = {}

  
  listComponents = []
  for i in componente:
    listComponents.append(i)

  
  x = 0
  while x < len (sal):
    algodaoCont.update({ listComponents[x] : algodao[x]})
    amidoCont.update({ listComponents[x] : amido[x]})
    arrozFareloCont.update({ listComponents[x] : arrozFarelo[x] })
    arrozFareloDesengCont.update({ listComponents[x] : arrozFareloDeseng[x] }) 
    carneOssosCont.update({ listComponents[x] : carneOssos[x] }) 
    polpaCont.update({ listComponents[x] : polpa[x] }) 
    mandiocaCont.update({ listComponents[x] : mandioca[x] }) 
    milho7Cont.update({ listComponents[x] : milho7[x] }) 
    milhoGlutenCont.update({ listComponents[x] : milhoGluten[x] }) 
    oleoSojaCont.update({ listComponents[x] : oleoSoja[x] }) 
    sojaFareloCont.update({ listComponents[x] : sojaFarelo[x] }) 
    trigoFareloCont.update({ listComponents[x] : trigoFarelo[x] }) 
    lisinaCont.update({ listComponents[x] : lisina[x] }) 
    metioninaCont.update({ listComponents[x] : metionina[x] }) 
    fosfatoCont.update({ listComponents[x] : fosfato[x] }) 
    calcarioCont.update({ listComponents[x] : calcario[x] }) 
    salCont.update({ listComponents[x] : sal[x] }) 
    excipienteCont.update({ listComponents[x] : excipiente[x] }) 

    x = x + 1

  fullList = {
    "Algodao" : algodaoCont,
    "Amido" : amidoCont,
    "Arroz_Farelo" : arrozFareloCont,
    "Arroz_Farelo_Deseng" : arrozFareloCont,
    "Carne_e_Ossos_Farinha_50" : carneOssosCont,
    "Citrus_Polpa" : polpaCont,
    "Mandioca_Integral_Raspa" : mandiocaCont, 
    "Milho_7,88" : milho7Cont,
    "Milho_Farelo_de_Gluten_60" : milhoGlutenCont,
    "oleo_de_Soja" : oleoSojaCont,
    "Soja_Farelo_48" : sojaFareloCont,
    "Trigo_Farelo" : trigoFareloCont,
    "Lisina_HCL" : lisinaCont,
    "Metionina" : metioninaCont,
    "Fosfato_BicAlcico" : fosfatoCont,
    "CalcArio_Calcitico" : calcarioCont,
    "Sal_Comum" : salCont,
    "Excipiente" : excipienteCont
  
  }

  df = pd.DataFrame(fullList, index=[0])
  df.to_json(outpath, indent=4)
  return fullList

@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    app.run(port=3001)