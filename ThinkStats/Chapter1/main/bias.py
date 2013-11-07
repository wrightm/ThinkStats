'''
Created on 26 Oct 2013

@author: wrightm
'''

class BiasPmf(object):
    '''
    Base class for Biases for a given Pmf
    '''

    def __call__(self, value):
        '''
        Calculate bias for particular value from pmf
        
        @param value: value from pmf
        @return: bias factor for particular pmf value
        '''
        return value