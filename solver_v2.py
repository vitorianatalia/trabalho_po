from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import * 


def solve_model(tabela):
    model = ConcreteModel()
        
    #variaveis

    items = list(range(len(tabela)))
    model.x = Var(items, within = NonNegativeReals)

    objFun = 0
    i = 0
    for key in tabela:
        floatPrice = tabela[key]['Preco'].replace(',', ".")
        objFun = objFun + float(floatPrice) * model.x[i]
        print(tabela[key]["Preco"])
        i+=1
        
    print(objFun)
    
    #objetivo
    model.obj = Objective(expr = objFun, sense = minimize) 

    #restricoes
    model.constrs = ConstraintList()

    constraints = []
    #print('Len tabela: ' + str(len(tabela['Exigencias'])))
    #j = 0

    listComponents = []
    for key in tabela['Algodao_Farelo_39']:
        listComponents.append(key)
    

    #print ("LEN TABELA: " + str(len(tabela)))
    j=0
    while j < len(tabela['Exigencias']):
        aux = 0
        print('Tabela keys' + str(len(tabela.keys())))
        for key in tabela.keys():
            #essa linha ta errada, por algum motivo o len(tabela.keys) é 19 e nao 69 como deveriamos ter
            #no caso, deveriamos ter 69 restrições, nao 19
            # print (key + ' : ' + listComponents[j] + ' : ' + str(tabela[key][listComponents[j]]))
            aux = aux + float(tabela[key][listComponents[j]].replace(',', ".")) * model.x[j]
        j+=1
        constraints.append(aux)

    print('Constraints: ' + str(len(constraints)))
    
    listExigencias = []
    for key in tabela['Exigencias']:
        aux = float(tabela['Exigencias'][key].replace(',', "."))
        listExigencias.append(aux)
    
    i = 0
    for i in range(len(listExigencias)):
        print(listExigencias[i])

    print("Lista de exigencias: " + str(len(listExigencias)))
    print("Tamanho Exigencias: " + str(len(tabela['Exigencias'])))

    i = 0
    while i < len(tabela['Exigencias']):
        #print (constraints[i] + '\n')
        tableLen = len(tabela['Exigencias'])
        if i != tableLen - 1:
            model.constrs.add(expr = constraints[i] >= listExigencias[i])
        else:
            model.constrs.add(expr = constraints[i] == 1)
        print(i)
        #print("Constrains: ", model.constrs[i].expr)
        i+=1

    model.pprint()
    # model.constrs.add(expr = model.x[0] <= 4)
    # model.constrs.add(expr = 2 * model.x[1] <= 12)
    # model.constrs.add(expr = 3 * model.x[0] + 2* model.x[1] <= 18)
    optimizer = SolverFactory('glpk')
    results = optimizer.solve(model, tee = False)

    cost = model.obj.expr()
    print("Valor: ", cost)

    for i in range(len(constraints)):
        x_value = model.x[i].value
        print("x", i, " = ", x_value)


    status = results.solver.status
    print("Status: ", status)

    termination = results.solver.termination_condition
    print("Criterio de Parada: ", termination) 




