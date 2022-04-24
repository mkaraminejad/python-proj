### Write file
def write_cidr(a,b):
    tmp=a+"/"+b
#    print (tmp)
    with open('new_cidr.txt', 'a') as f:
            f.write(tmp+"\n")

