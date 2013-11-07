'''
Created on 26 Oct 2013

@author: wrightm
'''
import unittest
from bias import BiasPmf
from relay import ReadResults, GetSpeeds
import Pmf
import Cdf
import myplot
from score_example import PercentileRank


class RelayRaceBias(BiasPmf):
    
    def __init__(self, relativePace):
        super(BiasPmf, self).__init__()
        self.__relativePace = relativePace
        
    def __call_(self, value):
        return (value - self.__relativePace)

def getPercentileRank(results, position):
    
    count = 0
    for indx, result in enumerate(results):
        if indx <= position:
            count += 1
        else:
            return 100 - int(100 * (float(count) / float(len(results))))
    return 100 - int(100 * (float(count) / float(len(results))))

def getPercentile(results, percentile):
    index = int((100 - percentile) * float(len(results)-1) / 100.00)
    return results[index]

class RelayRaceTest(unittest.TestCase):


    def testPaceBias(self):
        
        results = ReadResults()
        speeds = GetSpeeds(results)
        relayPmf = Pmf.MakePmfFromList(speeds, 'speeds')
        
        relayRaceBias = RelayRaceBias(7.5)
        relayBiasPmf = Pmf.BiasedPmf(relayRaceBias, relayPmf, 'bias relay pmf')
        
        cdf = Cdf.MakeCdfFromPmf(relayPmf, 'speeds')
        biasCdf = Cdf.MakeCdfFromPmf(relayBiasPmf, 'bias speeds')
        
        #myplot.Cdfs([cdf, biasCdf])
        #myplot.Show()
        pass
        
    def testPercentileRank(self):

        results = ReadResults()
        
        positions = []
        m4049Results = []
        m5059Results = []
        f2039Results = []
        
        for result in results:
            if result[2] == 'M4049':
                m4049Results.append(result)
            if result[2] == 'M5059':
                m5059Results.append(result)
            if result[2] == 'F2039':
                f2039Results.append(result)
            
            if result[0] == '97':
                allen = result    
            positions.append(int(result[0]))
            
        print getPercentileRank(positions, 97)
        print getPercentileRank(m4049Results, 26)
        print getPercentile(m5059Results, 90)
        print getPercentile(f2039Results, 91)
        print allen
        print 'expect to be 36 seconds slower per mile in 10 years'
        print 'if your friend want to beat you she will have to run 7:44 minute miles'
        
if __name__ == "__main__":
    unittest.main()