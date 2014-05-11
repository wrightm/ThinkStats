"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import Cdf
import cumulative
import math
import myplot
import random
import thinkstats
import matplotlib.pyplot as pyplot


def RunTest(root,
            pool,
            actual1,
            actual2, 
            iters=1000,
            trim=False,
            partition=False):
    """Computes the distributions of delta under H0 and HA.
    
    Args:
        root: string filename root for the plots        
        pool: sequence of values from the pooled distribution
        actual1: sequence of values in group 1
        actual2: sequence of values in group 2
        iters: how many resamples
        trim: whether to trim the sequences
        partition: whether to cross-validate by partitioning the data
    """
    if trim:
        pool.sort()
        actual1.sort()
        actual2.sort()
        pool = thinkstats.Trim(pool)
        actual1 = thinkstats.Trim(actual1)
        actual2 = thinkstats.Trim(actual2)

    if partition:
        n = len(actual1)
        m = len(actual2)
        actual1, model1 = Partition(actual1, n/2)
        actual2, model2 = Partition(actual2, m/2)
        pool = model1 + model2
    else:
        model1 = actual1
        model2 = actual2

    # P(E|H0)
    peh0, peh0_plus_sigma, peh0_minus_sigma  = Test(root + '_deltas_cdf',
                                                    actual1, actual2, pool, pool,
                                                    iters, plot=True)

    # P(E|Ha)
    peha, peha_plus_sigma, peha_minus_sigma = Test(root + '_deltas_ha_cdf',
                                                   actual1, actual2, model1, model2)

    prior = 0.5
    # Median 
    pe = prior*peha + (1-prior)*peh0
    if pe <= 0.0:
        posterior = 1.00
    else:
        posterior = prior*peha / pe
    # + Sigma
    pe_plus_sigma = prior*peha_plus_sigma + (1-prior)*peh0_plus_sigma
    if pe_plus_sigma <= 0.0:
        posterior_plus_sigma = 1.00
    else:
        posterior_plus_sigma = prior*peha_plus_sigma / pe_plus_sigma
    # - Sigma
    pe_minus_sigma = prior*peha_minus_sigma + (1-prior)*peh0_minus_sigma
    if pe_minus_sigma <= 0.0:
        posterior_minus_sigma = 1.00
    else:
        posterior_minus_sigma = prior*peha_minus_sigma / pe_minus_sigma
    
    # Print Info
    print 'Prior =', prior
    print 'P(E|H0): %s + Sigma %s - Sigma %s' % (peh0,peh0_plus_sigma,peh0_minus_sigma)
    print 'P(E|Ha): %s + Sigma %s - Sigma %s' % (peha,peha_plus_sigma,peha_minus_sigma)
    print 'P(E): %s + Sigma %s - Sigma %s' % (pe,pe_plus_sigma,pe_minus_sigma)
    print 'Posterior: %s + Sigma %s - Sigma %s' % (posterior, posterior_plus_sigma, posterior_minus_sigma)
    
    # Median
    if not peh0:
        print 'Likelihood Ratio = P(E|Ha) / P(E|H0) = ', 1.0
    else:
        print 'Likelihood Ratio = P(E|Ha) / P(E|H0) = ', peha / peh0

    # + Sigma
    if not peh0_plus_sigma:
        print 'Likelihood Ratio + Sigma = P(E|Ha) / P(E|H0) = ', 1.0
    else:
        print 'Likelihood Ratio + Sigma = P(E|Ha) / P(E|H0) = ', peha_plus_sigma / peh0_plus_sigma

    # - Sigma
    if not peh0_minus_sigma:
        print 'Likelihood Ratio - Sigma = P(E|Ha) / P(E|H0) = ', 1.0
    else:
        print 'Likelihood Ratio - Sigma = P(E|Ha) / P(E|H0) = ', peha_minus_sigma / peh0_minus_sigma

    
def Test(root, actual1, actual2, model1, model2, iters=1000, plot=False):
    """Estimates p-values based on differences in the mean.
    
    Args:
        root: string filename base for plots        
        actual1:
        actual2: sequences of observed values for groups 1 and 2
        model1: 
        model2: sequences of values from the hypothetical distributions
        iters: how many resamples
        plot: whether to plot the distribution of differences in the mean
    """
    n = len(actual1)
    m = len(actual2)
    
    mu1, mu2, delta = DifferenceInMean(actual1, actual2)
    delta = abs(delta)
    var1 = thinkstats.Var(actual1, mu1)
    var2 = thinkstats.Var(actual2, mu2)
    delta_std_dev = 0.0
    if n > 0 and m > 0:
        delta_std_dev = math.fabs(math.sqrt((var1/n) + (var2/m)))

    cdf, pvalue, pvalue_std_dev_plus, pvalue_std_dev_minus = PValue(model1, model2, n, m, delta, delta_std_dev, iters)
    print 'n:', n
    print 'm:', m
    print 'mu1', mu1
    print 'mu2', mu2
    print 'delta %s +/- %s' % (delta, delta_std_dev)
    print 'p-value', pvalue
    print 'p-value %s + 1 sigma %s' % (pvalue, pvalue_std_dev_plus)
    print 'p-value %s - 1 sigma %s' % (pvalue, pvalue_std_dev_minus)
    

    if plot:
        PlotCdf(root, cdf, delta)
        
    return pvalue, pvalue_std_dev_plus, pvalue_std_dev_minus
    
    
def DifferenceInMean(actual1, actual2):
    """Computes the difference in mean between two groups.

    Args:
        actual1: sequence of float
        actual2: sequence of float

    Returns:
        tuple of (mu1, mu2, mu1-mu2)
    """
    mu1 = thinkstats.Mean(actual1)
    mu2 = thinkstats.Mean(actual2)
    delta = mu1 - mu2
    return mu1, mu2, delta


def PValue(model1, model2, n, m, delta, delta_std_dev, iters=1000):
    """Computes the distribution of deltas with the model distributions.

    And the p-value of the observed delta.

    Args:
        model1: 
        model2: sequences of values from the hypothetical distributions
        n: sample size from model1
        m: sample size from model2
        delta: the observed difference in the means
        iters: how many samples to generate
    """
    deltas = [Resample(model1, model2, n, m) for i in range(iters)]
    mean_var = thinkstats.MeanVar(deltas)
    print '(Mean, Var) of resampled deltas', mean_var

    cdf = Cdf.MakeCdfFromList(deltas)

    delta_plus_sigma =  delta + delta_std_dev
    delta_minus_sigma =  delta - delta_std_dev
    # compute the two tail probabilities
    left = cdf.Prob(-delta)
    right = 1.0 - cdf.Prob(delta)

    left_plus_sigma = cdf.Prob(-delta_plus_sigma)
    right_plus_sigma = 1.0 - cdf.Prob(delta_plus_sigma)
    
    left_minus_sigma = cdf.Prob(-delta_minus_sigma)
    right_minus_sigma = 1.0 - cdf.Prob(delta_minus_sigma)
    
    pvalue = left + right
    print 'Tails (left, right, total):', left, right, left+right
        
    pvalue_minus_sigma = left_minus_sigma + right_minus_sigma 
    print '- Sigma Tails (left, right, total):', left_minus_sigma, right_minus_sigma, left_minus_sigma+right_minus_sigma
    pvalue_plus_sigms = left_plus_sigma + right_plus_sigma
    print '+ Sigma Tails (left, right, total):', left_plus_sigma, right_plus_sigma, left_plus_sigma+right_plus_sigma
    
    return cdf, pvalue, pvalue_minus_sigma, pvalue_plus_sigms

def PlotCdf(root, cdf, delta):
    """Draws a Cdf with vertical lines at the observed delta.

    Args:
       root: string used to generate filenames
       cdf: Cdf object
       delta: float observed difference in means    
    """
    pyplot.clf()
    def VertLine(x):
        """Draws a vertical line at x."""
        xs = [x, x]
        ys = [0, 1]
        pyplot.plot(xs, ys, linewidth=2, color='0.7')
        
    VertLine(-delta)
    VertLine(delta)

    xs, ys = cdf.Render()    
    pyplot.subplots_adjust(bottom=0.11)
    pyplot.plot(xs, ys, linewidth=2, color='blue')
    
    myplot.Save(root,
                title='Resampled differences',
                xlabel='difference in means (weeks)',
                ylabel='CDF(x)',
                legend=False) 
    

def Resample(t1, t2, n, m):
    """Draws samples and computes the difference in mean.
    
    Args:
        t1: sequence of values
        t2: sequence of values
        
        n: size of the sample to draw from t1
        m: size of the sample to draw from t2
    """
    
    sample1 = SampleWithReplacement(t1, n)
    sample2 = SampleWithReplacement(t2, m)
    mu1, mu2, delta = DifferenceInMean(sample1, sample2)
    return delta


def Partition(t, n):
    """Splits a sequence into two random partitions.
    
    Side effect: shuffles t
    
    Args:
        t: sequence of values
        n: size of the first partition

    Returns:
        two lists of values
    """
    random.shuffle(t)
    return t[:n], t[n:]


def SampleWithReplacement(t, n):
    """Generates a sample with replacement.
    
    Args:
        t: sequence of values
        n: size of the sample
        
    Returns:
        list of values
    """    
    return [random.choice(t) for i in range(n)]


def SampleWithoutReplacement(t, n):
    """Generates a sample without replacement.
    
    Args:
        t: sequence of values
        
        n: size of the sample
        
    Returns:
        list of values
    """    
    return random.sample(t, n)
 
 
def main():
    random.seed(1)

    # get the data
    pool, firsts, others = cumulative.MakeTables()
    mean_var = thinkstats.MeanVar(pool.lengths)
    print '(Mean, Var) of pooled data', mean_var
    
    # run the test
    RunTest('../resources/plots/length', 
            pool.lengths,
            firsts.lengths, 
            others.lengths, 
            iters=1000,
            trim=False,
            partition=False)


if __name__ == "__main__":
    main()
