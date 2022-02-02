import json
from word import Word


def contains_all(word, letter_set):
    return 0 not in [c in word for c in letter_set]


def contains_gray_letters(word, not_letter_lst):
    for letter in word:
        if letter in not_letter_lst:
            return True
    return False


def has_yellows_incorrect(word, letter_lst):
    for i in range(len(letter_lst)):
        if not letter_lst[i].is_found:
            if word[i] in letter_lst[i].not_letters:
                return True
    return False


def has_greens_correct(word, letter_lst):
    for i in range(len(letter_lst)):
        if letter_lst[i].is_found:
            if word[i] != letter_lst[i].correct_letter:
                return False
    return True


def all_letters_green(wordle):
    for letter in wordle.letter_list:
        if not letter.is_found:
            return False
    return True


def modify_possible_solution_list(old_list, wordle):
    # go through each word in possible_solution_list and only keep if
    # 1. word has all green letters in correct positions
    # 2. word has all yellow letters not in incorrect positions
    # 3. word does not have any gray letters

    new_possible_solution_lst = []

    for word_obj in old_list:
        # if it contains all the yellow and green letters
        if contains_all(word_obj["word"], wordle.letter_set):
            # if it does not contain any gray letters
            if not contains_gray_letters(word_obj["word"], wordle.does_not_contain_set):
                # if the yellows are not in the wrong spots
                if not has_yellows_incorrect(word_obj["word"], wordle.letter_list):
                    # if it has the greens in all the correct spots
                    if has_greens_correct(word_obj["word"], wordle.letter_list):
                        new_possible_solution_lst.append(word_obj)

    return new_possible_solution_lst

##################################################################


with open('master_list.json') as json_file:
    master_lst = json.load(json_file)

all_word_lst = [i for i in master_lst]

# sort a list of dictionaries by a key's value using a lambda
possible_solution_lst = sorted(all_word_lst, key=lambda i: (i['frequency_score'], i['placement_score']), reverse=True)

wordle_of_the_day = Word()

guess_num = 0

while guess_num <= 5:
    guess_num += 1
    if len(possible_solution_lst) > 0:
        guess_word_obj = possible_solution_lst[0]
    else:
        print("No possible solutions left")
        exit(1)

    # display guessed word
    print("Guess number " + str(guess_num) + ": " + guess_word_obj["word"])
    is_correct = input("Is this guess correct? [y/n]").lower()
    if is_correct == "y":
        print("You win, the word was: " + guess_word_obj["word"])
        exit(0)

    # allow user to select which letters are which colors
    gray_letters = set()

    for i in range(len(guess_word_obj["letter_list"])):
        curr_letter_in_solution = wordle_of_the_day.letter_list[i]
        curr_letter_in_guess = guess_word_obj["letter_list"][i]

        color_is_valid = False
        color = ""
        color_list = ["green", "yellow", "gray", "grey"]
        while not color_is_valid:
            color = input("What color is " + curr_letter_in_guess + "?").lower()
            if color in color_list:
                color_is_valid = True
            else:
                print("Color input is not valid")

        if color == "green":
            curr_letter_in_solution.is_found = True
            curr_letter_in_solution.correct_letter = curr_letter_in_guess
            wordle_of_the_day.letter_set.add(curr_letter_in_guess)
        else:
            curr_letter_in_solution.not_letters.add(curr_letter_in_guess)
            if color == "yellow":
                wordle_of_the_day.letter_set.add(curr_letter_in_guess)
            elif color == "gray" or color == "grey":
                gray_letters.add(curr_letter_in_guess)

    for g_letter in gray_letters:
        if g_letter not in wordle_of_the_day.letter_set:
            wordle_of_the_day.does_not_contain_set.add(g_letter)

    # if all letters are green, exit with win
    if all_letters_green(wordle_of_the_day):
        print("You win, the word was: " + guess_word_obj["word"])
        exit(0)

    # modify the list of possible solutions
    possible_solution_lst = modify_possible_solution_list(possible_solution_lst, wordle_of_the_day)

# after the 6th guess, if still not correct, lose
print("You lost")
