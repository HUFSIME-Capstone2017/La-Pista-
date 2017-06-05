#import csv
import sqlite3
import cplex
import pandas as pd
import numpy as np


# def asdf(a1,a2,a3):
#     airpot = a1
#     asdf = a2
#     asdfff = a3

#     summ = airpot + asdf + asdfff

#     return summ



class TSP:
    def __init__(self, nbairports):
        self.nbairports = nbairports
        self.conn = sqlite3.connect("lapistadb.db")
        self.cur = self.conn.cursor()
        self.cc=[]
        self.airport = ['ICN','LHR','CDG','FCO','MAD']
        self.prefer= [0,3.3,3.5,3.1,2.5]
        for i in self.airport:
            for j in self.airport:
                self.cur.execute("select * from csv where r_dest==(?) and r_origin==(?)", (i, j))
                b = self.cur.fetchall()
                self.cc.append(int(len(b)))   
        #print (sum(cc))
        self.b=[]
        self.a=[]
        self.costs=[]
        for i in self.airport:
            for j in self.airport:
                cursor = self.conn.execute("SELECT dep_day,arr_day,sch_cost from csv where r_dest=(?) and r_origin=(?)", (i, j) )
                ada=[]
                for row in cursor:
                    self.b.append(int(row[0]))
                    self.a.append(int(row[1]))
                    self.costs.append(int(row[2]))
        self.ARRIVAL = 15
        self.DEPARTURE = 1
        self.aa=[]
        self.bb=[]
        self.f = 0
        for c in self.cc:
            self.aa.append(list(self.a[self.f:self.f+c]))
            self.bb.append(list(self.b[self.f:self.f+c]))
            self.f+=c
        #print(aa)
        self.b = [self.bb[len(self.airport)*i :len(self.airport)* (i+1)] for i in range(len(self.airport))]
        self.a = [self.aa[len(self.airport)*i :len(self.airport)* (i+1)] for i in range(len(self.airport))]
        #print(len(costs))
        #print(a)
        self.cc = np.array(self.cc)
        self.cc = self.cc.reshape(len(self.airport),len(self.airport))
        print(self.cc)
        self.nbairports = len(self.airport)
        self.df=[0]
        for i in range(1,self.nbairports):
            self.df.extend([6.9*nbairports])
        # problem variables
        self.f = []
        self.s = []
        self.dep = []
        self.arr = []
        self.dif = []
    def setupproblem(self, c):
        c.objective.set_sense(c.objective.sense.minimize)
        
        flight = []
        for i in range(self.nbairports):
            self.f.append([])
            #print("i",i)
            for j in range(self.nbairports):
                self.f[i].append([])
                #print (j)
                for k in range(self.cc[i][j]):
                    varname = "f"+str(i)+str(j)+str(k)
                    flight.append(varname)
                    self.f[i][j].append(varname)
        
        c.variables.add(names = flight, lb = [0] * len(flight),
                        ub = [1] * len(flight),
                        types = ["B"] * len(flight), obj=self.costs)
        
        for i in range(self.nbairports):
            thevars = []
            thecoefs = []
            for j in range(self.nbairports):
                for k in range(self.cc[i][j]):
                    thevars.append(self.f[i][j][k])
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
          
     
        for i in range(self.nbairports):
            sname = "s_"+str(i)
            self.s.append(sname)
        c.variables.add(names = self.s, lb = [0.0]* len(self.s))
        
        for i in range(self.nbairports):
            depname = "dep_"+str(i)
            self.dep.append(depname)
        c.variables.add(names = self.dep, lb = [0.0]* len(self.dep))
        
        for i in range(self.nbairports):
            arrname = "arr"+str(i)
            self.arr.append(arrname)
        c.variables.add(names = self.arr, lb = [0.0]* len(self.arr))
        
        for i in range(self.nbairports):
            difname = "dif_"+str(i)
            self.dif.append(difname)
        c.variables.add(names = self.dif, lb = [0.0]* len(self.dif), obj=self.df)
        for i in range(self.nbairports):
            thevars = []
            thecoefs = []
            for j in range(self.nbairports):
                for k in range(self.cc[i][j]):
                    thevars.append(self.f[i][j][k])
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
            # cpx.objective.set_linear(zip(thevars, thecoefs))
            
                
        for j in range(self.nbairports):
            thevars = []
            thecoefs = []
            for i in range(self.nbairports):
                for k in range(self.cc[i][j]):
                    thevars.append(self.f[i][j][k])
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [1])
            
        for i in range(self.nbairports):
            thevars = []
            thecoefs = []
            for k in range(self.cc[i][i]):
                thevars.append(self.f[i][i][k])
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars,[1] * len(thevars))],senses = ["E"], rhs = [0])
        #   arr[i] - sum(j in AIRPORT , k in SCHEDULE)b[j][i][k]*f[j][i][k]==0;
        for i in range(self.nbairports):
            thevars = [self.arr[i]]
            thecoefs = [-1]
            for j in range(self.nbairports):
                    for k in range(self.cc[j][i]):
                        thevars.append(self.f[j][i][k])
                        thecoefs.append(self.a[j][i][k])
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "E" ,
                                 rhs = [0.0] )
        #arr[0] == ARRIVAL
        for i in range(0,1):
            thevars = [self.arr[i]]
            thecoefs = [1]
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "E" ,
                                 rhs = [self.ARRIVAL] )   
        
        #dep[i] - sum(j in AIRPORT , k in SCHEDULE)a[i][j][k]*f[i][j][k]==0;    
        for i in range(self.nbairports):
            thevars = [self.dep[i]]
            thecoefs = [-1]
            for j in range(self.nbairports):
                    for k in range(self.cc[i][j]):
                        thevars.append(self.f[i][j][k])
                        thecoefs.append(self.b[i][j][k])
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "E" ,
                                 rhs = [0.0] )
        
        #dep[0] == DEPARTURE    
        for i in range(0,1):
            thevars = [self.dep[i]]
            thecoefs = [1]
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "E" ,
                                 rhs = [self.DEPARTURE] )   
  
        # s[i]==dep[i]-arr[i];
        for i in range(1,self.nbairports):
            thevars = [self.s[i]]
            thecoefs = [1]
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "G" ,
                                 rhs = [1.0] ) 
        
        for i in range(1,self.nbairports):
            thevars = [self.s[i]]
            thecoefs=[1]
            thevars.append(self.dep[i])
            thecoefs.append(-1)   
            thevars.append(self.arr[i])
            thecoefs.append(1) 
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["E"], rhs = [0.0])
        #dif[i] >= s[i] - ((arr[i]-dep[i])/n);
        for i in range(self.nbairports):
            thevars = [self.dif[i]]
            thecoefs = [1]
            thevars.append(self.s[i])
            thecoefs.append(-1)   
            thevars.append(self.arr[0])
            thecoefs.append((1.0)*self.prefer[i]/sum(self.prefer))  
            thevars.append(self.dep[0])
            thecoefs.append((-1.0)*self.prefer[i]/sum(self.prefer))   
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["G"], rhs = [0.0])
        for i in range(self.nbairports):
            thevars = [self.dif[i]]
            thecoefs = [1]
            thevars.append(self.s[i])
            thecoefs.append(1)   
            thevars.append(self.arr[0])
            thecoefs.append((-1.0)*self.prefer[i]/sum(self.prefer))   
            thevars.append(self.dep[0])
            thecoefs.append((1.0)*self.prefer[i]/sum(self.prefer))   
            c.linear_constraints.add(lin_expr =[cplex.SparsePair(thevars, thecoefs)],senses = ["G"], rhs = [0.0])
          
        for i in range(0,4):
            thevars = [self.dep[4]]
            thecoefs = [1]
            thevars.append(self.dep[i])
            thecoefs.append(-1)
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "G" ,
                                 rhs = [0.0] )  
            
        for i in range(1,2):
            thevars = [self.dep[i]]
            thecoefs = [1]
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "L" ,
                                 rhs = [8] )   
        for i in range(1,2):
            thevars = [self.arr[i]]
            thecoefs = [1]
            c.linear_constraints.add([cplex.SparsePair(thevars,thecoefs)],                             
                                 senses = "G" ,
                                 rhs = [6] )   
       
    def compact(self):
        self.result_st=[]
        self.origin=[]
        self.destination=[]
        self.departure=[]
        c = cplex.Cplex()
        self.setupproblem(c)
        c.solve()
        c.write("hh.lp")
        sol = c.solution
        print()
        # solution.get_status() returns an integer code
        print("Solution status = " , sol.get_status(), ":")
        # the following line prints the corresponding string
        print(sol.status[sol.get_status()])
        if sol.is_primal_feasible():
            print("Solution value  = ", sol.get_objective_value())
            for i in range(self.nbairports):
                print("departure time from airport %s = %d" % (self.airport[i], sol.get_values(self.dep[i])))
                self.departure.extend([int(sol.get_values(self.dep[i]))])
            for i in range(self.nbairports):
                print("arrival time to airport %s = %d" % (self.airport[i], sol.get_values(self.arr[i])))
            for i in range(self.nbairports):
                print("staytime of airport %s = %d" % (self.airport[i], sol.get_values(self.s[i])))
            for i in range(self.nbairports):
                print("difstaytime of airport %s = %d" % (self.airport[i], sol.get_values(self.dif[i])))            
            for i in range(self.nbairports):
                for j in range(self.nbairports):
                    for k in range(self.cc[i][j]):
                        if sol.get_values(self.f[i][j][k]) > 0.5:
                            print(self.airport[i],"->",self.airport[j])
                            self.origin.extend([self.airport[i]])
                            self.destination.extend([self.airport[j]])

        
        else:
            print("No solution available.")
        self.for_sort=zip(self.departure,self.airport)
        self.for_sort.sort()
       
        self.new_airport=[]
        self.new_departure=[]


        for i,j in self.for_sort:
            self.new_airport.append(j)
            self.new_departure.append(i)

        print(self.new_airport) 
        print(self.new_departure)

tsp = TSP(5)
tsp.compact()
#compact(4)
#print (result_st)