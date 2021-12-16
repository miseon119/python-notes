import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('X', type=int,
                help="What is the number?")

    args = parser.parse_args()
    X = args.X
    
    parser.add_argument('--streaming',
                        action="store_true",
                        required=False,
                        default=False,
                        help='Use streaming inference API. ' +
                        'The flag is only available with gRPC protocol.')
    parser.add_argument('-m',
                        '--model-name',
                        type=str,
                        required=True,
                        help='Name of model')   
    
    #FLAGS = parser.parse_args()
    #FLAGS.model_name
    # FLAGS.streaming
    

if __name__=="__main__":
    main()
