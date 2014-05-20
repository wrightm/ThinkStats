'''
Created on 19 May 2014

@author: wrightm
'''
from chapter8.main.locomotive import MakeUniformSuite, Update, CredibleInterval
from matplotlib import pyplot
from chapter8.main import myplot

def main():
    
    upper_bound = 200
    prior = MakeUniformSuite(1, upper_bound, upper_bound)
    prior.name = 'prior'

    evidence = [60] 
    #evidence = [60, 61, 63, 70]
    #evidence = [60, 61, 63, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70]
    posterior = prior.Copy()
    Update(posterior, evidence)
    posterior.name = 'posterior'

    print CredibleInterval(posterior, 90)

    # plot the posterior distribution
    pyplot.subplots_adjust(wspace=0.4, left=0.15)
    plot_options = dict(linewidth=2)

    myplot.Pmf(posterior, **plot_options)
    myplot.Save(root='../resources/plots/locomotive',
                title='Locomotive problem',
                xlabel='Number of trains',
                ylabel='Posterior probability')
    
if __name__ == '__main__':
    main()