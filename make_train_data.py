import os
import sys
import argparse


if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description='Create train dataset from IEMOCAP.')
    #parser.add_argument('--mode', metavar='mode', type=int,
    #                    help='Mode: 0. process by sessions, 1. process by emotions',
    #                    required=True)
    #parser.add_argument('--iemo', metavar='src', type=str, help='A directory to iemocap dataset', required=True)
    #parser.add_argument('--dest', metavar='dst', type=str, help='Destination folder for processed dataset')
    #parser.add_argument('--comb', help='Combine files based on sessions or files.')

    #args = parser.parse_args()

    for root, dirs, files in os.walk(sys.argv[1]):
        print('root:{}'.format(root))
        print('dirs:{}'.format(dirs))
        print('files:{}'.format(files))
