import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry! Only enters in the alphabets please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()