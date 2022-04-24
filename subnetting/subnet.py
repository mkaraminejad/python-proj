#! /bin/python
import os
import readline
import read_cidr
from write_cidr import *
import init 
import cidrtable
import total_ip


# INIT CIDR
getcidr=init.initcidr
print(getcidr)
if getcidr == False:
    cidr_net=read_cidr.last_line
else:
    # go to find smallest one
    print("NO CIDR")

# Import Last Free CIDR RANGE
# Create a table For Calclulate Sunetting
if int(cidr_net[1]) >= 24 :
    print ("Class C")
    cidrtbl=cidrtable.cidrtb(24)
elif int(cidr_net[1]) >= 16 and int(cidr_net[1]) < 24:
    print("Class B")
    cidrtbl=cidrtable.cidrtb(16)
else:
    print("Class A")
    cidrtbl=cidrtable.cidrtb(8)

totalip=total_ip.totalfun(cidrtbl)
subnet = cidrtbl[0]
host = cidrtbl[1]
sm = cidrtbl[2]

# Input requested CIDR size, Public & Private
network=cidr_net[0]
print(network)

total=totalip
print("total: ",totalip)

# find the right host and subnet and required subnet mask
counter=0
while host[counter] > total:
    counter=counter+1
calculated_host     =   host[counter-1]
calculated_subnet   =   subnet[counter-1]
calculated_sm       =   sm[counter-1]
cidr_net[1]         =   str(calculated_sm)
#print(subnet[counter-1]," ",host[counter-1]," /", sm[counter-1])


# Steps for next subnet
subnet_step=int(host[counter-1]/256)
#print(subnet_step)

counter=0
while subnet[counter] <= subnet_step:
    counter=counter+1
selected_sm     =   host[counter-1]
#print(sm[counter-1])


exist_net=cidr_net[0]
find_octaves=exist_net.split(".")
#print(find_octaves[2])

new_octave=int(find_octaves[2])+subnet_step 
#print(new_octave)
find_octaves[2] =str(new_octave)
cidr_net[0]     ='.'.join(find_octaves)
#cidr_net[1]     =str(calculated_sm)

print(cidr_net[0]+"/"+cidr_net[1])
#write_cidr(cidr_net[0],cidr_net[1])
#write_cidr(cidr_net[0])

while new_octave < 255:
    new_octave=new_octave*2
    if new_octave < 255:
        find_octaves[2]=str(new_octave)
        cidr_net[0]='.'.join(find_octaves)
        cidr_net[1]=int(cidr_net[1])-1
        write_cidr(cidr_net[0],str(cidr_net[1]))
#       print(find_octaves)
#        print(cidr_net[0])


#if cidr_net[1] < '24' and cidr_net[1] >= '16':
#    print(y[2])
    
#elif cidr_net[1] >= '24':    
#    print(y[3])
    
#else:
#    print(y[1])

    







