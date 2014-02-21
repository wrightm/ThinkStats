"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import myplot
import Pmf


def BiasPmf(pmf, name, invert=False):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    If invert=True, computes in inverse operation; for example,
    unbiasing a sample collected from students.

    Args:
      pmf: Pmf object.
      name: string name for the new Pmf.
      invert: boolean

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy()
    new_pmf.name = name

    for x, p in pmf.Items():
        if invert:
            new_pmf.Mult(x, 1.0/x)
        else:
            new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


def UnbiasPmf(pmf, name):
    """Returns the Pmf with oversampling proportional to 1/value.

    Args:
      pmf: Pmf object.
      name: string name for the new Pmf.

     Returns:
       Pmf object
    """
    return BiasPmf(pmf, name, invert=True)


def ClassSizes():

    # start with the actual distribution of class sizes from the book
    d = {
         7: 8, 
         12: 8, 
         17: 14, 
         22: 4, 
         27: 6, 
         32: 12, 
         37: 8, 
         42: 3, 
         47: 2, 
    }

    # form the pmf
    pmf = Pmf.MakePmfFromDict(d, 'actual')
    print 'pmf: mean', round(pmf.Mean(),2)
    print 'pmf: var', round(pmf.Var(),2)
    
    # compute the biased pmf
    biased_pmf = BiasPmf(pmf, 'observed')
    print 'biased_pmf: mean', round(biased_pmf.Mean(),2)
    print 'biased_pmf: var', round(biased_pmf.Var(),2)

    # unbias the biased pmf
    unbiased_pmf = UnbiasPmf(biased_pmf, 'unbiased')
    print 'unbiased_pmf: mean', round(unbiased_pmf.Mean(),2)
    print 'unbiased_pmf: var', round(unbiased_pmf.Var(),2)

    # plot the Pmfs
    myplot.Pmfs([pmf, biased_pmf])
    
    myplot.Config( xlabel='Class size',
                ylabel='PMF')
    
    myplot.SaveFormat('../resources/plots/class_size', 'png')
    
 
def main():
    ClassSizes()


if __name__ == '__main__':
    main()
