'''
Created on 9 Mar 2014

@author: wrightm

cancer_cases / 1000000 = 1.100266 
prob of 3 = 0.074101
prob of 4 = 0.020122
prob = 0.0, value = 0.332272667727
prob = 1.0, value = 0.699079300921
prob = 2.0, value = 0.900391099609
prob = 3.0, value = 0.974492025508
prob = 4.0, value = 0.994614005386
prob = 5.0, value = 0.999041000959
prob = 6.0, value = 0.999863000137
prob = 7.0, value = 0.999983000017
prob = 8.0, value = 0.999999000001
prob = 9.0, value = 1.0

'''
import numpy
from chapter5.main.Cdf import MakeCdfFromList
from chapter5.main import myplot

def cdc():

    total_cancer_cases = 0.0
    cancer_cases_sample = []
    for game in xrange(1000001):
        sample = []
        cancer_cases = 0.0
        for year in xrange(11):
            p = float(1.0/1000.0)
            sample = sample + list(numpy.random.binomial(1, p, 100))

        for patient in sample:
            if patient == 1:
                cancer_cases += 1.0
                total_cancer_cases += 1.0
        
        cancer_cases_sample.append(cancer_cases)
           
    cancer_cases_cdf = MakeCdfFromList(cancer_cases_sample, "cancer_cases")
    
    myplot.Clf()
    myplot.Cdf(cancer_cases_cdf)
    myplot.Save('../resources/plots/cancer_cases')

    prob_3 = 0.0
    for case in cancer_cases_sample:
        if case == 3:
            prob_3 += 1.0
    prob_3 = prob_3 / 1000000.0
    
    prob_4 = 0.0
    for case in cancer_cases_sample:
        if case == 4:
            prob_4 += 1.0
    prob_4 = prob_4 / 1000000.0
    
    print "cancer_cases / 1000000 = %s " % (total_cancer_cases / 1000000.0)
    print "prob of 3 = %s" % prob_3
    print "prob of 4 = %s" % prob_4
    
    for prob, value in cancer_cases_cdf.Items():
        print "prob = %s, value = %s" % (prob, value)
        
def main():
    
    cdc()
    
if __name__ == '__main__':
    main()