import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_letters_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_letters = {code.letter: code.code for (index, code) in nato_letters_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_name = input("Enter a word: ")
user_nato = [nato_letters[c] for c in user_name.upper()]
print(user_nato)
