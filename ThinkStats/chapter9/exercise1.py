'''
Created on 20 May 2014

@author: wrightm
'''
from chapter9.main.brfss_scatter import Respondents
from matplotlib import pyplot
from chapter9.main import correlation, myplot
from chapter9.main.brfss_corr import Log
import math
from chapter9.main.Pmf import MakePmfFromList

def main():
    
    resp = Respondents()
    resp.ReadRecords('../resources', n=10000)

    heights, weights = resp.GetHeightWeight()
    pyplot.clf()
    resp.ScatterPlot('../resources/plots/scatter1', heights, weights)

    pyplot.clf()
    resp.HexBin('../resources/plots/scatter4', heights, weights)
 
    print 'Number of records:', len(resp.records)

    heights, weights = resp.GetHeightWeight()
    pearson = correlation.Corr(heights, weights)
    print 'Pearson correlation (weights):', pearson

    log_weights = Log(weights)
    pearson = correlation.Corr(heights, log_weights)
    print 'Pearson correlation (log weights):', pearson

    spearman = correlation.SpearmanCorr(heights, weights)
    print 'Spearman correlation (weights):', spearman

    inter, slope = correlation.LeastSquares(heights, log_weights)
    print 'Least squares inter, slope (log weights):', inter, slope

    res = correlation.Residuals(heights, log_weights, inter, slope)
    R2 = correlation.CoefDetermination(log_weights, res)
    print 'Coefficient of determination:', R2
    print 'sqrt(R^2):', math.sqrt(R2)
    
    heights_pmf = MakePmfFromList(heights, name='heights')
    weights_pmf = MakePmfFromList(weights, name='weights')
    
    myplot.Clf()
    myplot.Pmf(heights_pmf)
    myplot.Save('../resources/plots/heights_pmfs')
    
    myplot.Clf()
    myplot.Pmf(weights_pmf)
    myplot.Save('../resources/plots/weights_pmfs')
    
    
if __name__ == '__main__':
    main()