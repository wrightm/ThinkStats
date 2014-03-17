'''
Created on 6 Mar 2014

@author: wrightm
'''
import random
import math
import scipy.stats

def PairingDancers():
    
    men_heights = [ random.normalvariate(178, math.sqrt(59.4)) for i in xrange(101) ]
    ladies_heights = [ random.normalvariate(163, math.sqrt(52.8)) for i in xrange(101) ]
    
    prob_of_taller_women = []
    count = 0.0
    for i in xrange(1001):
        number_of_taller_women = 0
        for j in xrange(1001):
            count += 1.0
            mens_picks = random.randint(0,100)
            ladies_picks = random.randint(0,100)
            man = men_heights[mens_picks]
            lady = ladies_heights[ladies_picks]
            if lady > man:
                number_of_taller_women += 1
        
        prob_of_taller_women.append(float(number_of_taller_women))


    total = 0.0        
    for prob in prob_of_taller_women:
        total += prob
        
    print total / count
    print scipy.stats.norm.sf(float(178 - 163) / math.sqrt(59.4 + 52.8))
    

def main():
    
    PairingDancers()
    
if __name__ == '__main__':
    main()