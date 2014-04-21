'''
Created on 21 Apr 2014

@author: wrightm
'''
from chapter6.main import irs, myplot
from chapter6.main.gini import SummarizeData

def main():
    
    data = irs.ReadIncomeFile('../resources/08in11si.csv')
    hist, pmf, cdf = irs.MakeIncomeDist(data)
    SummarizeData(pmf, cdf)
    
    myplot.Pmf(pmf)
    myplot.Save('../resources/plots/irs_incomes_pmf',title='irs incomes')
    myplot.Clf()
    
    myplot.Cdf(cdf)
    myplot.Save('../resources/plots/irs_incomes_cdf',title='irs incomes')
    
if __name__ == '__main__':
    main()