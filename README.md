# WordleSolver
Wordle is a game that can be played at https://www.powerlanguage.co.uk/wordle/

The rules are simple: you have 6 chances to guess a 5-letter word.  
Each word you guess is then color-coded by letter.  
* If the letter is green, it means that letter is in the correct spot in the solution
* If the letter is yellow, it means that letter is in the solution, but not at that position
* If the letter is gray, then that letter is not in the solution

To have this program begin solving wordles, simply run solver.py with master_list.json and word.py in the same directory.

If for whatever reason you need to run all the files again to get a working "master_list", 
* Delete all json files in the directory along with all txt files
* Put a word bank txt file as "word_bank.txt" in the directory
* Modify then run clean_word_list.py to produce word_bank_clean.txt in a format of all words in your word bank separated by newlines
* Run find_distribution.py to generate letter_distribution.json
* Run find_placement_freq.py to generate letter_placement.json
* Run get_master_list.py to generate master_list.json
After a new master_list.json is created, solver.py should run as expected.
