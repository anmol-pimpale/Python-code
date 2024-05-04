#Write a program to read from a file and modify eacf of its line
# by pre-pending each line with "DIOT-" 

# ex: 
# i/p : hello
#       good morning  

# o/p:      DIOT-hello
#           DIOT-good morning

with  open('/home/hpcap/Desktop/abc.txt', 'r') as file1,open('/home/hpcap/Desktop/file2.txt', 'w') as file2:
    for line in file1:
        file2.write("DIOT-" + line)