'''
Created on 21 Feb 2014

@author: wrightm
'''
from chapter3.main.score_example import Percentile, scores
def main():
    
    print 'prank','score'
    for percentile_rank in [0, 20, 25, 40, 50, 60, 75, 80, 100]:
        print percentile_rank, 
        print Percentile(scores, percentile_rank),
        print ""
if __name__ == '__main__':
    main()