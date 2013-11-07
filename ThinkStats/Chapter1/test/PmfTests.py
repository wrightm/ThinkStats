'''
Created on 13 Oct 2013

@author: wrightm
'''
import unittest
import Pmf

class PmfTests(unittest.TestCase):


    def testMode(self):
        hist = Pmf.MakeHistFromList([1,2,3,3,4,5,2,2,3,3,5,5,5], 'test')
        modes = Pmf.Mode(hist)
        
        self.assertEqual(modes, [3,5], 'modes does not equal [3,5]')

    def testAllMode(self):
        hist = Pmf.MakeHistFromList([1,2,3,3,4,5,2,2,3,3,5,5,5], 'test')
        allmodes = Pmf.AllMode(hist)
        
        self.assertEqual(allmodes, [ (3, 4), (5, 4), (2, 3), (1, 1), (4, 1) ])
        
    def testPmfMean(self):
        
        pmf = Pmf.MakePmfFromList([1,2,3,3,4,5,2,2,3,3,5,5,5], 'test')
        
        mean = 0.0
        for value, prob in pmf.GetDict().iteritems():
            mean += prob * value
        
        self.assertAlmostEqual(mean, pmf.Mean(), 2, 'mean does not equal 3.307')
        
    def testPmfVariance(self):
        
        pmf = Pmf.MakePmfFromList([1,2,3,3,4,5,2,2,3,3,5,5,5], 'test')
        
        mean = 0.0
        for value, prob in pmf.GetDict().iteritems():
            mean += prob * value
        
        var = 0.0
        for value, prob in pmf.GetDict().iteritems():
            var += prob * (pow((value-mean),2))
            
        self.assertEqual(var, pmf.Var(), 'var does not equal pmf.Var')

if __name__ == "__main__":
    unittest.main()