'''
Created on 29 Sep 2013

@author: wrightm
'''
import unittest
import survey
import thinkstats

class FirstTests(unittest.TestCase):

    def testNumberOfPregnancies(self):
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        self.assertEquals(len(table.records), 13593, "Number of pregnancies does not equal 13593")
        
    def testNumberOfLiveBirths(self):
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        liveBirths = 0 
        for record in table.records:
            if record.outcome == 1:
                liveBirths+=1
                    
        self.assertEquals(liveBirths, 9148, "Number of live births does not equals 9148")
    
    def testNumberOfLiveBirthsFor1stBabiesANdOtherBabies(self):
        
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirths = 0
        secondAndGr8LiveBirths = 0 
        for record in table.records:
            if record.birthord == 1:
                if record.outcome == 1:
                    firstLiveBirths+=1
            elif record.birthord > 1:
                if record.outcome == 1:
                    secondAndGr8LiveBirths+=1    

        self.assertEquals(firstLiveBirths, 4413, "Number of first baby live births does not equal 4413")
        self.assertEquals(secondAndGr8LiveBirths, 4735, "Number of second and more live births does not equal 4735")
        
    def testAverageLengthOfPregnancy(self):
        
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirths = 0
        firstLiveBirthsDuration = 0.0
        secondAndGr8LiveBirths = 0
        secondAndGr8LiveBirthsDuration = 0.0
         
        for record in table.records:
            if record.birthord == 1:
                if record.outcome == 1:
                    firstLiveBirths +=1
                    firstLiveBirthsDuration += record.prglength
            elif record.birthord > 1:
                if record.outcome == 1:
                    secondAndGr8LiveBirths+=1
                    secondAndGr8LiveBirthsDuration += record.prglength
                    
        arithmeticMeanFirstBirthDuration = firstLiveBirthsDuration / firstLiveBirths
        arithmeticMeanSecondAndGreaterBirthDuration = secondAndGr8LiveBirthsDuration / secondAndGr8LiveBirths
        
        self.assertAlmostEquals(arithmeticMeanFirstBirthDuration, 38.60, 2, "Arithmetic Mean of first born pregnancy duration does not equal 38.60")
        self.assertAlmostEquals(arithmeticMeanSecondAndGreaterBirthDuration, 38.52, 2, "Arithmetic Mean of second/greater born pregnancy duration does not equal 38.52")

    
    def testAverageAndVarianceOfTwoPregnancyGroups(self):
        
        table = survey.Pregnancies()
        table.ReadRecords("/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources")
        firstLiveBirthsDuration = []
        secondAndGr8LiveBirthsDuration = []
         
        for record in table.records:
            if record.birthord == 1:
                if record.outcome == 1:
                    firstLiveBirthsDuration.append(record.prglength)
            elif record.birthord > 1:
                if record.outcome == 1:
                    secondAndGr8LiveBirthsDuration.append(record.prglength)

        arithmeticMeanFirstBirthDuration = thinkstats.Mean(firstLiveBirthsDuration)
        arithmeticVarianceFirstBirthDuration = thinkstats.Var(firstLiveBirthsDuration)
        
        arithmeticMeanSecondAndGreaterBirthDuration = thinkstats.Mean(secondAndGr8LiveBirthsDuration)
        arithmeticVarianceSecondAndGreaterBirthDuration = thinkstats.Var(secondAndGr8LiveBirthsDuration)
        
        self.assertAlmostEquals(arithmeticMeanFirstBirthDuration, 38.60, 2, "Arithmetic Mean of first born pregnancy duration does not equal 38.60")
        self.assertAlmostEquals(arithmeticVarianceFirstBirthDuration, 7.79, 2, "Arithmetic Variance of first born pregnancy duration does not equal 7.79")
        
        self.assertAlmostEquals(arithmeticMeanSecondAndGreaterBirthDuration, 38.52, 2, "Arithmetic Mean of second/greater born pregnancy duration does not equal 38.52")
        self.assertAlmostEquals(arithmeticVarianceSecondAndGreaterBirthDuration, 6.84, 2, "Arithmetic Variance of second/greater born pregnancy duration does not equal 6.84")
        

