import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create train dataset from IEMOCAP.')
    parser.add_argument('--mode', metavar='mode', type=int,
                        help='Mode: 0. process by sessions, 1. process by emotions',
                        required=True)
    parser.add_argument('--iemo', metavar='src', type=str, help='A directory to iemocap dataset', required=True)
    parser.add_argument('--dest', metavar='dst', type=str, help='Destination folder for processed dataset')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
