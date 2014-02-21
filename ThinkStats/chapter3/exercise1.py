'''
Created on 21 Feb 2014

@author: wrightm
'''
from chapter3.main.class_size import ClassSizes
from chapter3.main import relay, Pmf, myplot
from chapter3.test.relay_soln import BiasPmf

def main():
    
    # Class size
    ClassSizes()

    ## Relay
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    # plot the distribution of actual speeds
    pmf = Pmf.MakePmfFromList(speeds, 'actual speeds')

    myplot.Clf()
    myplot.Hist(pmf)
    myplot.Save(root='../resources/plots/observed_speeds_relay',
                title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')

    # plot the biased distribution seen by the observer
    biased = BiasPmf(pmf, 7.5, name='observed speeds')

    myplot.Clf()
    myplot.Hist(biased)
    myplot.Save(root='../resources/plots/observed_speeds_relay_bias',
                title='PMF of running speed bias',
                xlabel='speed (mph)',
                ylabel='probability')
    
if __name__ == '__main__':
    main()