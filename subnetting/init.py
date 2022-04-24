with open ('init.txt', 'r') as initfile:
        line=initfile.readlines()
#        line=line.strip('\n')
        if line == "DONE" : 
            initcidr= True
        else:    
            print("NO INIT CIDR IS ASSIGNED")
            initcidr= False
