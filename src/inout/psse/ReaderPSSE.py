'''
Created on 15 jul 2014

@author: fragom
'''
import psspy

class ReaderPSSE(object):
    '''
    classdocs
    '''
    busPowerFlow= {} #array of dictionaries with busID, P, Q
    busVoltAngle= {} #array of dictionaries with busID, V, Delta
    branchData= {} 
    generatorData= {}
    loadData= []
    
    def __init__(self, studyCase):
        '''
        Constructor
        '''
        psspy.psseinit(1000)
        psspy.case(studyCase)
        
    def getBusesPF(self):
        return self.busPowerFlow
    
    def loadBusesPF(self, ibus, entries):
        ''' retrieve the information of power flow values associated to each branch. Information of branches, 
        pair of buses (fromBus,toBus) is used.
        ibus bus number to start searching
        entries - int number to retrieve either 1) only forward branches or 2) forward and backward branches
        '''
        sid= -1
        flag= 2
        string= ['NUMBER','TYPE']
#         print 'buses', buses
        ierr, buslist = psspy.abusint(sid, flag, string)
#         print 'buslist: ', buslist
        branchlist= []                      
        for frombus in buslist:                             
            psspy.inibrn(frombus[0], entries)                        
            while True:  #branch loop
                ierr,tobus,ckt = psspy.nxtbrn(frombus[0])      
                if ierr != 0:                               
                    break                                   
                branchlist.append((frombus[0],tobus,ckt))
#         print 'branchlist: ', branchlist
        for branch in branchlist: #get branch data       
            frombus,tobus,ckt = branch
            ierr, pflow = psspy.brnflo(frombus,tobus,ckt)  
            if ierr!= 0:
                break
#             print 'pflow: ', pflow
            self.busPowerFlow[frombus] = pflow
        print 'busPowerFlow: ', self.busPowerFlow
        
    def getBusesVA(self):
        return self.busVoltAngle
    
    def loadBusesVA(self, ibus, flag):
        ierr, buses = psspy.abuscount(ibus, flag)
        ierr, (voltages, angle,) = psspy.abusreal(ibus, flag, ['PU','ANGLE'])
#         print 'voltages: ', voltages
#         print 'angle: ', angle
        index= 1
        while index<= buses:
            bus= [voltages[index-1], angle[index-1]]
            self.busVoltAngle[index]= bus
            index+= 1
        print 'busVoltAngle', self.busVoltAngle

    def getBranchZ(self):
        return self.branchData
    
    def loadBranchZ(self, ibus, entries):
        ''' retrieve the information of inductances and admittances of branches of the model
        ibus - bus number to start searching
        entries - int number to retrieve either 1) only forward branches or 2) forward and backward branches
        '''
        sid= -1
        flag= 2
        string= ['NUMBER','TYPE']
        ierr, buslist = psspy.abusint(sid, flag, string)
        ''' retrive info from the branch starting at bus ibus '''
        branchlist= []                                         
        psspy.inibrn(ibus, entries)       
        ierr,tobus,ckt = psspy.nxtbrn(ibus)                                
        branchlist.append((ibus,tobus,ckt))
#         print 'branchlist: ', branchlist
        ''' retrieve info from the branch model 
        Resistance, reactance, admittance sending end, admittance receiving end'''
        branchParam= []
        for branch in branchlist: #get branch data       
            frombus,tobus,ckt = branch
            '''load impedance Z'''
            ierr, cmprx = psspy.brndt2(frombus,tobus,ckt,'RX')
#             print 'cmprx: ', cmprx, 'ierr: ', ierr
            branchParam.append(cmprx)
            '''load conductance G'''
            ierr, cmpishunt = psspy.brndt2(frombus,tobus,ckt,'ISHNT')
#             print 'cmpishunt: ', cmpishunt, 'ierr: ', ierr
            branchParam.append(cmpishunt)
            '''load susceptance B'''
            ierr, cmpjshunt = psspy.brndt2(frombus,tobus,ckt,'JSHNT')
#             print 'cmpjshunt: ', cmpjshunt, 'ierr: ', ierr
            branchParam.append(cmpjshunt)
            if ierr!= 0:
                break
#             print 'pflow: ', pflow
#             print 'branchParam: ', branchParam
            self.branchData[branch] = branchParam
        print 'branchData: ', self.branchData
        
    def getGeneratorVA(self):
        pass
    
    def loadGeneratorVA(self, ibus, entries):
        ierr, machs = psspy.amachcount(ibus, entries)
        print 'machs: ', machs
#         imach= 0
#         while imach< machs: # maquines < machs
        # returns machine identifier for each mach connected to bus ibus 
        ierr, id = psspy.nxtmac(ibus) 
        print 'id: ', id, ' ibus: ', ibus
        ''' P & Q values in complex format '''
        err, cmpval= psspy.gendat(ibus)
        print "gendat: ", cmpval
        ''' Machine static parameters '''
        err, rval= psspy.macdat(ibus,id,'PMAX')
        print 'macdat: ', rval
        err, rval= psspy.macdat(ibus,id,'MVA')
        print 'macdat: ', rval
#         imach+= 1

    def getLoadVA(self):
        return self.loadData
    
    def loadLoadVA(self, _ibus, _flag):
        ierr, busIDs = psspy.aloadchar(sid=_ibus, flag=_flag, string="ID")
        ierr, busNums = psspy.aloadint(sid=_ibus, flag=_flag, string="NUMBER")
#         print 'busIDs: ', busIDs
        print 'busNums: ', busNums
        loadData= []
        for bus in busNums[0]:
            ierr, mvar = psspy.loddt1(bus, busIDs[0][0], 'MVA', 'NOM')
            ierr, ilr = psspy.loddt1(bus, busIDs[0][0], 'IL', 'NOM')
            ierr, ylr = psspy.loddt1(bus, busIDs[0][0], 'YL', 'NOM')
            ierr, mvacmp = psspy.loddt2(bus, busIDs[0][0] , 'MVA', 'NOM')
            ierr, ilcmp = psspy.loddt2(bus, busIDs[0][0] , 'IL', 'NOM')
            ierr, ylcmp = psspy.loddt2(bus, busIDs[0][0] , 'YL', 'NOM')
            busData= dict([('busNum', bus), ('MVAr', mvar), ('MVAcmp', mvacmp), ('ILr', ilr), 
                           ('ILcmp', ilcmp), ('YLr', ylr), ('YLcmp', ylcmp)])
            print 'busData: ', busData
            self.loadData.append(busData)
    
    def loadLoadPF(self, ibus):
        ''' retrieve the information of load values
        ibus - bus number to start searching for loads
        '''
        pass
        
        
    def loadDynamics(self):
        pass