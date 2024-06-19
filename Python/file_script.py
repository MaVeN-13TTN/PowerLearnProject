"""
This script demonstrates basic file handling operations in Python, including
file creation, reading, writing, and appending. It also includes error
handling to manage common file-related exceptions.
"""

# File Creation
try:
    with open("my_file.txt", "w", encoding="utf-8") as file:
        file.write("This is the first line.\n")
        file.write("The value of pi is approximately 3.14159.\n")
        file.write("Hello, Python file handling!")
except PermissionError:
    print("Error: Unable to create the file. Please check the permissions.")
except FileNotFoundError:
    print("Error: The file 'my_file.txt' could not be found.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Contents of the file:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' does not exist.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a", encoding="utf-8") as file:
        file.write("\nThis line is appended to the file.\n")
        file.write("Adding another appended line.\n")
        file.write("The file has been successfully appended.")
except PermissionError:
    print("Error: Unable to append to the file. Please check the permissions.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("File handling tasks completed successfully.")
