'''
Created on 20 Feb 2014

@author: wrightm
'''
from chapter2.main.descriptive import MakeTables
from chapter2.main.conditional import RelativeRisk, MakeFigure

def main():
    
    data_dir = "../resources/"
    pool, firsts, others = MakeTables(data_dir)
    RelativeRisk(firsts, others)
    MakeFigure(firsts, others)

if __name__ == '__main__':
    main()