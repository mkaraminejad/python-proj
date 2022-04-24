
subnet = cidrtbl[0]
host = cidrtbl[1]
sm = cidrtbl[2]

# Input requested CIDR size, Public & Private
network=cidr_net[0]
print(network)

#### INPUT INFOMARTION"
public=int(input("Public Size: "))
private=int(input("Private Size: "))

# find and calculate proper hosts
counter=0
total=0

size_pub=int(input("Public Times: "))
size_pri=int(input("Private Times: "))

for i in sm:
        if i == public:
                    print(host[counter])
                            total=total+(host[counter]*size_pub)
                                if i == private:
                                            print(host[counter])
                                                    total=total+(host[counter]*size_pri)

                                                        counter=counter+1
                                                        #print(total)

                                                        # find the right host and subnet and required subnet mask
