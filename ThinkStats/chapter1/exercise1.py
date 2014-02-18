'''
Created on 18 Feb 2014

@author: wrightm
'''
from chapter1.main.survey import Respondents, Pregnancies

def main():
    
    data_dir = '../resources'
    resp = Respondents()
    resp.ReadRecords(data_dir)
    print 'Number of respondents', len(resp.records)

    preg = Pregnancies()
    preg.ReadRecords(data_dir)
    print 'Number of pregnancies', len(preg.records)
    
if __name__ == '__main__':
    main()