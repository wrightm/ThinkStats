"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import chapter3.main.relay as relay
import chapter3.main.Cdf as Cdf
import chapter3.main.Pmf as Pmf
import chapter3.main.myplot as myplot


def BiasPmf(pmf, speed, name=None):
    """Returns a new Pmf representing speeds observed at a given speed.

    The chance of observing a runner is proportional to the difference
    in speed.

    Args:
        pmf: distribution of actual speeds
        speed: speed of the observing runner
        name: string name for the new dist

    Returns:
        Pmf object
    """
    new = pmf.Copy(name=name)
    for val, prob in new.Items():
        diff = abs(val - speed)
        new.Mult(val, diff)
    new.Normalize()
    return new


def main():
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    # plot the distribution of actual speeds
    pmf = Pmf.MakePmfFromList(speeds, 'actual speeds')

    myplot.Clf()
    myplot.Hist(pmf)
    myplot.Save(root='../resources/plots/observed_speeds_relay',
                title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')

    # plot the biased distribution seen by the observer
    biased = BiasPmf(pmf, 7.5, name='observed speeds')

    myplot.Clf()
    myplot.Hist(biased)
    myplot.Save(root='../resources/plots/observed_speeds_relay',
                title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')

    cdf = Cdf.MakeCdfFromPmf(biased)

    myplot.Clf()
    myplot.Cdf(cdf)
    myplot.Save(root='../resources/plots/observed_speeds_cdf_relay',
                title='CDF of running speed',
                xlabel='speed (mph)',
                ylabel='cumulative probability')
    

if __name__ == '__main__':
    main()
