raw_lst = []

with open("word_bank.txt") as file:
    for line in file:
        raw_lst.append(''.join(ch for ch in line if ch.isalpha()))

textfile = open("word_bank_clean.txt", "w")
for element in raw_lst:
    textfile.write(element + "\n")
textfile.close()

input()