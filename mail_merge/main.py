# TODO: Create a letter using starting_letter.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
def return_name(inputs):
    names_list = []
    user_name = ""
    for c in inputs:
        if c != "\n":
            user_name += c
        else:
            names_list.append(user_name)
            user_name = ""
    return names_list


name_list = []
name_file = open("./Input/Names/invited_names.txt", mode="r")
names = name_file.read()
name_list = return_name(names)

letters = open("./Input/Letters/starting_letter.txt", mode="r")
letter_format = letters.read()

for i in range(len(name_list)):
    letter_format_temp = letter_format.replace("[name]", name_list[i])
    with open(f"./Output/ReadyToSend/{name_list[i]}.txt", mode="w") as ready_to_send:
        ready_to_send.write(letter_format_temp)

name_file.close()