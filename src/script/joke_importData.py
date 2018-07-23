'''
Created on 26 jan 2016

@author: fragom
'''
import sys, os
import psspy
import dyntools

def main(argv):
    PSSE_PATH= r'C:\\Program Files (x86)\\PTI\\PSSE33\\PSSBIN'
    sys.path.append(PSSE_PATH)
    os.environ['PATH']+= ';'+ PSSE_PATH
    
    outlst = [argv[0]]
    print outlst
    chnfobj = dyntools.CHNF(outlst)
    print '\n Testing call to get_id'
#     sh_ttl, ch_id = chnfobj.get_id()
    sh_ttl, ch_id, ch_data= chnfobj.get_data()
    print sh_ttl
    print ch_id
#     channels = [ch_id[index[1]] for index in enumerate(ch_id, start= 1)]
    channels = [ch_id[index] for index in range(1, len(ch_id))]
    print ch_id.values()
    print channels
    print 'index -> ', channels.index('VOLT 1 [BUS1 16.500]')
    index= channels.index('VOLT 1 [BUS1 16.500]')+ 1
    print 'index -> ', ch_id.values().index('VOLT 1 [BUS1 16.500]')
    signal= ch_data[1]
    print channels[0]
    print signal
    print ch_data[index]
    print ch_data['time']
    
#     print '\n Testing call to get_range'
#     ch_range = chnfobj.get_range()
#     print ch_range
#     
#     print '\n Testing call to get_scale'
#     ch_scale = chnfobj.get_scale()
#     print ch_scale
#     
#     print '\n Testing call to print_scale'
#     chnfobj.print_scale()
    
#     print '\n Testing call to txtout'
#     chnfobj.txtout(channels=[1,4])
#     
#     print '\n Testing call to xlsout'
#     chnfobj.xlsout(channels=[1,2,3,4,5])

if __name__ == '__main__':
    main(sys.argv[1:])