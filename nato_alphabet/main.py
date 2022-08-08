import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


nato_letters_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_letters = {code.letter: code.code for (index, code) in nato_letters_df.iterrows()}
is_on = True
while is_on:
    user_name = input("Enter a word: ")
    try:
        user_nato = [nato_letters[c] for c in user_name.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(user_nato)
        is_on = False
