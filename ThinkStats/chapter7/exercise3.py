'''
Created on 12 May 2014

@author: wrightm
'''
from chapter7.main import descriptive
from chapter7.main.chi import Test

def main():
    # get the data
    pool, firsts, others = descriptive.MakeTables('../resources')
    Test(pool, firsts, others, num_trials=1000)
    
if __name__ == '__main__':
    main()