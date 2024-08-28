# Read from data.txt
file1 = open("data.txt", "r")
data = file1.read()
print("Contents of data.txt:")
print(data)
print()  # Print a blank line for separation
file1.close()  # Close the file after reading

# Write to result.txt
file2 = open("result.txt", "w")
str1 = 'Learning Python is fun!'
file2.write(str1)
print("Written to result.txt:")
print(f"'{str1}'")
print()  # Print a blank line for separation
file2.close()  # Close the file after writing

# Read and write from data.txt
file3 = open("data.txt", "r+")
print("Reading first 20 characters from data.txt:")
print(file3.readline(20))  # Read the first 20 characters
file3.close()  # Close the file after reading and writing
