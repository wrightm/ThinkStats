'''
Created on 7 May 2014

@author: wrightm
'''
from chapter7.main import cumulative, thinkstats
from chapter7.main.hypothesis import RunTest
import math

def main():
    
    # get the data
    pool, firsts, others = cumulative.MakeTables('../resources/')
    mean_var_pool = thinkstats.MeanVar(pool.weights)
    mean_var_firsts = thinkstats.MeanVar(firsts.weights)
    mean_var_others = thinkstats.MeanVar(others.weights)
    
    print '(Mean, Var) of pooled data', (mean_var_pool[0], math.sqrt(mean_var_pool[1]))
    print '(Mean, Var) of firsts data', (mean_var_firsts[0], math.sqrt(mean_var_firsts[1]))
    print '(Mean, Var) of others data', (mean_var_others[0], math.sqrt(mean_var_others[1]))
    
    # run the test
    RunTest('../resources/plots/weight', 
            pool.weights,
            firsts.weights, 
            others.weights, 
            iters=1000,
            trim=False,
            partition=True)
   

if __name__ == '__main__':
    main()