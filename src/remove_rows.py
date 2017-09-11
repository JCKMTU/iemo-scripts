import os
import csv
import sys
import itertools


'''
FUNCTION: remove_rows(src, dst, num)
PARAMETERS:
    src - source path to a file to be modified.
    dst - destination path for a modified file if specified.
    num - number of rows to be deleted.
USAGE:
    This function will remove number of rows from a tail of a file.
'''


def remove_rows(src, dst, num):
    # Get length of a file minus number of rows to be deleted.
    length = sum(1 for row in open(src)) - int(num)

    # Instantiate iterreader 
    iterreader = itertools.islice(csv.reader(open(src), delimiter=','), 0, length)

    writer = csv.writer(open(dst, 'w'), delimiter=',')

    for row in iterreader:
        writer.writerow(row)


def main():
    try:
        src = sys.argv[1]
        num_rows = sys.argv[2]

    if os.path.isdir(path):
        files = [path + f for f in os.listdir(path) if os.path.isfile(path + f)]

        for file in files:
            remove_rows(src, dst, num)
    else:
        remove_rows(src, dst, num)


if __name__ == "__main__":
    main()
