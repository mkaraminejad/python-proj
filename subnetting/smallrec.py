with open("test.txt", "r") as f:
     lines = f.readlines()
list_net=[]
for line in lines:
    line=line.strip('\n')
    line=line.split("/")
    list_net.append(int(line[1]))
#sort the cidr blocks
list_net.sort()
print(list_net)

#count=count+1
# Total of subnets in Cidr file
#len_subnets=count-1
#temp=[]*len_subnets



