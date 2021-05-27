import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('X', type=int,
                help="What is the number?")

    args = parser.parse_args()
    X = args.X

if __name__=="__main__":
    main()
