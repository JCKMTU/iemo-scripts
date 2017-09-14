import os
import csv
import sys
import math
import numpy as np

'''
src can be a file, a dir, or iemocap full path.
dst is a target directory.
'''

if __name__ == "__main__":
    try:
        src = sys.argv[1]
        dst = sys.argv[2]
    except:
        sys.exit(1)

    # The script creates a directory in a parent directory,
    # storing results in each session.
    if src.split('/')[-1].startswith('IEMOCAP_full_release'):
        sessions = [s for s in os.listdir(iemocap_path) if s.startswith('Ses')]

        for session in sessions:
            out_file = open(dst + '/' + session, 'w')

            # Get the list of all the files in the directories.
            mocap_path = iemocap_path + session + '/dialog/MOCAP_rotated/'
            files = [mocap_path + f for f in os.listdir(mocap_path) if f.endswith('.txt')]

            # Call eval_files()
            for file in files:
                result = eval_nan(file)
                out_file.write(result)

    elif os.isdir(src):
        out_file = open(dst + '/nan.txt', 'w')
        file in src:
            result = eval_nan(file)
            out_file.write(result)
    else:
        print eval_nan(src)

    out_file.close()
    print "Evaluation done."
