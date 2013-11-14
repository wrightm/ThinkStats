'''
Created on 14 Nov 2013

@author: wrightm
'''
import unittest
import brfss
import brfss_figs

class BrfssTest(unittest.TestCase):


    def testBrfss(self):

        respondents = brfss.Respondents()
        respondents.ReadRecords('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources')
        
        respondents.SummarizeWeight()
        
    def testBrfssPlot(self):
        
        resp = brfss_figs.Respondents()
        resp.ReadRecords('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources')
        resp.MakeFigures()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()