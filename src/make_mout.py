import os
import sys
import csv
import numpy as np


shapekeys = ['brow_center_DN', 'brow_center_UP',
             'brow_inner_DN.L', 'brow_inner_UP.L', 'brow_inner_DN.R', 'brow_inner_UP.R',
             'brow_outer_DN.L', 'brow_outer_UP.L', 'brow_outer_DN.R', 'brow_outer_up.R',
             'wince.L', 'wince.R',
             'lip-JAW.DN',
             'eye-blink.LO.L', 'eye-flare.LO.L', 'eye-blink.LO.R', 'eye-flare.LO.R',
             'eye-blink.UP.L', 'eye-flare.UP.L', 'eye-blink.UP.R', 'eye-flare.UP.R',
             'lips-wide.L', 'lips-narrow.L', 'lips-wide.R', 'lips-narrow.R',
             'lips-frown.L', 'lips-frown.R',
             'lip-DN.C.DN', 'lip-DN.C.UP',
             'lip-DN.L.DN', 'lip-DN.L.UP', 'lip-DN.R.DN', 'lip-DN.R.UP',
             'lips-smile.L', 'lips-smile.R',
             'lip-UP.C.DN', 'lip-UP.C.UP',
             'lip-UP.L.DN', 'lip-UP.L.UP', 'lip-UP.R.DN', 'lip-UP.R.UP',
             'sneer.L', 'sneer.R']
# [0:26] = mouth movement, [26:] = eye, blow movement.
reorder = [10, 11, 12, 21, 22,
           23, 24, 25, 26, 27,
           28, 29, 30, 31, 32,
           33, 34, 35, 36, 37,
           38, 39, 40, 41, 42,
           0, 1, 2, 3, 4,
           5, 6, 7, 8, 9,
           13, 14, 15, 16, 17,
           18, 19, 20]

key_name = ['10.wince.L', '11.wince.R', '12.lip-JAW.DN', '21.lips-wide.L', '22.lips-narrow.L',
            '23.lips-wide.R', '24.lips-narrow.R', '25.lips-frown.L', '26.lips-frown.R', '27.lip-DN.C.DN',
            '28.lip-DN.C.UP', '29.lip-DN.L.DN', '30.lip-DN.L.UP', '31.lip-DN.R.DN', '32.lip-DN.R.UP',
            '33.lips-smile.L', '34.lips-smile.R', '35.lip-UP.C.DN', '36.lip-UP.C.UP', '37.lip-UP.L.DN',
            '38.lip-UP.L.UP', '39.lip-UP.R.DN', '40.lip-UP.R.UP', '41.sneer.L', '42.sneer.R']


'''
FUNCTION: extract_mouth(src, dst)
PARAMETERS:
    src - a source directory or a _face.dat file.
    dst - s destination directory or a _mout.dat file.
USAGE:
    This function creates a dat file that contains only a mouth
    part of retargeted mocap data from _face.dat file according to
    provided the list of the original shape keys and reorder indice.
'''


def extract_mouth(src, dst):
    # Load data to np.array and then delete unimportant blendshape columns.
    data = np.loadtxt(src, delimiter=',', dtype=str)
    data = np.delete(data, np.s_[13:27], axis=1)

    # Re-order data line by line.
    data = data[:, reorder]

    # Delete other uni,portant columns.
    data = np.delete(data, np.s_[25:], axis=1)
    data = np.delete(data, np.s_[-2:], axis=1)
    data = np.delete(data, np.s_[0:2], axis=1)
    if not dst == '':
        out_file = dst
    else:
        out_file = src.replace('_face.dat', '_mout.dat')

    writer = csv.writer(open(out_file, 'w'), delimiter=',')
    writer.writerows(data)


def main():
    src = ''
    dst = ''
    try:
        src = sys.argv[1]
    except:
        print('extract_mouth.py [SRC] [DST|NULL]')

    if os.path.isdir(src):
        if not os.path.isdir(src):
            print('Destination not found. Using source directory, instead...')
            dst = src
        file_list = [src + f for f in os.listdir(src) if f.endswith('_face.dat')]
        for file in file_list:
            extract_mouth(file, dst)
    else:
        extract_mouth(src, dst)


if __name__ == "__main__":
    main()
