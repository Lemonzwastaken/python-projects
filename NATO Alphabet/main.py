import pandas

data = pandas.read_csv(r"NATO Alphabet\nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for (index, row) in data.iterrows()}

machine_running = True

phonetic_list = []

while True:
    word = input("What word do you need the phonetic alphabet of: ").upper()
    try:
        phonetic_list = [letter_dict[letter] for letter in word]
    except KeyError:
        print("Please use words only")
    else:
        print(phonetic_list)
        break
