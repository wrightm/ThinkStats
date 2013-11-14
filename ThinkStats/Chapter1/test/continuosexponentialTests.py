'''
Created on 11 Nov 2013

@author: wrightm
'''
import unittest
import random
from matplotlib import pyplot
import math
import myplot
import Pmf


class ContinuosExponentialTests(unittest.TestCase):


    def testExponentialDistrobution(self):
        
        expoDistribution = [ 1 - random.expovariate(32.6) for i in range(44) ]
        fig = pyplot.figure()
        #ax = fig.add_subplot(1,1,1)
        #ax.plot(expoDistribution)
        #ax.set_yscale('log')
        #pyplot.show()
        
    def testParetoDistribution(self):
        
        def paretoVariate(alpha, x_m):
            
            return math.pow(x_m, alpha) * random.paretovariate(alpha)
        
        paretoDistribution = [ paretoVariate(1.7, 100) for i in range(600) ]
        pmf = Pmf.MakePmfFromList(paretoDistribution,'population height')
        myplot.Pmf(pmf)
        #myplot.Show()
        #fig = pyplot.figure()
        #ax = fig.add_subplot(1,1,1)
        #ax.plot(paretoDistribution)
        #pyplot.show()
        
    def testTextCounter(self):
        
        with open('/Volumes/MichaelWright1/Dropbox/Projects/ThinkStats/ThinkStats/resources/big.txt') as f:
            numberOfWords = {}
            for line in f:
                if line:
                     for word in line.strip().strip('\n').strip('\t').strip('v').strip('r').split(' '):
                         if word:
                             parsedWord = word.strip(',').strip('(').strip(')').strip('.').strip(':').strip("")
                             if parsedWord:
                                 numberOfWords[parsedWord] = numberOfWords.get(parsedWord, 0) + 1
            
            moreFrequentWords = {}
            for word, freq in numberOfWords.iteritems():
                if freq > 1:
                    moreFrequentWords[word] = freq
                    
            xs, fs = zip(*moreFrequentWords.items())        
            #pyplot.bar(range(len(fs)), fs, align='center')
            #pyplot.xticks(range(len(xs)), xs, size='small')
            #pyplot.show()
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()