'''
Created on 6 Mar 2014

@author: wrightm
'''
from chapter5.main.continuous import RenderNormalCdf
from chapter5.main.Cdf import Cdf, MakeCdfFromList
import random
from chapter5.main import myplot
from matplotlib import pyplot

from scipy import stats

def compare_poincare_baker():

    """
    bread measurements by poincare 365 fitted normal distribution with mean 950g and 50g standard deviation
    """ 

    poincare_sample = [ random.normalvariate(950, 50) for i in xrange(366) ]
    poincare_sample_cdf = MakeCdfFromList(poincare_sample, 'poincare')
    
    baker_sample = []
    for i in xrange(366):
        baker_sample.append(max(random.normalvariate(950, 50) for i in xrange(4)))
    baker_cdf = MakeCdfFromList(baker_sample)
    
        
    print poincare_sample_cdf.Mean(),
    print baker_cdf.Mean()
    myplot.Clf()
    myplot.Cdfs([poincare_sample_cdf, baker_cdf])
    pyplot.xlim(600, 1120)
    pyplot.legend(loc=0)
    myplot.SaveFormat('../resources/plots/poincare_vs_baker', 'png')
    
    # t-test
    t_test = stats.ttest_rel(poincare_sample, baker_sample)
    
    print "t-test statistic is %s with a p-value %s" % t_test
    
def main():
    
    compare_poincare_baker()
    
if __name__ == '__main__':
    main()