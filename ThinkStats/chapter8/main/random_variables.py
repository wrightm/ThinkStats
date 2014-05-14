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
        return round(random.expovariate(self.lam),2)

class Erlang(RandomVariable):
    def __init__(self, lam, k):
        self.lam = lam
        self.k = k
        self.expo = Exponential(lam)
        
    def generate(self):
        total = 0
        for i in xrange(self.k):
            total += round(self.expo.generate(), 2)
        return total
    
class Gumbel(RandomVariable):
    
    def __init__(self, mu, beta):
        self.mu = mu
        self.beta = beta
        
    def generate(self):
        return round(numpy.random.gumbel(self.mu, self.beta), 2)
    
class Normal(RandomVariable):
    
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        
    def generate(self):
        return round(numpy.random.normal(self.mu, self.sigma),2)
    
class LogNormal(RandomVariable):
    
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma   
    
    def generate(self):
        return round(numpy.random.lognormal(self.mu, self.sigma),2)
    
class Pareto(RandomVariable):
    
    def __init__(self, shape, mode):
        self.shape = shape
        self.mode = mode
    
    def generate(self):
        return round((numpy.random.pareto(self.shape, 1000) + self.mode),2)
    
class Sum(RandomVariable):
    
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        if not issubclass(self.X, RandomVariable):
            raise TypeError('Object X is not of Subclass Type RandomVariable')
        if not issubclass(self.Y, RandomVariable):
            raise TypeError('Object Y is not of Subclass Type RandomVariable')
        
    def generate(self):
        return round(self.X.generate() + self.X.generate(),2)
    
def generateSample(rand_var, sample_size):
    
    if not issubclass(rand_var.__class__, RandomVariable):
        raise TypeError('Object rand_var is not of Subclass Type RandomVariable')
    return sorted([rand_var.generate() for i in xrange(sample_size)])
        
def main():
    
    print Exponential(1.0).generate()
    print Erlang(1.0, 10).generate()
    print Gumbel(6.0, 4.0).generate()

if __name__ == '__main__':
    main()