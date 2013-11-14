'''
Created on 14 Nov 2013

@author: wrightm
'''
import unittest
import numpy
import thinkstats
import math
from matplotlib import pyplot
from scipy.special import erf
from cumulative import MakeTables
from Cdf import MakeCdfFromList, Cdf
import myplot
from continuous import RenderNormalCdf

def normCdf(maximum, mu, stdev):
            
    normCdfs = []
    sqrt2 = math.sqrt(2)
    for item in xrange(int(maximum+1)):
        prob = ( 1 + erf( score(item, mu, stdev) / sqrt2 ) ) * (1.0/2.0)
        normCdfs.append(prob)
    return normCdfs
        
def score(item, mu, sigma):
            
    return float(item - mu) / sigma
        
class NormalDistributionTest(unittest.TestCase):


    def testNormalDistributionTest(self):
        
        def normCdf(sample):
            
            normCdfs = []
            mu = thinkstats.Mean(sample)
            stdev = math.sqrt(thinkstats.Var(sample, mu))
            sqrt2 = math.sqrt(2)
            for item in sample:
                normCdfs.append(( 1 + erf( score(item, 5.0, 1) / sqrt2 ) ) * (1.0/2.0))
            return normCdfs
        
        def score(item, mu, sigma):
            
            return item - mu / sigma
        
        sample = numpy.linspace(0, 10, 100)
        normcdf = normCdf(sample)
        pyplot.plot(sample, normcdf)
        pyplot.savefig('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources/plots/normalCdf.jpg', format='jpg')

    def testBirthWeights(self):

        pool, firsts, others = MakeTables('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources')
        
        firstsCDF = MakeCdfFromList(firsts.weights, 'first born')
        muFirstsCDF = firstsCDF.Mean()
        stdFirstsCDF = math.sqrt(firstsCDF.Var())
        firstNormalCDFProbs = normCdf(max(firsts.weights), muFirstsCDF, stdFirstsCDF)
        firstNormalCDF = Cdf(range(max(firsts.weights)+1), firstNormalCDFProbs, 'norm first')
        
        othersCDF = MakeCdfFromList(others.weights, 'others born')
        muOthersCDF = othersCDF.Mean()
        stdOthersCDF = math.sqrt(othersCDF.Var())
        othersNormalCDFProbs = normCdf(max(others.weights), muOthersCDF, stdOthersCDF)
        othersNormalCDF = Cdf(range(max(others.weights)+1), othersNormalCDFProbs, 'norm others')
        
        poolCDF = MakeCdfFromList(pool.weights, 'pool born')
        mupoolCDF = poolCDF.Mean()
        stdpoolCDF = math.sqrt(poolCDF.Var())
        poolNormalCDFProbs = normCdf(max(pool.weights), mupoolCDF, stdpoolCDF)
        poolNormalCDF = Cdf(range(max(pool.weights)+1), poolNormalCDFProbs, 'norm pool')
        
        myplot.Cdfs([poolCDF, poolNormalCDF])
        myplot.Show()
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()