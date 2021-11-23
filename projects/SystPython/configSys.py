#!/usr/bin/python3
import sys
import configparser

class SnmpManager:
    def __init__(self, *args):
        # super(SnmpManager, self).__init__(*args))
        self.systems = {}


    def add_system(self,id,descr,addr,port,comm_ro):
        self.systems[id]={'description':descr,
                            'address':addr,
                            'port':int(port),
                            'communityro':comm_ro,
                            'checks':{}}

    def add_check(self,id,oid,descr,system):
        oid_tuple = tuple([int(i) for i in oid.split('.')])
        self.systems[system]['check'][id] = {'diescription':descr,
                                                'oid':oid_tuple}

    def query_all_systems(self): 
        cg = cmdgen.CommandGenerator() 
        for system in self.systems.values(): 
            comm_data = cmdgen.CommunityData('my-manager', system['communityro']) 
            transport = cmdgen.UdpTransportTarget((system['address'], system['port'])) 
            for check in system['checks'].values(): 
                oid = check['oid'] 
                errInd, errStatus, errIdx, result = cg.getCmd(comm_data, transport, oid) 
                if not errInd and not errStatus: 
                    print ("%s/%s -> %s" % (system['description'],
                                            check['description'],
                                             str(result[0][1]))) 





def main(config_file=""):
    if not config_file:
        sys.exit(1)
    config = configparser.ConfigParser()
    conf.read(config_file)
    snmp_manager = SnmpManager()


    for system in [s for s in config.sections() if s.startswith('system')]:
        snmp_manager.add_system(system,config.get(system,'description'),
                                        config.get(system,'address'),
                                        config.get(system,'port'),
                                        config.get(system,'communityro'))

    for check in [c for c in config.sections() if c.startswith('check')]:
        snmp_manager.add_check(check,
                              config.get(check,'oid'),
                              config.get(check,'description'),
                              config.get(check,'system'))
        


if __name__ == '__main__':
   m =  main()
   print(m)