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
    e.populate_char_set(t.fmt_text)
    e.show_predictions()
    e.write_prediction(e.init_char, t.fmt_text)



if __name__ == '__main__':
    main()
