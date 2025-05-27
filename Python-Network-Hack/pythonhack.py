from scapy.all import *

#capture stp frame
pkt = sniff(filter ="ether dst 01:80:c2:00:00:00", count=1)

#print the stp frame
pkt[0]

#view the stp frame 
pkt[0].show()

#view capture frame - show  nicely
pkt[0][0].show()
#view capture frame - show  nicely
pkt[0][1].show()

#view capture frame - show  nicely
pkt[0][2].show()




