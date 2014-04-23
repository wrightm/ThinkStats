'''
Created on 23 Apr 2014

@author: wrightm
'''
from chapter6.main import erf

import math

def main():
    
    male_185_4 = erf.NormalCdf(185.4, 178, math.sqrt(59.4))
    male_177_8 = erf.NormalCdf(177.8, 178, math.sqrt(59.4))
    
    prob_of_usa_male_blueman = male_185_4 - male_177_8
    
    print "The percentage of the U.S. male population in the Blue Man Group Range = %s" % prob_of_usa_male_blueman
    
if __name__ == '__main__':
    main()