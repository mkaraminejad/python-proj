with open("test.txt", "r") as f:
     lines = f.readlines()
with open("bktest.txt", "a") as f1:
     for line in lines:
         if line.strip("\n") == "192.168.0.0/16":
            f1.write(line)
