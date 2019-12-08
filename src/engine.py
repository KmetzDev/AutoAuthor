import random
import string
import re

class PredictionEngine:
    """
    Handles each letter read by the TextReader
    Creates a history and prediction of next character based upon
    characters seen previously
    """

    def __init__(self):
        self.predicted_char = random.choice(string.ascii_lowercase)
        print('Base Prediction:', self.predicted_char)

    def print_prediction(self):
        print(self.predicted_char)

    def init_dict(self):
        """
        Main data structure for the prediction info
        A dictionary of dictionaries holding letters of alphabet
        and a count of each occurence of the following letter.
        char_set{k: current letter, v: dict{k_2: following letters, v_2: count}}
        """
        self.char_set = {}
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
        print(target_dict)
        max_key = max(target_dict, key=lambda k: target_dict[k])
        print(max_key)

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
        Creates an array of each character to easily iterate over
        """
        self.fmt_text = []
        raw_text = open(self.file_name, 'r')
        for line in raw_text:
            for char in line:
                self.fmt_text.append(re.sub(r'[^a-zA-Z ]','',str(char)).split())
