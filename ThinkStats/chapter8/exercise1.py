'''
Created on 13 May 2014

@author: wrightm
'''
from chapter8.main.random_variables import Normal, generateSample
from chapter8.main import thinkstats
from chapter8.main.estimate import mean_squared_error, mean_error

def main():
    
    normal_distribution = Normal(0,1)
    
    sample_of_means = []
    for _ in xrange(0,1000):
        sample = generateSample(normal_distribution, 6)
        sample_mean = thinkstats.Mean(sample)
        sample_of_means.append(sample_mean)
        
    me = mean_error(sample_of_means, thinkstats.Mean(sample_of_means))
    mse = mean_squared_error(sample_of_means, thinkstats.Mean(sample_of_means))
    
    print 'mean error: ', me
    print 'mean squared error: ', mse
    
    sample_of_medians = []
    for _ in xrange(0,1000):
        sample = generateSample(normal_distribution, 6)
        sample_median = thinkstats.Median(sample)
        sample_of_medians.append(sample_median)
        
    me = mean_error(sample_of_medians, thinkstats.Median(sample_of_medians))
    mse = mean_squared_error(sample_of_medians, thinkstats.Median(sample_of_medians))
    
    print 'median mean error: ', me
    print 'median mean squared error: ', mse
    
    sample_of_var = []
    for _ in xrange(0,1000):
        sample = generateSample(normal_distribution, 6)
        sample_var = thinkstats.Var(sample)
        sample_of_var.append(sample_var)
    
    me = mean_error(sample_of_var, thinkstats.Var(sample_of_var))
    mse = mean_squared_error(sample_of_var, thinkstats.Var(sample_of_var))
    
    print 'variance mean error: ', me
    print 'variance mean squared error: ', mse
    
    sample_of_unbiased_var = []
    for _ in xrange(0,1000):
        sample = generateSample(normal_distribution, 6)
        sample_unbiased_var = thinkstats.UnBiasedVar(sample)
        sample_of_unbiased_var.append(sample_unbiased_var)
        
    me = mean_error(sample_of_unbiased_var, thinkstats.Var(sample_of_unbiased_var))
    mse = mean_squared_error(sample_of_unbiased_var, thinkstats.Var(sample_of_unbiased_var))
    
    print 'unbiased variance mean error: ', me
    print 'unbiased variance mean squared error: ', mse
    
if __name__ == '__main__':
    main()