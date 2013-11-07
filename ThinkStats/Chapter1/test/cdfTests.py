'''
Created on 27 Oct 2013

@author: wrightm
'''
import unittest


def CdfValue(items, chosenItem):
    count = 0
    for indx, item in enumerate(items):
        if item <= chosenItem:
            count += 1
    return float(count) / float(len(items))
    
def calculateAllCDFValues(items):
    runsum = 0
    values = []
    sum  = []
    for value, freq in sorted(items):
        runsum += freq
        values.append(value)
        sum.append(runsum)
    
    probs = [value/runsum for value in sum]
    return values, probs
    
class Test(unittest.TestCase):


    def testCdf(self):

        items = range(100)
        self.assertEqual(CdfValue(items,90), 0.91)

if __name__ == "__main__":
    unittest.main()