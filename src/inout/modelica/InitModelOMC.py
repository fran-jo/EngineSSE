'''
Created on 11 apr 2014

@author: fragom
'''

class InitModelOMC(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def loadFile(self, _path, _model):
        strcommand = []
        strcommand.append('loadFile(')
        strcommand.append('"')
        strcommand.append(_path)
        strcommand.append(_model)
        strcommand.append('"')
        strcommand.append(')')
        command = ''.join(strcommand)
        command = command.replace('\\','/') 
        print 'loadFile: ', command
        return command
    
    def simulate(self, _model, _simOptions, _modelParams, _isParamsFile):
        strcommand= []
        strcommand.append('simulate(')
        strcommand.append(_model)
        if (_simOptions!= ''):
            strcommand.append(_simOptions)
        if (_isParamsFile):
            strcommand.append(',simflags="-overrideFile=')
            strcommand.append(_modelParams)
            strcommand.append('"')
        else:
            strcommand.append(',simflags="-override ')
            strcommand.append(_modelParams)
            strcommand.append('"')
        strcommand.append(')')
        command = ''.join(strcommand) 
        command= command.replace('\\','/')
        print 'simulate: ', command
        return command
    
    def plot(self, _simOutputs):
        strcommand= []
        strcommand.append('plot({')
        for value in _simOutputs:
            strcommand.append(value)
            strcommand.append(',')
        strcommand= strcommand[:-1]
        strcommand.append('})')
        command = ''.join(strcommand) 
        return command