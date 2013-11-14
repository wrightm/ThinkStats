'''
Created on 14 Nov 2013

@author: wrightm
'''
import unittest
import myplot
from irs import ReadIncomeFile, MakeIncomeDist


class IrsTest(unittest.TestCase):


    def testIRS(self):
        
        data = ReadIncomeFile('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources/08in11si.csv')
        hist, pmf, cdf = MakeIncomeDist(data)

        plotDir='/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources/plots/'
        # plot the CDF on a log-x scale
        myplot.Clf()
        myplot.Cdf(cdf)
        myplot.Save(root=plotDir+'income_logx',
                    xscale='log',
                    xlabel='income',
                    ylabel='CDF')

        # plot the complementary CDF on a log-log scale
        myplot.Clf()
        myplot.Cdf(cdf, complement=True)
        myplot.Save(root=plotDir+'income_loglog',
                    complement=True,
                    xscale='log',
                    yscale='log',
                    xlabel='income',
                    ylabel='complementary CDF')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()