'''
Created on 29 jul 2014

@author: fragom
'''
import os, sys
import psspy
from inout.psse.ReaderPSSE import ReaderPSSE
from inout.modelica.InitModelDYM import WriterMO
from pymodelica import compile_fmu
from pyfmi import load_fmu
# import OMPython
# import inout.modelica.InitModelOMC as objCOMC

def main(argv):
    PSSE_PATH= r'C:\\Program Files (x86)\\PTI\\PSSE33\\PSSBIN'
    sys.path.append(PSSE_PATH)
    os.environ['PATH']+= ';'+ PSSE_PATH
    
#     WORKING PSSE VALUES take .sav value as parameter of the script
    studyCase = 'C:\\Users\\fragom\\PhD_CIM\PSSE\\ieee_9bus\\IEEE_9bus.sav'
    pssread= ReaderPSSE(studyCase)
    
#     '''Information of buses from the power system, inputs must be processed as user entries'''
#     ibus= -1
#     entries= 2
#     pssread.loadBusesPF(ibus, entries)
#     ''' -1 means all buses of the model network '''
#     ibus= -1 
#     flag= 2
#     pssread.loadBusesVA(ibus, flag)
#     '''Information of lines from the power system'''
#     ibus= 1
#     entries= 1
#     pssread.loadBranchZ(ibus, entries)
#     ''' Information of generators from the power system, static and dynamic data'''
#     ibus= 1
#     entries= 1
#     pssread.loadGeneratorVA(ibus, entries)
    ''' Information of loads from the power system, static and dynamic data'''
    ibus= -1 # SID of -1 to assume all buses 
    flag= 4 # FLAG of 4 for all loads on those buses
    pssread.loadLoadVA(ibus, flag)
    print pssread.getLoadVA(
                            )
#     '''Store the information into the model'''
#     branch= pssread.getBranchZ()
#     mowrite= WriterMO()
#     zValues= {}
#     ''' TODO mirar de posar name al branch de psse per usar dictionary.pop(key) '''
#     for value in branch.values():
#         print value[0].real
#         print value[0].imag
#         zValues['pwLine.R']= value[0].real
#         zValues['pwLine.X']= value[0].imag
#         print value[1].real
#         print value[1].imag
#         zValues['pwLine.G']= value[1].imag
#         print value[2]
#         zValues['pwLine.B']= value[2].imag
#         mowrite.setBranchZ(zValues)
        
    '''Information of loads from the power system'''
    
#     WORKING WITH MODELICA VALUES
#     '''Reading model'''
#      # loading the model we want to simulate #
#     '''build the fmu block from the modelica model '''
#     fmu_name= compile_fmu('SmarTSLab.Networks.SMIB1L', 'C:/Users/fragom/PhD_CIM/Modelica/SmarTSLab/SmarTSLab.mo',
#                            compiler_options = {'extra_lib_dirs':'C:/Users/fragom/PhD_CIM/Modelica/Models/Library/'})
#     # Load the model
#     model_fmu= load_fmu(fmu_name)
#     model_fmu.set('pwLine.R',value[0].real)
#     model_fmu.set('pwLine.X',value[0].imag)
#     model_fmu.set('pwLine.G',value[1].imag)
#     model_fmu.set('pwLine.B',value[2].imag)
#     model_fmu.set('genrou1.Angle',0.011)
#     
#     result = model_fmu.simulate(start_time= 0, 
#                                 final_time= 10)
#     
#     print result
#     comOMC= objCOMC.CommandOMC()
#     OMPython.execute("loadModel(Modelica)") 
#     # loading the model we want to simulate #
#     '''extract model name from path'''
#     command= comOMC.loadFile('C:/Users/fragom/PhD_CIM/Modelica/Models/Library/', 'PowerSystems.mo')
#     print '1) ', command
#     OMPython.execute(command)
#     command= comOMC.loadFile('C:/Users/fragom/PhD_CIM/Modelica/SmarTSLab/', 'SmarTSLab.mo')
#     print '2) ',command
#     success= OMPython.execute(command)
#     if (success):
#         command= comOMC.simulate('SmarTSLab.Networks.SMIB1L', '','C:/Users/fragom/PhD_CIM/PYTHON/ScriptSE/params/smib1l.txt', True)
#         print '3) ',command
#         result= OMPython.execute(command)
#         print '4) ', result
#         filename = OMPython.get(result,'SimulationResults.resultFile')
#         print '5) ', filename[1]
    
    '''Writing model'''
    #simulate(ModelName, simflags="-overrideFile=file.txt"); getErrorString(); 
    
if __name__ == '__main__':
    main(sys.argv[1:])