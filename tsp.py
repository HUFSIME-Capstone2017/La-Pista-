#import csv
import sqlite3
import cplex
conn = sqlite3.connect("lapistadb.db")
import pandas as pd
import numpy as np

cur = conn.cursor()
cc=[]
airport = ['ICN','LHR','CDG','FCO']
for i in airport:
    for j in airport:
        cur.execute("select * from csv where r_dest==(?) and r_origin==(?)", (i, j))
        b = cur.fetchall()
        cc.append(int(len(b)))   
#print (sum(cc))
b=[]
a=[]
costs=[]
for i in airport:
    for j in airport:
        cursor = conn.execute("SELECT dep_day,arr_day,sch_cost from csv where r_dest=(?) and r_origin=(?)", (i, j) )
        ada=[]
        for row in cursor:
            b.append(int(row[0]))
            a.append(int(row[1]))
            costs.append(int(row[2]))
ARRIVAL = max(b)
DEPARTURE = min(b)
aa=[]
bb=[]
f = 0
for c in cc:
    aa.append(list(a[f:f+c]))
    bb.append(list(b[f:f+c]))
    f+=c
#print(aa)
b = [bb[len(airport)*i :len(airport)* (i+1)] for i in range(len(airport))]
a = [aa[len(airport)*i :len(airport)* (i+1)] for i in range(len(airport))]
#print(len(costs))
#print(a)
cc = np.array(cc)
cc = cc.reshape(len(airport),len(airport))
print(cc)
from math import fabs
import cplex
import numpy as np
# number of airports
nbairports = len(airport)
df=[0]
for i in range(1,nbairports):
    df.extend([50])
# problem variables
f = []
s = []
dep = []
arr = []
dif = []
def setupproblem(c):
    c.objective.set_sense(c.objective.sense.minimize)
      
    
    flight = []
    for i in range(nbairports):
        f.append([])
        #print("i",i)
        for j in range(nbairports):
            f[i].append([])
            #print (j)
            for k in range(cc[i][j]):
                varname = "f"+str(i)+str(j)+str(k)
                flight.append(varname)
                f[i][j].append(varname)
    
    c.variables.add(names = flight, lb = [0] * len(flight),
                    ub = [1] * len(flight),
                    types = ["B"] * len(flight), obj=costs)
    
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for j in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
      
 
    for i in range(nbairports):
        sname = "s_"+str(i)
        s.append(sname)
    c.variables.add(names = s, lb = [0.0]* len(s))
    
    for i in range(nbairports):
        depname = "dep_"+str(i)
        dep.append(depname)
    c.variables.add(names = dep, lb = [0.0]* len(dep))
    
    for i in range(nbairports):
        arrname = "arr"+str(i)
        arr.append(arrname)
    c.variables.add(names = arr, lb = [0.0]* len(arr))
    
    for i in range(nbairports):
        difname = "dif_"+str(i)
        dif.append(difname)
    c.variables.add(names = dif, lb = [0.0]* len(dif), obj=df)
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for j in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
        # cpx.objective.set_linear(zip(thevars, thecoefs))
        
            
    for j in range(nbairports):
        thevars = []
        thecoefs = []
        for i in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
        
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for k in range(cc[i][i]):
            thevars.append(f[i][i][k])
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [0])
    #   arr[i] - sum(j in AIRPORT , k in SCHEDULE)b[j][i][k]*f[j][i][k]==0;
    for i in range(nbairports):
        thevars = [arr[i]]
        thecoefs = [-1]
        for j in range(nbairports):
                for k in range(cc[j][i]):
                    thevars.append(f[j][i][k])
                    thecoefs.append(a[j][i][k])
        c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                             senses = "E" ,
                             rhs = [0.0] )
    #arr[0] == ARRIVAL
    for i in range(0,1):
        thevars = [arr[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                             senses = "E" ,
                             rhs = [ARRIVAL] )   
    
    #dep[i] - sum(j in AIRPORT , k in SCHEDULE)a[i][j][k]*f[i][j][k]==0;    
    for i in range(nbairports):
        thevars = [dep[i]]
        thecoefs = [-1]
        for j in range(nbairports):
                for k in range(cc[i][j]):
                    thevars.append(f[i][j][k])
                    thecoefs.append(b[i][j][k])
        c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                             senses = "E" ,
                             rhs = [0.0] )
    
    #dep[0] == DEPARTURE    
    for i in range(0,1):
        thevars = [dep[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                             senses = "E" ,
                             rhs = [DEPARTURE] )   
    # s[i]==dep[i]-arr[i];
    
    for i in range(1,nbairports):
        thevars = [s[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                             senses = "G" ,
                             rhs = [1.0] ) 
    
    for i in range(1,nbairports):
        thevars = [s[i]]
        thecoefs=[1]
        thevars.append(dep[i])
        thecoefs.append(-1)   
        thevars.append(arr[i])
        thecoefs.append(1) 
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["E"], rhs = [0.0])
    #dif[i] >= s[i] - ((arr[i]-dep[i])/n);
    for i in range(nbairports):
        thevars = [dif[i]]
        thecoefs = [1]
        thevars.append(s[i])
        thecoefs.append(-1)   
        thevars.append(arr[0])
        thecoefs.append((1.0)/nbairports)   
        thevars.append(dep[0])
        thecoefs.append((-1.0)/nbairports)   
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["G"], rhs = [0.0])
    for i in range(nbairports):
        thevars = [dif[i]]
        thecoefs = [1]
        thevars.append(s[i])
        thecoefs.append(1)   
        thevars.append(arr[0])
        thecoefs.append((-1.0)/nbairports)   
        thevars.append(dep[0])
        thecoefs.append((1.0)/nbairports)   
        c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["G"], rhs = [0.0])
    
   
result_st=[]
def compact(airport_count):
    nbairports = airport_count
    c = cplex.Cplex()
    setupproblem(c)
    c.solve()
    sol = c.solution
    print()
    # solution.get_status() returns an integer code
    print("Solution status = " , sol.get_status(), ":")
    # the following line prints the corresponding string
    print(sol.status[sol.get_status()])
    if sol.is_primal_feasible():
        print("Solution value  = ", sol.get_objective_value())
        for i in range(nbairports):
            print("departure time from airport %s = %d" % (airport[i], sol.get_values(dep[i])))
        for i in range(nbairports):
            print("arrival time to airport %s = %d" % (airport[i], sol.get_values(arr[i])))
        for i in range(nbairports):
            print("staytime of airport %s = %d" % (airport[i], sol.get_values(s[i])))
            result_st.extend([int(sol.get_values(s[i]))])
        for i in range(nbairports):
            print("difstaytime of airport %s = %d" % (airport[i], sol.get_values(dif[i])))            
        for i in range(nbairports):
            for j in range(nbairports):
                for k in range(cc[i][j]):
                    if sol.get_values(f[i][j][k]) > 0.5:
                        print(airport[i],"->",airport[j])
      
    else:
        print("No solution available.")
compact(4)
print (result_st)