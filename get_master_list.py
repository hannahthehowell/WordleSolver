import json


def get_freq_score(word):
    letter_set = set(word)
    total = 0
    for letter in letter_set:
        total += letter_distribution[letter]
    return total


def get_plac_score(word):
    total = 0
    for i in range(len(word)):
        curr_letter = word[i]
        total += letter_plac_lst[i][curr_letter]
    return total


with open('letter_distribution.json') as json_file:
    letter_distribution = json.load(json_file)

with open('letter_placement.json') as json_file:
    letter_plac_lst = json.load(json_file)

raw_lst = []
with open("word_bank_clean.txt") as file:
    for line in file:
        raw_lst.append(line.rstrip())

master_list = []
for curr_word in raw_lst:
    obj = {
        "word": curr_word,
        "letter_list": [letter for letter in curr_word],
        "frequency_score": get_freq_score(curr_word),
        "placement_score": get_plac_score(curr_word)
    }
    master_list.append(obj)

file = open("master_list.json", "w")
json.dump(master_list, file)
file.close()
