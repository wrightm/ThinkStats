'''
Created on 27 Apr 2014

@author: wrightm
'''
from chapter6.main.random_variables import generateSample, Normal,\
    LogNormal
from chapter6.main.Pmf import MakePmfFromList
from chapter6.main.myplot import Pmfs, Clf, SaveFormat, Config


def main():
    
    
    log_normal_1 = LogNormal(0,0.3)
    lognorm_nsample_1 = generateSample(log_normal_1, 1000000)
    pmf_log_nsample_1 = MakePmfFromList(lognorm_nsample_1, name='lognorm_with_sample_1')
    
    log_normal_2 = LogNormal(0,0.4)
    lognorm_nsample_2 = generateSample(log_normal_2, 1000000)
    pmf_lognorm_nsample_2 = MakePmfFromList(lognorm_nsample_2, name='lognorm_with_sample_2')
    
    lognorm_nsample_add = lognorm_nsample_1 + lognorm_nsample_2
    pmf_lognorm_nsample_add = MakePmfFromList(lognorm_nsample_add, name='lognorm_with_sample_add')
    
    norm = Normal(1,0.3)
    norm_nsample_8 = generateSample(norm, 1000000)
    pmf_norm_nsample_8 = MakePmfFromList(norm_nsample_8, name='norm_with_sample')
    
    Clf()
    Pmfs([pmf_log_nsample_1, pmf_lognorm_nsample_2, pmf_lognorm_nsample_add, pmf_norm_nsample_8])
    Config()
    SaveFormat('../resources/plots/central_limit_theorem_expo', 'png')
    
if __name__ == '__main__':
    main()