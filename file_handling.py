import os

filename = "system_logs.txt"

print("1. Writing data to a new file:")
with open(filename, "w") as file:
    file.write("Log entry 1: Server started successfully.\n")
    file.write("Log entry 2: Database connection established.\n")
print("Data written successfully.")

print("\n2. Reading the entire file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

print("3. Appending new data to the file:")
with open(filename, "a") as file:
    file.write("Log entry 3: User authentication service active.\n")
    file.write("Log entry 4: Daily backup routine triggered.\n")
print("Data appended successfully.")

print("\n4. Reading the file line by line using a loop:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

print("\n5. Reading all lines into a list structure:")
with open(filename, "r") as file:
    all_lines = file.readlines()
    print(f"Total number of log lines: {len(all_lines)}")
    print(f"First line: {all_lines[0].strip()}")
    print(f"Last line: {all_lines[-1].strip()}")

print("\n6. Checking if the file exists before deletion:")
if os.path.exists(filename):
    print(f"Confirmation: '{filename}' exists on the disk.")

print("\n7. Deleting the file to clean up workspace:")
if os.path.exists(filename):
    os.remove(filename)
    print("File has been deleted successfully.")