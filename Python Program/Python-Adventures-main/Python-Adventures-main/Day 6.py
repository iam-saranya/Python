# Write to a file and read its content
with open("example.txt", "w") as file:
    file.write("Hello, File!")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)
