'''
Created on 6 Mar 2014

@author: wrightm
'''
from chapter5.main.continuous import RenderNormalCdf
from chapter5.main.Cdf import Cdf, MakeCdfFromList
import random
from chapter5.main import myplot
from matplotlib import pyplot

def compare_poincare_baker():

    """
    bread measurements by poincare 365 fitted normal distribution with mean 950g and 50g standard deviation
    """ 

    xs, ps  = RenderNormalCdf(950, 50, 1150, 365)
    normal_cdf_distribution = Cdf(xs, ps, 'baker')
    poincare_sample = [ random.normalvariate(950, 50) for i in xrange(366) ]
    
    poincare_sample_cdf = MakeCdfFromList(poincare_sample, 'poincare')

    myplot.Clf()
    myplot.Cdfs([poincare_sample_cdf, normal_cdf_distribution])
    pyplot.xlim(600, 1120)
    pyplot.legend(loc=0)
    myplot.SaveFormat('../resources/plots/poincare_vs_baker')

def main():
    
    compare_poincare_baker()
    
if __name__ == '__main__':
    main()