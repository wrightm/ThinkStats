'''
Created on 27 Feb 2014

@author: wrightm
'''
from chapter4.main.populations_cdf import MakeFigures
from chapter4.main.irs import ReadIncomeFile, MakeIncomeDist
from chapter4.main import myplot

def main():

    # population
    MakeFigures()

    #
    data = ReadIncomeFile()
    hist, pmf, cdf = MakeIncomeDist(data)

    # plot the CDF on a log-x scale
    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='../resources/plots/income_logx',
                xscale='log',
                xlabel='income',
                ylabel='CDF')

    # plot the complementary CDF on a log-log scale
    myplot.Clf()
    myplot.Cdf(cdf, complement=True)
    myplot.Save(root='../resources/plots/income_loglog',
                complement=True,
                xscale='log',
                yscale='log',
                xlabel='income',
                ylabel='complementary CDF')

if __name__ == '__main__':
    main()