from engine import PredictionEngine, TextReader

def main():
    """
    Entry point into program
    """
    print('Hello, world')

    t = TextReader('lotr')
    t.setup()
    t.read_and_format_text()

    e = PredictionEngine()
    e.init_dict()
    print(e.char_set)



if __name__ == '__main__':
    main()
