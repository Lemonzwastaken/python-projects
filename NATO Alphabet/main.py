import pandas

#TODO 1. Create a dictionary in this format:


data = pandas.read_csv(r"NATO Alphabet\nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
machine_running = True
 
word = input("What word do you need the phonetic alphabet of: ").upper()
    
phonetic_list = [letter_dict[letter] for letter in word]
print(phonetic_list)
