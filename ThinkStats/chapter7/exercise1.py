'''
Created on 5 May 2014

@author: wrightm
'''
import random
from chapter7.main import cumulative, thinkstats
from chapter7.main.hypothesis import RunTest

def main():
    
    random.seed(1)

    # get the data
    pool, firsts, others = cumulative.MakeTables('../resources/')
    mean_var_pool = thinkstats.MeanVar(pool.lengths)
    mean_var_firsts = thinkstats.MeanVar(firsts.lengths)
    mean_var_others = thinkstats.MeanVar(others.lengths)
    
    print '(Mean, Var) of pooled data', mean_var_pool
    print '(Mean, Var) of firsts data', mean_var_firsts
    print '(Mean, Var) of others data', mean_var_others
    
    # run the test
    RunTest('../resources/plots/length', 
            pool.lengths,
            firsts.lengths, 
            others.lengths, 
            iters=1000,
            trim=False,
            partition=True)
    
if __name__ == '__main__':
    main()