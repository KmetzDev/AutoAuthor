import random
import string
import re

class PredictionEngine:
    """
    Handles each letter read by the TextReader
    Creates a history and prediction of next character based upon
    characters seen previously
    """
    char_set = {}
    init_char = ''

    def __init__(self):
        self.init_char = random.choice(string.ascii_lowercase)
        print('Base Prediction:', self.init_char)

    def print_prediction(self):
        print(self.predicted_char)

    def init_dict(self):
        """
        Main data structure for the prediction info
        A dictionary of dictionaries holding letters of alphabet
        and a count of each occurence of the following letter.
        char_set{k: current letter, v: dict{k_2: following letters, v_2: count}}
        """
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        for letter in alpha:
          self.char_set[letter] = {}

        for key in self.char_set:
          for letter in alpha:
              self.char_set[key][letter] = 0

    def get_max_key(self, target):
        """
        Gets the maximum key of the nested dictionary for a given key
        Used to get the most likely following character based on the count of
        occurances of next characters
        """
        target_dict = self.char_set[target]
        return max(target_dict, key=lambda k: target_dict[k])

    def populate_char_set(self, text):
        """
        Iterate over all chars in the prediction text, add the char following
        the current char to the correct position in the char_set
        """
        for idx, char in enumerate(text):
            if idx < len(text) - 1:
                next_char = text[idx + 1]

            if char.isspace() or next_char.isspace() or char == '' or next_char == '':
                pass
            else:
                self.char_set[char][next_char] = self.char_set[char][next_char] + 1

    def show_predictions(self):
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        for key in self.char_set:
            m = self.get_max_key(key)
            print(''+ key + ': ' + m)

    def write_prediction(self, start_char, text):
        """
        Use the prediction dictionary to write the most likely next letters
        """
        for idx, char in enumerate(text):
            if char.isspace() or char == '':
                print('  |  ')
            elif idx < len(text) - 1:
                print('' + char + ' | ' + self.get_max_key(char))


class TextReader:
    """
    Reads the text file passed the constructor one char at a time
    Converts all to lowercase and ignores punctuation (possible future addition)
    """

    def __init__(self, file_name):
        self.file_name = '../text/'+file_name+'.txt'

    def setup(self):
        print('Reading File:', self.file_name)

    def read_and_format_text(self):
        """
        Reads text from file and removes anything other than a<->z A<->Z
        Creates an array of each character in the text file
        """
        self.fmt_text = []
        raw_text = open(self.file_name, 'r')
        for line in raw_text:
            for char in line.lower():
                self.fmt_text.append(re.sub(r'[^a-zA-Z ]','',str(char)))
