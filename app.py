import os
import pandas as pd
from flask import Flask, request, render_template, redirect, send_file
from solver_v2 import solve_model
from fpdf import FPDF
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app)


filename = None

ALLOWED_EXTENSIONS = set(['csv'])


@app.route('/solver', methods=['GET'])
def fileHandler():
    pathname = os.path.abspath("trabalho_po_backend/uploads/" + filename).replace("trabalho_po_backend", "", 1)
    data = pd.read_csv(pathname, sep=',')

    # print(data)

    componente = data.Componente
    exigencias = data.Exigencias
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

    exigenciasCont = {}
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
    while x < len(sal):
        exigenciasCont.update({listComponents[x]: exigencias[x]})
        algodaoCont.update({listComponents[x]: algodao[x]})
        amidoCont.update({listComponents[x]: amido[x]})
        arrozFareloCont.update({listComponents[x]: arrozFarelo[x]})
        arrozFareloDesengCont.update({listComponents[x]: arrozFareloDeseng[x]})
        carneOssosCont.update({listComponents[x]: carneOssos[x]})
        polpaCont.update({listComponents[x]: polpa[x]})
        mandiocaCont.update({listComponents[x]: mandioca[x]})
        milho7Cont.update({listComponents[x]: milho7[x]})
        milhoGlutenCont.update({listComponents[x]: milhoGluten[x]})
        oleoSojaCont.update({listComponents[x]: oleoSoja[x]})
        sojaFareloCont.update({listComponents[x]: sojaFarelo[x]})
        trigoFareloCont.update({listComponents[x]: trigoFarelo[x]})
        lisinaCont.update({listComponents[x]: lisina[x]})
        metioninaCont.update({listComponents[x]: metionina[x]})
        fosfatoCont.update({listComponents[x]: fosfato[x]})
        calcarioCont.update({listComponents[x]: calcario[x]})
        salCont.update({listComponents[x]: sal[x]})
        excipienteCont.update({listComponents[x]: excipiente[x]})

        x = x + 1

    fullList = {
        "Exigencias": exigenciasCont,
        "Algodao_Farelo_39": algodaoCont,
        "Amido": amidoCont,
        "Arroz_Farelo": arrozFareloCont,
        "Arroz_Farelo_Deseng": arrozFareloDesengCont,
        "Carne_e_Ossos_Farinha_50": carneOssosCont,
        "Citrus_Polpa": polpaCont,
        "Mandioca_Integral_Raspa": mandiocaCont,
        "Milho_7,88": milho7Cont,
        "Milho_Farelo_de_Gluten_60": milhoGlutenCont,
        "oleo_de_Soja": oleoSojaCont,
        "Soja_Farelo_48": sojaFareloCont,
        "Trigo_Farelo": trigoFareloCont,
        "Lisina_HCL": lisinaCont,
        "Metionina": metioninaCont,
        "Fosfato_BicAlcico": fosfatoCont,
        "CalcArio_Calcitico": calcarioCont,
        "Sal_Comum": salCont,
        "Excipiente": excipienteCont

    }

    df = pd.DataFrame(fullList)
    solve_model(fullList)
    return fullList


app.config["FILE_UPLOADS"] = os.path.abspath("trabalho_po_backend/uploads").replace("trabalho_po_backend", "", 1)

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
  global filename
  if request.method == 'POST':

    if request.files:

        file = request.files['file']

        if file.filename == '':
            print('File must have a filename')
            return redirect(request.url)

        if not allowed_file(file.filename):
            print('Filetype not allowed')
            return redirect(request.url)

        file.save(os.path.join(app.config['FILE_UPLOADS'], file.filename))
        filename = file.filename
        #print("File uploaded")
        fileHandler()
        return render_template('download.html')

  return render_template('index.html')

def generatePdf():
    pdf = FPDF()
    pdf.add_page(orientation='L')
    pdf.set_font("Arial", size = 7)
    f = open("file_out.txt", "r")
    pdf.set_margins(0,0,0)
    for x in f:
        pdf.cell(1, 10, txt = x, ln = 1, align = 'l' )
    pdf.output("Resultado.pdf")

generatePdf()

@app.route('/return-file/')
def return_file():
    path = os.path.abspath('trabalho_po_backend/Resultado.pdf').replace("trabalho_po_backend", "", 1)
    return send_file(path)

@app.route('/download/')
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(port=3001)