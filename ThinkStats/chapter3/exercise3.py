'''
Created on 23 Feb 2014

@author: wrightm
'''
from chapter3.main import myplot, Cdf, relay, Pmf
from chapter3.test.relay_soln import BiasPmf

def main():
    
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    
    # plot the distribution of actual speeds
    pmf = Pmf.MakePmfFromList(speeds, 'actual speeds')
    
    # plot the biased distribution seen by the observer
    biased = BiasPmf(pmf, 7.5, name='observed speeds')

    cdf = Cdf.MakeCdfFromPmf(biased)

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='../resources/plots/observed_speeds_cdf_relay',
                title='CDF of running speed',
                xlabel='speed (mph)',
                ylabel='cumulative probability')

if __name__ == '__main__':
    main()