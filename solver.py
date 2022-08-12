from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import * 

model = ConcreteModel()

#variaveis

model.x1 = Var(within = NonNegativeReals, bounds = (0, 4))
model.x2 = Var(within = NonNegativeReals, bounds = (0, 6))
#model.x = Var(bounds =(0, None)) -> define limites superiores e inferiores para a variavel de decisão

# print(model.x1.domain)
# print(model.x1.bounds)

#funcao objetivo
model.obj = Objective(expr = 3 * model.x1 + 5 * model.x2, sense = maximize) #default é minimize

#print(model.obj.expr) #expression
# print(model.obj.sense) #1 = minimize, -1 = maximize


#restricoes
# model.c1 = Constraint(expr = model.x1 <= 4)
# model.c2 = Constraint(expr = 2 * model.x2 <= 12)
model.c3 = Constraint(expr = 3 * model.x1 + 2* model.x2 <= 18)

#model.pprint()

optimizer = SolverFactory('glpk')

#usando solver p resolver
results = optimizer.solve(model, tee = False) #tee = true para mostrar o log de resolucoes

cost = model.obj.expr()
print("Valor: ", cost)

x1_value = model.x1.value
x2_value = model.x2.value

print("x1 = ", x1_value)
print("x2 = ", x2_value)

status = results.solver.status
print("Status: ", status) #ok se nao teve erro

termination = results.solver.termination_condition
print("Criterio de Parada: ", termination) #optimal = solucao otima, infeasible, unbounded (infinito)





