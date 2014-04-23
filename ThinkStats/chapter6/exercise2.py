'''
Created on 23 Apr 2014

@author: wrightm
'''
from chapter6.main.continuous import ExpoCdf

def main():
    
    maximum = ExpoCdf(0.01, 20)
    minimum = ExpoCdf(0.01, 1)
    
    prob = maximum - minimum
    
    print "The probability of the exponential distribution to lie within 20 and 1 with a lambda of 0.01 = %s" % prob
    
if __name__ == '__main__':
    main()