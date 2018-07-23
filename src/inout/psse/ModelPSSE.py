'''
Created on 15 jul 2014

@author: fragom
'''

class ModelPSSE(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self._components= list()
        self._steadystate= {}
        self._dynamics= {}