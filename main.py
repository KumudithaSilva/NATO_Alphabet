import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for(index, row) in df.iterrows()}
nato_start = True

while nato_start:
    text_value = input("Enter Your Name :").upper()
    if text_value == "EXIT":
        break
    name_letters = [letter for letter in text_value]
    nato_name = [nato_dict[i] for i in name_letters]
    print(nato_name)