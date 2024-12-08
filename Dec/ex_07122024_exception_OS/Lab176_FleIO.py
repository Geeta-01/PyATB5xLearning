import os

file_name = "Geeta.txt"
content = "This is a Geeta's File Welcome!!!!!!!!!!"

with open(file_name, "w") as file:
    file.write(content)

with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

# os.chdir("Desktop")
