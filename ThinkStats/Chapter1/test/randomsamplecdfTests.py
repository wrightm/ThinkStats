'''
Created on 28 Oct 2013

@author: wrightm
'''
import unittest
import random
import survey
import Cdf
import myplot
import Pmf


def Sample(cdf, sampleSize):
    sample = []
    for i in range(sampleSize):
        sample.append(cdf.Value(random.random()))
    return sample
    
    
class RandomSampleCdfTest(unittest.TestCase):


    def testBirthWeights(self):
        
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirthsWeights = []
        secondAndGr8LiveBirthsWeights = []
         
        for record in table.records:
            if record.birthwgt_lb != 'NA' and record.birthwgt_lb <=20:
                if record.birthord == 1:
                    if record.outcome == 1:
                        firstLiveBirthsWeights.append(record.birthwgt_lb)
                elif record.birthord > 1:
                    if record.outcome == 1:
                        secondAndGr8LiveBirthsWeights.append(record.birthwgt_lb)
        
        first = Cdf.MakeCdfFromList(firstLiveBirthsWeights, 'first births')
        other = Cdf.MakeCdfFromList(secondAndGr8LiveBirthsWeights, 'other births')
        
        sample = Sample(first, 1000)
        generated = Cdf.MakeCdfFromList(sample, 'generated')
        
        
    def testUniformDistribution(self):
        
        values = [] 
        
        for i in range(1000):
            values.append(random.random())
        
        pmf = Pmf.MakeHistFromList(values, 'uniform pmf')
        cdf = Cdf.MakeCdfFromList(values, 'uniform cdf')
        
        myplot.Pmf(pmf)
        myplot.Cdf(cdf)
        
        myplot.Show()
        
        
if __name__ == "__main__":
    unittest.main()