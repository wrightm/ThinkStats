'''
Created on 25 Oct 2013

@author: wrightm
'''
import unittest
import Pmf
from bias import BiasPmf


class ClassSizeTests(unittest.TestCase):


    def testDeanAverageClassSize(self):
        
        classSizes = {7: 8,
                      12: 8,
                      17: 14,
                      22: 4,
                      27: 6,
                      32: 12,
                      37: 8,
                      42: 3,
                      47: 2}
        
        pmfClassSizes = Pmf.MakePmfFromDict(classSizes, 'pmf of class sizes')
        pmfClassSizes.Normalize()
        self.assertAlmostEqual(pmfClassSizes.Mean(), 23.69, 2, "deans class size mean does not equal 23.69")
        
        
    def testStudentAverageClassSize(self):
        
        classSizes = {7: 8,
                      12: 8,
                      17: 14,
                      22: 4,
                      27: 6,
                      32: 12,
                      37: 8,
                      42: 3,
                      47: 2}
        
        pmfClassSizes = Pmf.MakePmfFromDict(classSizes, 'pmf of class sizes')
        
        pmfStudentView = Pmf.BiasedPmf(BiasPmf(), pmfClassSizes, 'student view')
        self.assertAlmostEqual(pmfStudentView.Mean(), 29.12, 2, "students class size mean does not equal 29.12")


if __name__ == "__main__":
    unittest.main()