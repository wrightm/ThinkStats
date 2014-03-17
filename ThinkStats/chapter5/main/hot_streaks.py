'''
Created on 9 Mar 2014

@author: wrightm
'''
import random
import numpy 

def HotStreak():
    
    sample_size = 1000000.0
    success = 0.0
    for i in xrange(int(sample_size)+1):
        sample = numpy.random.binomial(1,0.5,15)
        same = 0.0
        for item in sample:
            if same == 10:
                continue
            if item == 0:
                same += 1.0
            else:
                same = 0.0
        
        if same >= 10.0:        
            success += 1.0
            print sample
        
    print success, (success / sample_size), (success / sample_size) * 100 
    
    

def main():

    HotStreak()
    
if __name__ == '__main__':
    main()