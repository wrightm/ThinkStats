'''
Created on 18 Feb 2014

@author: wrightm
'''
from chapter1.main.first import Summarize, MakeTables, ProcessTables
from chapter2.main.thinkstats import Mean, Var

def main():
    
    data_dir = "../resources/"
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)

    mu1 = round(Mean(firsts.lengths),2) 
    mu2 = round(Mean(others.lengths),2)

    var1 = round(Var(firsts.lengths, mu1),2)
    var2 = round(Var(firsts.lengths, mu2),2)
    
    print "firsts: %s +/- %s" % (mu1, var1)
    print "others: %s +/- %s" % (mu2, var2)
       
if __name__ == '__main__':
    main()