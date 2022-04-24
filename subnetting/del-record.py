with open("test.txt", "r") as f:
     lines = f.readlines()
with open("test.txt", "w") as f:
     for line in lines:
        if line.strip("\n") != "192.168.0.0/16":
              f.write(line)
