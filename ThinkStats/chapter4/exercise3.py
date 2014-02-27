'''
Created on 27 Feb 2014

@author: wrightm
'''
from chapter4.main.continuous import RandomExpo, RandomWeibull, RandomPareto
from matplotlib import pyplot
from chapter4.main import myplot

def main():
    
    n = 1000
    
    expo_sample = [RandomExpo(2) for x in xrange(n)]
    
    expo_xs, expo_ps = zip(*sorted(expo_sample))
    
    pyplot.clf()
    pyplot.plot(expo_xs, expo_ps, linewidth=2)
    myplot.Save('../resources/plots/random_numbers_expo',
                title='Expo Random CDF',
                xlabel='x',
                ylabel='CDF',
                legend=False)
    
    weibull_sample = [RandomWeibull(2, 1) for x in xrange(n)]
    
    weibull_xs, weibull_ps = zip(*sorted(weibull_sample))
    
    pyplot.clf()
    pyplot.plot(weibull_xs, weibull_ps, linewidth=2)
    myplot.Save('../resources/plots/random_numbers_weibull',
                title='Weibull Random CDF',
                xlabel='x',
                ylabel='CDF',
                legend=False)
    
    pareto_sample = [RandomPareto(2, 10) for x in xrange(n)]
    
    pareto_xs, pareto_ps = zip(*sorted(pareto_sample))
    
    pyplot.clf()
    pyplot.plot(pareto_xs, pareto_ps, linewidth=2)
    myplot.Save('../resources/plots/random_numbers_pareto',
                title='Pareto Random CDF',
                xlabel='x',
                ylabel='CDF',
                legend=False)
    
if __name__ == '__main__':
    main()