'''
Created on 13 May 2014

@author: wrightm
'''
from chapter8.main import myplot
from matplotlib import pyplot
from chapter8.main.estimate import EstimateParameter, MakeUniformSuite
import random

def main():

    # make a uniform prior
    param = 1.2
    prior = MakeUniformSuite(0.5, 1.5, 1000)

    # try out the sample in the book
    t = []
    sample = [2.68, 0.20, 1.15, 0.79, 2.72, 4.27]
    name = 'post%d' % len(sample)
    posterior = EstimateParameter(prior, sample, name)
    value, prob = posterior.MostLikeli()
    print "lambda estimator sample in the book: %s with prob %s" % (value, prob) 
    t.append(posterior)

    # try out a range of sample sizes
    for n in [10, 20, 40, 500]:

        # generate a sample
        sample = [round(random.expovariate(param),2) for _ in range(n)]
        name = 'post%d' % n

        # compute the posterior
        posterior = EstimateParameter(prior, sample, name)
        value, prob = posterior.MostLikeli()
        print "lambda estimator sample with sample size %s and param %s : %s with prob %s" % (n, param, value, prob)
        t.append(posterior)

    # plot the posterior distributions
    for i, posterior in enumerate(t):
        myplot.Clf()
        myplot.Pmf(posterior)
        pyplot.legend()
        pyplot.xlabel('lambda')
        pyplot.ylabel('Posterior probability')
        myplot.Save(root='../resources/plots/posteriors_%s' % posterior.name)
    
if __name__ == '__main__':
    main()