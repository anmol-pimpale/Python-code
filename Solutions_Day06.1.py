
"""solutions"""


# 1: write a program to take some text lines from the user and write it to the file

# file_handle = open("my_file.txt","w")
# while(True):
#     line_provided = input("Please enter a line :")
#     file_handle.write(line_provided+"\n")
#     choice = input("Do you want to continue (Y/N)").lower()
#     if choice == 'n':
#         break
# file_handle.close()

## 2: write a program to read from a file and write to another file 

# input_file_handle = open("my_file.txt","r")
# output_file_handle = open("my_file_copy.txt","w")

# for input_line in input_file_handle:
#     output_file_handle.write(input_line)

# # output_file_handle.write(input_file_handle.read())
# input_file_handle.close()    
# output_file_handle.close()  
  
## 3: Write a program to read from a file and modify its content 
## by pre-pending each line with "HPCAP" 

# input_file_handle = open("my_file.txt","r")
# contents_in_list = []

# for input_line in input_file_handle:
#     contents_in_list.append(input_line)
# input_file_handle.close()

# input_file_handle = open("my_file.txt","w")    
# for list_input_line in contents_in_list:
#         input_file_handle.write("HPCAP "+list_input_line)

## 4: Write a program to read from a file, pre-pending each line with "HPCAP" 
## and write to the different file 

# input_file_handle = open("my_file.txt","r")
# output_file_handle = open("my_modified_file.txt","w")

# for input_line in input_file_handle:
#     modified_input_line = "HPCAP "+input_line
#     output_file_handle.write(modified_input_line)


# input_file_handle.close()    
# output_file_handle.close()  



"better solutions with context used"
# # program to read from one file and write to another file 

# with open("my_first_file_copy.txt","w+" ) as output_file:
#     with open("my_first_file.txt","r" )  as input_file:
#         for line in input_file:
#             output_file.write(line)



# # # program to read from one file and write to the same file 
# # while pre-pending each line with HPCSA text

# with open('my_first_file.txt') as input_file:
#     input_data_in_list = input_file.readlines()

# with open('my_first_file.txt','w+') as output_file:
#     for input_line in input_data_in_list:
#         output_file.write('HPCAP '+input_line)

# # program to read from one file and write to the different file 
# # while pre-pending each line with HPCSA text in the new created file

with open("my_first_file_copy.txt","w+" ) as output_file:
    with open("my_first_file.txt","r" )  as input_file:
        for line in input_file:
            output_file.write('HPCAP '+ line)
      

