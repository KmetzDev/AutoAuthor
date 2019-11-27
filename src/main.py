from engine import PredictionEngine, TextReader

def main():
    """
    Entry point into program
    """
    print('Hello, world')

    t = TextReader('lotr')
    t.setup()
    t.read_and_convert_file()



if __name__ == '__main__':
    main()
