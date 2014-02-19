'''
Created on 20 Feb 2014

@author: wrightm
'''
from chapter2.main.descriptive import MakeTables, Summarize, MakeFigures,\
    MakeDiffFigure

def main():
    data_dir = "../resources/"
    pool, firsts, others = MakeTables(data_dir)
    Summarize(pool, firsts, others)
    MakeFigures(firsts, others)
    MakeDiffFigure(firsts, others)

if __name__ == '__main__':
    main()