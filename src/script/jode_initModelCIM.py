'''
Created on 14 jan 2015

Intention of this class, use PyCIM to read CIM model and create the corresponding Modelica class / model

@author: fragom
'''
import logging

logging.basicConfig(level=logging.INFO)

from PyCIM import cimread

d = cimread('C:/Users/fragom/PhD_CIM/CIMv16/SmarTSLab/Components/ACLineSegment.xml')

if __name__ == '__main__':
    pass