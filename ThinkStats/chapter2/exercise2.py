'''
Created on 19 Feb 2014

@author: wrightm
'''
from chapter2.main.first import ProcessTables, MakeTables
import chapter2.main.Pmf as Pmf
from chapter2.main import myplot
from chapter2.main.thinkstats import Trim

def main():

    data_dir = "../resources/"
    table, firsts, others = MakeTables(data_dir)
    ProcessTables(firsts, others)
    
    pmfFirsts = Pmf.MakePmfFromList(firsts.lengths, name = "firsts")
    pmfOthers = Pmf.MakePmfFromList(others.lengths, name = "others")

    print "firsts: %.2f +\- %.2f : mode %.2f" % (pmfFirsts.Mean(), pmfFirsts.Var(), pmfFirsts.Mode()[0])
    print "others: %.2f +\- %.2f : mode %.2f" % (pmfOthers.Mean(), pmfOthers.Var(), pmfOthers.Mode()[0])

    myplot.Hist(pmfFirsts, color='blue', edgecolor='blue')
    myplot.Hist(pmfOthers, color='green', edgecolor='green')
    myplot.Config(xlabel='weeks', ylabel='probability')
    myplot.SaveFormat(data_dir+"plots/first_and_others_gestation_periods", "png")
    myplot.Clf()
    
    pmfFirsts = Pmf.MakePmfFromList(Trim(firsts.lengths), name = "firsts")
    pmfOthers = Pmf.MakePmfFromList(Trim(others.lengths), name = "others")

    print "Trimmed firsts: %.2f +\- %.2f : mode %.2f" % (pmfFirsts.Mean(), pmfFirsts.Var(), pmfFirsts.Mode()[0])
    print "Trimmed others: %.2f +\- %.2f : mode %.2f" % (pmfOthers.Mean(), pmfOthers.Var(), pmfOthers.Mode()[0])
    
    myplot.Hist(pmfFirsts, color='blue', edgecolor='blue')
    myplot.Hist(pmfOthers, color='green', edgecolor='green')
    myplot.Config(xlabel='weeks', ylabel='probability')
    myplot.SaveFormat(data_dir+"plots/trimmed_first_and_others_gestation_periods", "png")
    myplot.Clf()
    
  
if __name__ == '__main__':
    main()