'''
Created on 4 nov 2014

@author: fragom
'''

class InitModelDYM(object):
    '''
    classdocs
    '''
    paramFile= None

    def __init__(self):
        '''
        Constructor
        '''
        self.paramFile = open('C:/Users/fragom/PhD_CIM/PYTHON/ScriptSE/params/smib1l.txt', 'w')
        
    def setBranchZ(self, zValues):
        ''' save the parameters for the modelica line component in txt file, text file used by Dymola script'''
        ''' save the values directly in the Modelica model ''' 
        for key,value in zValues.items():
            self.paramFile.write(key+ '='+ str(value))
            self.paramFile.write('\n')
        self.paramFile.close()