'''
Created on 21 Apr 2014

@author: wrightm
'''
from chapter6.main.first import Mean, Median
import math
from chapter6.main import irs

class Skewness(object):
    
    def __init__(self, sample):
        self.__sample = sample
        self.__mean = Mean(sample)
        self.__median = Median(sample)
        
    def __m2(self):
        """
        Mean Squared Deviation (Variance)
        """
        n = float(len(self.__sample))
        sum_squared = sum(math.pow(x - self.__mean, 2) for x in self.__sample)
        return sum_squared / n
    
    def __m3(self):
        """
        Mean Cubed Deviation
        """
        n = float(len(self.__sample))
        sum_squared = sum(math.pow(x - self.__mean, 3) for x in self.__sample)
        return sum_squared / n
    
    def g1(self):
        """
        basic skeweness, bias to outliers.
        
        -ve skewness. skews left
        +ve skewness. skews right
        """
        return self.__m3() / math.sqrt(math.pow(self.__m2(), 3))
    
    def gp(self):
        """
        Pearson's median skewness coefficient
        """
        sigma = math.sqrt(self.__m2())
        return (3.0*(self.__mean - self.__median)) / sigma
        
def main():
    
    
    skew = Skewness([1,2,3,4,5,1,1,1,1,1,1,1,1,1,1,2,3,4,5,2,3,4,5,2,3,4,5])
    print skew.g1(), skew.gp()
    

if __name__ == '__main__':
    main()