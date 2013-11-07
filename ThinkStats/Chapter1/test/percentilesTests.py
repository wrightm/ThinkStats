'''
Created on 27 Oct 2013

@author: wrightm
'''
import unittest


def percentileRank(scores, yourScore):
    
    count = 0
    for score in scores:
        if score <= yourScore:
            count +=1
    
    rank = 100.00 * (float(count)/float(len(scores)))
    return rank

def percentile(scores, percentile):
    
    scores.sort()
    for score in scores:
        percentilerank = percentileRank(scores, score)
        if percentilerank >= percentile:
            return score

def percentile2(scores, percentile):
    
    scores.sort()
    index = int(percentile * (len(scores)-1) / 100)
    return scores[index] 
    
class PercetileTest(unittest.TestCase):


    def testStandardAlgorithmPercentile(self):
        
        scores = range(100)
        nintieth = percentile(scores, 90)
        self.assertEqual(nintieth, 89)
        
    def testMoreEfficientIndexPercentileAlgorithm(self):
        
        scores = range(100)
        nintieth = percentile2(scores, 90)
        self.assertEqual(nintieth, 89)
        
        

if __name__ == "__main__":
    unittest.main()