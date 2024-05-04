#write a program to read from a file and write to another file 

# with( open('/home/hpcap/Desktop/abc.txt',"r+") as file1):
#      print(file1.read())
#      file1.write("\nI am writing")
#      print(file1.read())


# open file1 in reading mode
with open('/home/hpcap/Desktop/abc.txt', 'r') as file1:
    content = file1.read()

# open file2 in writing mode
with open('/home/hpcap/Desktop/file2.txt', 'w') as file2:
    file2.write(content)