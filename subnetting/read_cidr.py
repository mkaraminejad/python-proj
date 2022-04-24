with open ('cidr.txt', 'r') as cidrfile:
    last_line=cidrfile.readlines()[-1]
last_line=last_line.strip('\n')
last_line=last_line.split("/")
#rint(last_line)

