from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *
import sys


def solve_model(tabela):
    model = ConcreteModel()
        
    #writes to txt
    f = open('file_out.txt', 'w+')
    f.truncate()
    sys.stdout = f

    #variaveis
    items = list(range(len(tabela)))
    model.x = Var(items, within = NonNegativeReals)

    #objetivo
    objFun = 0
    i = 0
    for key in tabela:
        if key != 'Exigencias':
            floatPrice = tabela[key]['Preco'].replace(',', ".")
            objFun = objFun + float(floatPrice) * model.x[i]
        i+=1

    model.obj = Objective(expr = objFun, sense = minimize) 

    #restricoes
    model.constrs = ConstraintList()

    constraints = []
    listComponents = []
    for key in tabela['Algodao_Farelo_39']:
        listComponents.append(key)

    j = i = 0
    while i < len(listComponents):
        aux = 0
        j = 0
        for key in tabela.keys():
            if key != 'Exigencias':   
                aux = aux + float(tabela[key][listComponents[i]].replace(',', ".")) * model.x[j]
                j+=1
            
        i+=1
        constraints.append(aux)
    
    listExigencias = []
    for key in tabela['Exigencias']:
        if key != 'Exigencias':
            aux = float(tabela['Exigencias'][key].replace(',', "."))
            listExigencias.append(aux)

    i = 0
    while i < len(listExigencias) -1:
        if (type(constraints[i]) != int):
            model.constrs.add(expr = constraints[i] >= listExigencias[i])
        i+=1

    #GLPK
    model.constrs.pprint()
    optimizer = SolverFactory('glpk')
    results = optimizer.solve(model, tee = False)


    #print model
    cost = model.obj.expr()
    print("Valor: ", cost)

    for i in range(len(tabela)):
        x_value = model.x[i].value
        print("x", i, " = ", x_value)


    status = results.solver.status
    print("Status: ", status)

    termination = results.solver.termination_condition
    print("Criterio de Parada: ", termination) 

    model.pprint()
    f.close()



