import os
import sys


'''
FUNCTION: validate_frames(files_dir)
PARAMETERS:
    files_dir - a directory to a collection of files.
USAGE:
    This function will check if *_face.dat, *.pho, and *.emo
    are all aligned and has the same frame count.
REQUIREMENTS:
    There has to be 3 files: .dat, .pho, and .emo file with the 
    same actor, category, and session.
'''


def validate_frames(files_dir):

    files = sorted([files_dir + f for f in os.listdir(directory) if f.endswith('_face.dat')])

    fd = open(files_dir + 'file-not-aligned.txt', 'w')

    for file in files:
        # Read lines from a *_face.dat
        face_length = sum(1 for line in open(file))

        # Read lines from a *.pho
        pho_file = file.replace('_face.dat', '.pho')
        pho_length = sum(1 for line in open(pho_file))

        # Read lines from a *.emo
        emo_file = file.replace('_face.dat', '.emo')
        emo_length = sum(1 for line in open(emo_file))

        # Check if their length are equal. If not take a note.
        if not face_length == pho_length == emo_length:
            print face_length, pho_length, emo_length
            print(file + ' Not aligned.')
            fd.write(file.replace('_face.dat', '\r\n'))
    fd.close()


if __name__ == "__main__":
    files_dir = sys.argv[1]
    validate_frames(files_dir)
