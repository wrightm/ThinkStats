'''
Created on 19 May 2014

@author: wrightm
'''
from chapter8.main.decay import MakeUniformSuite, Update
from chapter8.main import myplot, thinkstats

def main():
    
    suite = MakeUniformSuite(0.001, 1.5, 1000)
    evidence = [1.5, 2, 3, 4, 5, 12]

    Update(suite, evidence)
    suite.name = 'posterior'

    # plot the posterior distributions
    myplot.Pmf(suite)
    myplot.Config(title='Decay parameter',
                xlabel='Parameter (inverse cm)',
                ylabel='Posterior probability')
    myplot.Save('../resources/plots/decay_')

    print 'Naive parameter estimate:', 1.0 / thinkstats.Mean(evidence)
    print 'Mean of the posterior distribution:', suite.Mean()
    
if __name__ == '__main__':
    main()