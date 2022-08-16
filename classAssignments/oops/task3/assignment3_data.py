import logging as log
log.basicConfig(filename='data.log',level=log.INFO,format='%(levelname)s: %(asctime)s %(message)s')
log.info('logged into assignment3_data')
class data:
    def __init__(self):
        self.l=[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]