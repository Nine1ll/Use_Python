contents = 0
with open("my_file.txt") as file:
    contents = int(file.read()) + 7
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write(str(contents))
# with open("new_file.txt", mode="a") as file:
#     file.write("\nNew Text.2")
