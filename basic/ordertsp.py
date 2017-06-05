# import csv
import sqlite3
import cplex
import pandas as pd
import numpy as np
from math import fabs
import datetime
from fractions import Fraction

# def compact(airport,ARRIVAL,DEPARTURE):
def order(air,depday,arrday,result_st,result_air,result_dep,air_dest,ST,alpha,beta):
    import datetime
    from fractions import Fraction
    conn = sqlite3.connect("lapistadb.db")
    airport=air
    depday=datetime.date(int(depday[0:4]),int(depday[5:7]),int(depday[8:10]))
    arrday=datetime.date(int(arrday[0:4]),int(arrday[5:7]),int(arrday[8:10]))
    D1 = datetime.date.toordinal(depday)
    D2 = (datetime.date.toordinal(arrday))+1
    
    dates=[]
    for i in range(D1,D2):
        dates.append(datetime.date.fromordinal(i))
    print(dates)   
    dif_dates=[]
    for i in dates:
        today = datetime.date.today()
        someday = i
        diff = someday - today
        dif_dates.append(diff.days)
    min_dif=min(dif_dates)
    max_dif=max(dif_dates)
    
    print(dif_dates)
 
    #airport = ['ICN', 'LHR', 'CDG']
    
    cc = []
    route_id=[]
    for i in airport:
        for j in airport:
            if j==air_dest[airport.index(i)]:
                cursor = conn.execute("SELECT ROUTE_ID from route where r_dest=(?) and r_origin=(?)", (j, i))
                for row in cursor:
                    route_id.append(str(row[0]))
                    cc.append(max_dif-min_dif+1)
            else :
                cc.append(0)
    print(len(route_id))
    print(len(dif_dates))
    scale_cost=[]
    for i in route_id:
        for j in dif_dates:
            #if route_id =0:
            cursor2= conn.execute("SELECT COST from trend where ROUTE_ID=(?) and daysleft=(?)",(i,j))
            for row in cursor2:
                a=float(row[0])
                scale_cost.append(a)
                
    print(len(dates))
    
    ini_price=[]
    for i in route_id:
        for j in dates:
            cursor3 = conn.execute("SELECT INITIAL_COST from initialprice where ROUTE_ID=(?) and INITIAL_DATE=(?)",(i,j))
            for row in cursor3:
                ini_price.append(float(row[0]))
                
    print(len(ini_price)) 
            
    depday=depday.toordinal()
    arrday=arrday.toordinal()
    for i in dates:
        dates[dates.index(i)]=i.toordinal()
    
    costs=[]
    for i in zip(scale_cost,ini_price):
        cost=i[0]*i[1]
        costs.append(cost)
    print(len(costs))
    dates=dates*len(route_id)
    aa = []
    fk = 0
    for ccc in cc:
        aa.append(list(dates[fk:fk + ccc]))
        fk += ccc
    print(aa)
    dates = [aa[len(airport) * i:len(airport) * (i + 1)] for i in range(len(airport))]
   
    f = []
    s = []
    dep = []
    arr = []
    dif = []
    
    c = cplex.Cplex()
    c.objective.set_sense(c.objective.sense.minimize)
    cc = np.array(cc)
    cc = cc.reshape(len(airport), len(airport))
    print(cc)
    nbairports = len(airport)
    
    scale=84*float(Fraction(beta,2*alpha))
    dfd = [0]
    for i in range(1, nbairports):
        dfd.append(scale)

    flight = []
    for i in range(nbairports):
        f.append([])
        for j in range(nbairports):
            f[i].append([])
            for k in range(cc[i][j]):
                varname = "f" + str(i) + str(j) + str(k)
                flight.append(varname)
                f[i][j].append(varname)
    c.variables.add(names=flight, lb=[0] * len(flight),
                    ub=[1] * len(flight),
                    types=["B"] * len(flight), obj=costs)
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for j in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, [1] * len(thevars))], senses=["E"], rhs=[1])
    for i in range(nbairports):
        sname = "s_" + str(i)
        s.append(sname)
    c.variables.add(names=s, lb=[0.0] * len(s))
    for i in range(nbairports):
        depname = "dep_" + str(i)
        dep.append(depname)
    c.variables.add(names=dep, lb=[0.0] * len(dep))
    for i in range(nbairports): 
        arrname = "arr" + str(i)
        arr.append(arrname)
    c.variables.add(names=arr, lb=[0.0] * len(arr))
    for i in range(nbairports):
        difname = "dif_" + str(i)
        dif.append(difname)
    c.variables.add(names=dif, lb=[0.0] * len(dif))
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for j in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, [1] * len(thevars))], senses=["E"], rhs=[1])
        # cpx.objective.set_linear(zip(thevars, thecoefs))
    for j in range(nbairports):
        thevars = []
        thecoefs = []
        for i in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, [1] * len(thevars))], senses=["E"], rhs=[1])
    for i in range(nbairports):
        thevars = []
        thecoefs = []
        for k in range(cc[i][i]):
            thevars.append(f[i][i][k])
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, [1] * len(thevars))], senses=["E"], rhs=[0])
    # arr[i] - sum(j in AIRPORT , k in SCHEDULE)b[j][i][k]*f[j][i][k]==0;
    for i in range(nbairports):
        thevars = [arr[i]]
        thecoefs = [-1]
        for j in range(nbairports):
            for k in range(cc[j][i]):
                thevars.append(f[j][i][k])
                thecoefs.append(dates[j][i][k])
        c.linear_constraints.add([cplex.SparsePair(thevars, thecoefs)],
                                 senses="E",
                                 rhs=[0.0])
    arr[0] == arrday
    for i in range(0, 1):
        thevars = [arr[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars, thecoefs)],
                                 senses="E",
                                 rhs=[arrday])
        # dep[i] - sum(j in AIRPORT , k in SCHEDULE)a[i][j][k]*f[i][j][k]==0;
    for i in range(nbairports):
        thevars = [dep[i]]
        thecoefs = [-1]
        for j in range(nbairports):
            for k in range(cc[i][j]):
                thevars.append(f[i][j][k])
                thecoefs.append(dates[i][j][k])
        c.linear_constraints.add([cplex.SparsePair(thevars, thecoefs)],
                                 senses="E",
                                 rhs=[0.0])
    # dep[0] == DEPARTURE
    for i in range(0, 1):
        thevars = [dep[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars, thecoefs)],
                                 senses="E",
                                 rhs=[depday])
        # s[i]==dep[i]-arr[i];
    for i in range(1, nbairports):
        thevars = [s[i]]
        thecoefs = [1]
        c.linear_constraints.add([cplex.SparsePair(thevars, thecoefs)],
                                 senses="G",
                                 rhs=[1.0])
    for i in range(1, nbairports):
        thevars = [s[i]]
        thecoefs = [1]
        thevars.append(dep[i])
        thecoefs.append(-1)
        thevars.append(arr[i])
        thecoefs.append(1)
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, thecoefs)], senses=["E"], rhs=[0.0])
    
    for i in range(nbairports):
        thevars = [dif[i]]
        thecoefs = [1]
        thevars.append(s[i])
        print(depday,arrday)
        print(ST[i],sum(ST))
        thecoefs.append(-1)
        thevars.append(arr[0])
        thecoefs.append(float(Fraction(ST[i],sum(ST))))
        thevars.append(dep[0])
        thecoefs.append(-float(Fraction(ST[i], sum(ST))))
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, thecoefs)], senses=["G"], rhs=[0.0])
    
    for i in range(nbairports):
        thevars = [dif[i]]
        thecoefs = [1]
        thevars.append(s[i])
        thecoefs.append(1)
        thevars.append(arr[0])
        thecoefs.append(-float(Fraction(ST[i], sum(ST))))
        thevars.append(dep[0])
        thecoefs.append(float(Fraction(ST[i],sum(ST))))
        c.linear_constraints.add(lin_expr=[cplex.SparsePair(thevars, thecoefs)], senses=["G"], rhs=[0.0])

       
    c.solve()
    sol = c.solution
    print()
    # solution.get_status() returns an integer code
    print("Solution status = ", sol.get_status(), ":")
    # the following line prints the corresponding string
    print(sol.status[sol.get_status()])
    # result_st = []
    # result_air=[]
    # result_dep=[]
    if sol.is_primal_feasible():
        print("Solution value  = ", sol.get_objective_value())
        for_dep=[]
        for i in range(nbairports):
            akak=int(sol.get_values(dep[i]))
            print("departure time from airport %s = %s" % (airport[i],datetime.date.fromordinal(akak) ))
            ddd=datetime.date.fromordinal(akak)
            ddd=str(ddd)
            for_dep.append((airport[i],ddd ))
        for_dep.sort(key=lambda tup:tup[1])
        for i in range(nbairports):
            result_dep.append(for_dep[i][1])
            result_air.append(for_dep[i][0])
        result_air.append('ICN')
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
                        print(airport[i], "->", airport[j])
    else:
        print("No solution available.")
# compact(air, arrday, depday)
    print (result_st)
    print (result_air)
    print (result_dep)