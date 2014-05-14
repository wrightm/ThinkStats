'''
Created on 13 May 2014

@author: wrightm
'''
from chapter7.main import descriptive
from chapter7.main.chi import TestProbEarly
from chapter7.main.hypothesis_analytic import Test

def main():
    # get the data
    pool, firsts, others = descriptive.MakeTables('../resources')
    TestProbEarly(pool, firsts, others, num_trials=1000)
    
    print 'Test: Normal Approximation'
    
    # run the test
    Test(firsts.lengths, 
         others.lengths, 
         pool.lengths,
         iters=1000)
if __name__ == '__main__':
    main()