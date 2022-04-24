def cidrtb(a):
    subnet=[]
    host=[]
    sm=[]
    subnet_index=1
    if a == 16 :
        cnt=16
    elif a==24:
        cnt=8
    else:
        cnt=24

    for i in range(0,cnt+1):
        subnet.append(subnet_index)
        subnet_index=subnet_index*2
    host=subnet[::-1]
    sm_index=a
    for i in range(0,cnt+1):
        sm.append(sm_index)
        sm_index=sm_index+1

#    print(host)
#    print(subnet)
#    print(sm)
    return(subnet,host,sm)
