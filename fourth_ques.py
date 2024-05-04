#4: Write a program to read from a file, pre-pending each line with "DIOT-" 
# and write to the different file 

with open('/home/hpcap/Desktop/abc.txt', 'r') as file1, open('/home/hpcap/Desktop/file2.txt', 'w') as file2:
    for line in file1:
        file2.write("DIOT-" + line)