'''
Created on 22 Apr 2014

@author: wrightm
'''
import random
import numpy.random


class RandomVariable(object):
    
    def generate(self):
        raise NotImplementedError()
    
class Exponential(RandomVariable):

    def __init__(self, lam):
        self.lam = lam

    def generate(self):
        return random.expovariate(self.lam)

class Erlang(RandomVariable):
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.expo = Exponential(lam)
        
    def generate(self):
        total = 0
        for i in xrange(self.k):
            total += self.expo.generate()
        return total
    
class Gumbel(RandomVariable):
    
    def __init__(self, mu, beta):
        self.mu = mu
        self.beta = beta
        
    def generate(self):
        return numpy.random.gumbel(self.mu, self.beta)
        
def main():
    
    print Exponential(1.0).generate()
    print Erlang(1.0, 10).generate()
    print Gumbel(6.0, 4.0).generate()

if __name__ == '__main__':
    main()