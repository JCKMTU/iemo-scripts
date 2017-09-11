import os
import sys
import csv
import json
import time

NaN = 0.0


'''
FUNCTION: add_restpose(file_dir, num)
PARAMETERS:
    file_dir - a directory to a file to read.
    num - number of rows to delete.
'''


def add_restpose(file_dir, num):
    rest_poses = json.load(open('./rest_pose.json'))

    actor = file_dir.replace('./', '').split('_')[0]
    with open(file_dir, 'a') as write:
        for _ in range(num):
            buf = str(rest_poses[actor]).replace(",", "")
            buf = buf.replace("]", "")
            buf = buf.replace("[", "") + "\r\n"
            write.write(buf)

        write.close()


def remove_frames(file_dir, num):
    fd = open(file_dir)
    lines = fd.readlines()[:-5]

    writer = csv.writer(open(file_dir, 'w'), delimiter=',')
    for line in lines:
        writer.writerow(line.split(', '))


if __name__ == '__main__':
    try:
        mode = int(sys.argv[1])
        path = sys.argv[2]
    except:
        print "add_restpose.py [-mode] [FILE-PATH]"
        sys.exit(1)

    if not os.path.exists(path):
        print "Path does not exist."
        sys.exit(1)

    if os.path.isfile(path):
        if mode == 0:
            add_restpose(path, 5)
        else:
            remove_frames(path, 5)
    else:
        file_list = os.listdir
        for file in file_list:
            if mode == 0:
                add_restpose(path, 5)
            else:
                remove_restpose(path, 5)
