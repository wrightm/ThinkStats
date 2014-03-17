'''
Created on 5 Mar 2014

@author: wrightm
'''
from chapter5.main.Pmf import MakePmfFromList
from random import randint

def UniformIntDistribution(min, max, steps):
    
    
    sample = [ min+(((max+1)-min)*i)/(steps) for i in xrange(steps+1) ]
    return sample[:-1]


def UniformPmf(min, max, steps, name=''):
    
    sample = UniformIntDistribution(min, max, steps)
    return MakePmfFromList(sample, name)
    
def MontyHall():
    
    wins_dont_move = 0
    wins_move = 0
    for game in xrange(1000):
        correctDoor = randint(1,3)
        doorA = 1
        doorB = 2
        doorC = 3
        
        if correctDoor == doorA:
            wins_dont_move += 1
            
        if correctDoor != doorB:
            if correctDoor == doorC:
                wins_move += 1
        
        if correctDoor != doorC:
            if correctDoor == doorB:
                wins_move += 1
                
    print "Wins when we stick with the same door for 1000 games = %s, probability = %s" % (wins_dont_move, (wins_dont_move/1000.0)) 
    print "Wins when we move door for 1000 games = %s, probability = %s" % (wins_move, (wins_move/1000.0))

    
    
def main():
     
    MontyHall()            
    
    
if __name__ == '__main__':
    main()