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
