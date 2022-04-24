my_file = open("switches.txt", "r")
#content = my_file.read()
#print(content)
#content_list = content.split("\n")
#content_list = my_file.readlines()
#Read Switches File with stripping the newline character Line by Line
content_list = [line.rstrip() for line in my_file]
print(content_list)
my_file.close()
#with open('switches.txt') as my_file:
 #       lines = [line.rstrip() for line in my_file]
#print(lines)        
