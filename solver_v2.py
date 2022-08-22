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
    model.pprint()

    model.obj = Objective(expr = objFun, sense = minimize) 

    model.constrs = ConstraintList()

    model.constrs.add(expr = model.x[0] <= 4)
    model.constrs.add(expr = 2 * model.x[1] <= 12)
    model.constrs.add(expr = 3 * model.x[0] + 2* model.x[1] <= 18)

    #print("Constrains: ", model.constrs[1].expr)

    optimizer = SolverFactory('glpk')
    results = optimizer.solve(model, tee = False)

    cost = model.obj.expr()
    print("Valor: ", cost)

    for i in range(2):
        x_value = model.x[i].value
        print("x", i, " = ", x_value)


    status = results.solver.status
    print("Status: ", status)

    termination = results.solver.termination_condition
    print("Criterio de Parada: ", termination) 




