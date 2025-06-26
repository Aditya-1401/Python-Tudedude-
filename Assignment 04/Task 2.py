#Task 2 --> Write and Append Data to a File

text_to_write = input("Enter some text to write to the file: ")
print("Data successfully written to output.txt")

with open('output.txt', 'w') as file:
    file.write(text_to_write + '\n')

additional_text = input("Enter additional text to append to the file: ")
print("Data successfully appended")

with open('output.txt', 'a') as file:
    file.write(additional_text + '\n')

print("\nFinal content of 'output.txt':")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.strip())
