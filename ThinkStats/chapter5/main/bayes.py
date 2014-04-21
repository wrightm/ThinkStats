'''
Created on 12 Mar 2014

@author: wrightm

P(A and B) = P(B)P(A|B)
P(A and B) = P(A)P(B|A)

P(A or B) = P(A) + P(B), where A and B are mutually exclusive (only one event can happen at a time)
P(A or B) = P(A) + P(B) - P(A and B)

Bayes:

P(B)P(A|B) = P(A)P(B|A)
P(A|B) = P(A)P(B|A) / P(B)

P(A|B) - posterior
P(A) - prior

P(H|E) = P(H)P(E|H) / P(E)

P(H|E) - posterior
P(H) - prior
P(E|H) - Likelihood of evidence
P(E) - normalising constant

'''

def drug_test():

    '''
    P(A and B) = P(B)P(A|B)
    P(A and B) = P(A)P(B|A)
    P(A or B) = P(A) + P(B) - P(A and B)
    if A and B are mutually exclusive (one event happens at a time)then P(A and B) = 0
    
    bayes:
    
    P(A|B)= P(A)P(B|A) / P(B)
    
    P(A|B) = posterior
    P(A) = prior
    P(B|A) = likelihood of evidence
    P(B) = normalisation
    
    Drug test:
    
    P(A) = 0.05
    P(B|A) = 0.60
    P(B) = P(A)P(B|A) + P(N)P(E|N) = (0.05*0.60) + (0.99*0.01)
    P(A|B) = P(A)P(B|A) / P(B) = (0.05*0.60) /  (0.05*0.60) + (0.99*0.01)
    '''
    prior = 0.05
    likelihood_of_evidence = 0.60
    normalising_constant = (0.05*0.60) + (0.99*0.01)
    
    posterior = prior * (likelihood_of_evidence / normalising_constant)
    
    print "drugs test = %s" % posterior
    
def cookies():
    
    '''
    P(bowl 1 | plain) = P(bowl 1)P(plain | bowl 1) / P(plain)
    
    P(bowl 1 | plain) - posterior 
    P(bowl 1) - prior
    P(plain | bowl 1) - likelihood of evidence = 30 / 40
    P(plain | bowl 2) - likelihood of evidence = 20 / 40 = 1 / 2
    P(plain) - normalising constant
    
    bowl 1 - 10 choco + 30 plain = 40 cookies
    bowl 2 - 20 choco + 20 plain = 40 cookies
    
    
    Hypotheses:
    A: plain cookie comes from bowl 1
    B: plain cookie comes from bow 2
    
    prior:
    P(A) = P(B) = 0.5
    
    Evidence:
    E: cookie is plain
     
    Likelihood of evidence:
    P(E|A): 30.0 / 40.0
    P(E|B): 20.0 / 40.0
    
    
    P(A|E) = P(A)P(E|A) / P(E)
    
    P(E) = P(A)P(E|A) + P(B)P(E|B)
    P(E) = 0.5*(30.0/40.0) + 0.5*(20.0/40.0)
    
    P(A)P(E|A) = 0.5*(30.0/40.0)
    
    P(A|E) = (0.5*(30.0/40.0)) / (0.5*(30.0/40.0) + 0.5*(20.0/40.0))
    
    '''
    
    prior = 0.5
    likelihood_of_evidence = 30.0 / 40.0
    normalising_constant = (0.5*(30.0/40.0) + 0.5*(20.0/40.0))
    
    posterior = (prior * likelihood_of_evidence) / normalising_constant
    
    print "chance of cookie coming from bowl 1 = %s" % (posterior)
    
def m_and_ms():
    
    '''
        P(Old | Yellow) = P(Old)P(Yellow | Old) /  P(Yellow)
        
        
        Old = 0.30 Brown + 0.20 Yellow + 0.20 Red + 0.10 Green + 0.10 Orange + 0.10 Tan
        New = 0.13 Brown + 0.14 Yellow + 0.13 Red + 0.20 Green + 0.16 Orange + 0.24 Blue
        
        Hypotheses:
        A: Yellow Bag Old, Green Bag New
        B: Yellow Bag New, Green Bag Old

        Prior:
        P(A) = P(B) = 0.5
        
        Likelihood of Evidence:
        P(E|A) = (0.2)(0.2)
        P(E|B) = (0.14)(0.10)
        
        The evidence is:
        E: yellow from Bag #1, green from Bag #2

        P(A|E) = P(A)P(E|A) / P(E)
        
        P(E) = P(A)P(E|A) + P(B)P(E|B)
        
        P(A|E) = P(A)P(E|A) / (P(A)P(E|A) + P(B)P(E|B))
               = (0.5 * (0.2)*(0.2)) / (0.5*((0.2)*(0.2) + (0.14)*(0.10)))
        
    '''
    prior = 0.5
    likelihood_of_evidence = 0.2 * 0.2
    normalising_factor = 0.5*((0.2)*(0.2) + (0.14)*(0.10))
    
    posterior = (prior * likelihood_of_evidence) / normalising_factor
    
    print "chance of m and m being in bag from 1994 = %s" % posterior
    
def elvis_identical_twin():
    
    '''
    P(identical | twin) = P(identical)P(twin | identical) / P(twin)
    
    Hypotheses:
    A: Elvis was an identical twin
    B: Elvis was a fraternal twin
    
    prior:
    P(A) = 8%
    P(B) = 92%
    
    Evidence:
    E: elvis twin was male
    
    P(E|A) = 1
    P(E|B) = 0.5
    
    P(A|E) = P(A)P(E|A) / P(E)
    P(E) = P(A)P(E|A) + P(B)P(E|B)
    
    P(E) = (0.08 * 1) + (0.92 * 0.5)
    P(A|E) =  (0.08 * 1) / ((0.08 * 1) + (0.92 * 0.5))
    
    
    '''
    prior = 0.08
    likelihood_of_evidence = 1.0
    normalising_factor = (0.08 * 1) + (0.92 * 0.5)
    
    posterior = (prior * likelihood_of_evidence) / normalising_factor
    
    print "chance of elvis being an identical twin = %s" % posterior
    
def blood_crime_scene():
    
    '''
        Oliver blood type O
        
        type O and type AB
        
        type O = 60 %
        type AB = 1%
        
        Hypotheses:
        A: Oliver Blood found at scene of crime
        B: Oliver Blood not found at scene of crime
        
        Prior:
        P(A) = P(B) = 50 %
        
        Evidence:
        E: Two blood samples found types O and AB
        
        P(E|A) = 1(0.01)
        
        P(E|B) = 2(0.60)(0.01)
        
    '''
    
    print "probability of blood O and AB found at scene given oliver blood is found at scene = %s" % 0.01
    print "probability of blood O and AB found at scene given oliver blood is not found at the scene = %s" % (2.0*0.60*0.01)
    
def smoker_cancer():
    
    '''
    Women Smoke = 15.8 %
    Men Smoke = 20.5 %
    
    23 times more likely Men
    13 times more likely Women

    y = 15.8
    1 - y = 84.2
    smoker = y
    non smoker = 1 - y
    cancer smoker = 13x
    cancer non smoker = x
    
    chance of women smoker = 13xy / (13xy + (1-y)x) 
                           = 13 * 15.8 / ((13 * 15.8) + (84.2))
                           
    chance of man smoker = 23xy / (23xy + (1-y)x) 
                         = 23 * 20.5 / ((23 * 20.5) + (79.5))

    '''
    print "chance of women being a smokers = %s"  % (13 * 15.8 / ((13 * 15.8) + (84.2)))
    print "chance of man being a smokers = %s"  % (23 * 20.5 / ((23 * 20.5) + (79.5)))
    

def monty_hall():
    
    '''
    
    Suppose you're on a game show, and you're given the choice of three doors: 
    Behind one door is a car; behind the others, goats. 
    You pick a door, say Door A [but the door is not opened], 
    and the host, who knows what's behind the doors, opens Door B, which has a goat. 
    He then says to you, "Do you want to pick Door C?" Is it to your advantage to switch your choice?
    
    Hypotheses:
    A: Car is behind door A
    B: Car is behind door B
    C: Car is behind door C
    
    Prior:
    P(A)=P(B)=P(C)=1/3
    
    Evidence:
    E: door B has a goat
    
    Likelihood of Evidence:
    P(E|A) = p
    P(E|B) = 0
    P(E|C) = 1 since if door c has a car it will not be shown every time
    
    p = 1/2
    
    P(A|E) = P(A)P(E|A) / P(E)
    
    P(E) = P(A)P(E|A) + P(B)P(E|B) + P(C)P(E|C)
         = 1/3*(p + 1)
         
    P(A)P(E|A) = 1/3*p
    P(A|E) = p / p + 1
        
    p = 1/2
    
    P(A|E) = 1/3
    
    When we don't want it to be behind p i.e. we switch
    
    P(C|E) = 1 / p + 1
    p = 1/2
    
    P(C|E) = 2/3
    '''
    
    prob_of_chosing_a = 0.5
    prior = 0.3
    likelihood_of_evidence = 1
    normalizing_factor = ((prior*prob_of_chosing_a) + (prior*0.0) + (prior*1.0))
    posterior_change = (prior*likelihood_of_evidence) / normalizing_factor
    
    posterior = (prior*prob_of_chosing_a) / normalizing_factor
    
    print "Monty Hall: Change door = %s" % posterior_change
    print "Monty Hall: Do not change door = %s" % posterior
    
    


def main():
    
    drug_test()
    
    cookies()
    
    m_and_ms()
    
    elvis_identical_twin()
    
    blood_crime_scene()
    
    smoker_cancer()
    
    monty_hall()
    
if __name__ == '__main__':
    main()