'''
Created on 26 Feb 2014

@author: wrightm
'''
from chapter4.main.continuous import MakeNormalCdf, MakeNormalModel,\
    MakeNormalPlot
from chapter4.main import cumulative, relay, rankit

def main():
    
    MakeNormalCdf()
    
    # test the distribution of birth weights for normality
    pool, _, _ = cumulative.MakeTables('../resources')
    
    t = pool.weights
    MakeNormalModel(t)
    
    # Test Rankit of weights
    MakeNormalPlot(t)
    
    # Test Rankit of relay speeds
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    rankit.MakeNormalPlot(speeds,
                          root='../resources/plots/relay_normal',
                          ylabel='Speed (MPH)')
    
    
    
if __name__ == '__main__':
    main()