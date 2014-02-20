'''
Created on 20 Feb 2014

@author: wrightm
'''
from chapter2.main.risk import ComputeRelativeRisk
from chapter2.main.descriptive import MakeTables

def main():
    
    data_dir = "../resources/"
    pool, firsts, others = MakeTables(data_dir)
    ComputeRelativeRisk(firsts.pmf, others.pmf)
    
if __name__ == '__main__':
    main()