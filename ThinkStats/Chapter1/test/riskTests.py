'''
Created on 14 Oct 2013

@author: wrightm
'''
import unittest
import Pmf
import survey


class BinnedPmf(object):
    
    def __init__(self, pmf):
        self.pmf = pmf
        self.earlyPmf = Pmf.Pmf()
        self.onTimePmf = Pmf.Pmf()
        self.latePmf = Pmf.Pmf()
        self.__bin()
        
    def __bin(self):
        
        for weeks, prob in self.pmf.GetDict().iteritems():
            if weeks <= 37:
                self.earlyPmf.Set(weeks, prob)
            elif weeks > 37 and weeks <= 40:
                self.onTimePmf.Set(weeks, prob)
            else:
                self.latePmf.Set(weeks, prob)
                
    def probOfBeingEarly(self):
        return self.earlyPmf.Total()
    
    def probOfBeingOnTime(self):
        return self.onTimePmf.Total()
    
    def probOfBeignLate(self):
        return self.latePmf.Total()
    
    
    
    

class RiskTests(unittest.TestCase):


    def testRelativeRisks(self):
        
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirthsDuration = []
        secondAndGr8LiveBirthsDuration = []
        allLiveBirths = []
        
        for record in table.records:
            if record.outcome == 1:
                allLiveBirths.append(record.prglength)
                if record.birthord == 1:
                    firstLiveBirthsDuration.append(record.prglength)
                elif record.birthord > 1:
                    secondAndGr8LiveBirthsDuration.append(record.prglength)
        
        firstLiveBirthPmf = Pmf.MakePmfFromList(firstLiveBirthsDuration, 'firstLiveBirths')
        otherLiveBirthPmf = Pmf.MakePmfFromList(secondAndGr8LiveBirthsDuration, 'otherLiveBirths')
        allLiveBirthPmf = Pmf.MakePmfFromList(allLiveBirths, 'allLiveBirths')
        
        binnedFirstLiveBirthPmf = BinnedPmf(firstLiveBirthPmf)
        binnedOtherLiveBirthPmf = BinnedPmf(otherLiveBirthPmf)
        #binnedAllLiveBirthPmf = BinnedPmf(allLiveBirthPmf)
        
        relativeRiskEarlyBirths = binnedFirstLiveBirthPmf.probOfBeingEarly() / binnedOtherLiveBirthPmf.probOfBeingEarly()
        relativeRiskOnTimeBirths = binnedFirstLiveBirthPmf.probOfBeingOnTime() / binnedOtherLiveBirthPmf.probOfBeingOnTime()
        relativeRiskLateBirths = binnedFirstLiveBirthPmf.probOfBeignLate() / binnedOtherLiveBirthPmf.probOfBeignLate()
        
        self.assertAlmostEqual(relativeRiskEarlyBirths, 1.08, 2, 'relative risk of early births in first babies is 8% more likely')
        
    def testConditionalProbability(self):
         
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirthsDuration = []
        secondAndGr8LiveBirthsDuration = []
        allLiveBirths = []
        
        for record in table.records:
            if record.outcome == 1:
                allLiveBirths.append(record.prglength)
                if record.birthord == 1:
                    firstLiveBirthsDuration.append(record.prglength)
                elif record.birthord > 1:
                    secondAndGr8LiveBirthsDuration.append(record.prglength)
                    
        self.assertAlmostEquals(probOfBirthPriorToWeek(Pmf.MakePmfFromList(allLiveBirths), 39),0.68, 2, 'probability of births after week 39 should be 0.68') 
        
def probOfBirthPriorToWeek(pmf, allowedWeek):
    
    newPmf = Pmf.Pmf()
    
    for week, prob in pmf.GetDict().iteritems():
        if week < allowedWeek:
            continue
        newPmf.Set(week, prob) 
    newPmf.Normalize()
    
    return newPmf.Prob(allowedWeek)
    
if __name__ == "__main__":
    unittest.main()