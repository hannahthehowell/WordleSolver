class Letter:
    def __init__(self):
        self.is_found = False
        self.correct_letter = ""
        self.not_letters = set()


class Word:
    def __init__(self):
        self.letter_list = [
            Letter(),
            Letter(),
            Letter(),
            Letter(),
            Letter()
        ]
        self.letter_set = set()
        self.does_not_contain_set = set()
