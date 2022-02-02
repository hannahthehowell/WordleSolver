import json

raw_lst = []
with open("word_bank_clean.txt") as file:
    for line in file:
        raw_lst.append(line.rstrip())

distribution = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

total_num_words = len(raw_lst)
for curr_word in raw_lst:
    if len(curr_word) != 5:
        exit(-1)
    letter_set = set(curr_word)
    for letter in letter_set:
        distribution[letter] += 1

percent_distribution = {}
for letter in distribution:
    percent_distribution[letter] = distribution[letter] / total_num_words

file = open("letter_distribution.json", "w")
json.dump(percent_distribution, file)
file.close()
