file = open('example.txt', 'w')  # Open a file in write mode
content = file.write("Hello, World!")  # Write content to the file
file.close()  # Close the file\

file = open('example.txt', 'r')  # Open the file in read mode
content = file.read()  # Read content from the file
print(content)  # Display the content
file.close()  # Close the file