import gurobipy as gp
from gurobipy import GRB
import numpy as np

totalPressedButtons = 0

env = gp.Env(empty=True)
env.setParam('OutputFlag',False)
env.start()

with open("datas/2025_day10_data", 'r') as file:
    for line in file:
        line = line.strip()
        a = line.split(" ")

        wiringSchematics = []
        for wiring in a[1:-1]: #only those between parentheses
            numberString = wiring[1:-1].split(',')
            schema = []
            for numberS in numberString:
                schema.append(int(numberS))
            wiringSchematics.append(schema)

        lights = []
        brackets = a[-1][1:-1]
        bracketNbString = brackets.split(',')
        for numberS in bracketNbString:
            lights.append(int(numberS))

        A = []
        for j in range(len(lights)):
            line = []
            for wiring in wiringSchematics:
                line.append(j in wiring)
            A.append(line)
        
        A = np.array(A)
        b = np.array(lights)
        c = np.ones(len(wiringSchematics))

        model = gp.Model(env=env)

        x = model.addMVar(shape=c.shape, vtype=GRB.INTEGER)

        model.setObjective(c @ x, GRB.MINIMIZE)

        model.addConstr(A @ x == b)

        model.optimize()
        totalPressedButtons += model.ObjVal


print("Part 2 :", int(totalPressedButtons))