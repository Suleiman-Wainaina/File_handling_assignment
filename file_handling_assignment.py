#create a file and write content.
with open ("my_file.txt", "w") as file:
  file.write("This is my first line.\n")
  file.write("This is the second line with  a number: 492\n")
  file.write("The last line for now.\n")
print("Successfully created and wrote to 'my_file.txt'. ")

#Open the file in read mode ('r')

with open ("my_file.txt", "r") as file:
  contents = file.readlines()
print (contents)

#Open the file in append mode ('a')
with open ("my_file.txt", "a") as file:
  file.write("\nHere are some additional lines:\n")
  file.write("Line 1 after appending.\n")
  file.write("Line 2 after appending.\n")
  file.write("Line 3 after appending.\n")
print("\nSuccessfully appended content to 'my_file.txt'.")

with open("my_file.txt", "a") as file:
    file.write("\nHere are some additional lines:\n")
    file.write("Line 1 after appending.\n")
    file.write("Line 2 after appending.\n")
    file.write("Line 3 after appending.\n") 
  
try:
    # Code that might raise FileNotFoundError or PermissionError
  pass
  
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while working with the file: {e}")

finally:
#code that will always be executed, regardless of whether an exception occurred or not.
  print("The file 'my_file.txt' has been closed.")
  
