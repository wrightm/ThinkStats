"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math
import sys

import irs

import Pmf
import Cdf
from chapter6.main import myplot


def PmfMean(pmf):
    total = 0.0
    for val, p in pmf.Items():
        total += p * val
    return total

        
def PmfMoment(pmf, mean=None, exponent=2):
    if mean is None:
        mean = PmfMean(pmf)

    total = 0.0
    for val, p in pmf.Items():
        total += p * (val - mean)**exponent
    return total


def RelativeMeanDifference(pmf, mean=None):
    if mean is None:
        mean = PmfMean(pmf)

    diff = Pmf.Pmf()
    for v1, p1 in pmf.Items():
        for v2, p2 in pmf.Items():
            diff.Incr(abs(v1-v2), p1*p2)

    print PmfMean(diff), mean

    return PmfMean(diff) / mean


def SummarizeData(pmf, cdf):

    mean = PmfMean(pmf)
    print 'mean:', mean

    median = cdf.Percentile(50)
    print 'median:', median

    fraction_below_mean = cdf.Prob(mean)
    print 'fraction below mean:', fraction_below_mean

    m2 = PmfMoment(pmf, mean, 2)
    m3 = PmfMoment(pmf, mean, 3)

    sigma = math.sqrt(m2)
    print 'sigma:', sigma

    g1 = m3 / m2**(3.0/2.0)
    print 'skewness:', g1

    gp = 3 * (mean - median) / sigma
    print 'Pearsons skewness:', gp

    gini = RelativeMeanDifference(pmf) / 2
    print 'gini', gini

def main(script, *args):
    
    data = irs.ReadIncomeFile()
    hist, pmf, cdf = irs.MakeIncomeDist(data)
    SummarizeData(pmf, cdf)

    myplot.Clf()
    myplot.Pmf(pmf, 'irs incomes')
    myplot.Save('../resources/plots/irs_incomes_pmf')

    myplot.Clf()
    myplot.Cdf(cdf, 'irs incomes')
    myplot.Save('../resources/plots/irs_incomes_cdf')
    
if __name__ == "__main__":
    main(*sys.argv)
