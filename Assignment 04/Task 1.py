#Task 1 --> Read a file and handle errors


#If the file exists
try:
    with open('sample.txt', 'r') as file:
        
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


#If the file is not exists
# try:
#     with open('sample.txt', 'r') as file:
        
#         for line in file:
#             print(line.strip())
# except FileNotFoundError:
#     print("Error: The file 'sample.txt' does not exist.")
