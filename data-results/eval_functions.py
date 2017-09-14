import os
import sys
from math import exp

'''
FUNCTION: get_median(src)
PARAMETERS:
    src - a file
USAGE:
    get meidan of input file
'''


def get_median(src):

	data = sorted(open(src))
	length = len(list(data)) - 2

    # Get median.
	median = [length / 2][2:5]
	f_name = src.split('/')[-1]
    f_dir = src

    fd.close()
	return f_name, median, f_dir


'''
FUNCTION: eval_nan(src)
PARAMETERS:
    src - a file or a list of files
USAGE:
    get a frequency of nan value in a file
'''


def eval_nan(src):
    # Result is aligned in this order,
    # 'File_Name', 'Total_Frames', 'NaN', 'Avg', 'Path'
    fd = open(src)
    total_frame = 0
    nan = 0

    # Go through the line
    for row in fd:
        total_frame += 1

        # Split line and make it to list
        coords = row.split(" ")

        # Go through each coordinates and if NaN increment
        # counter and then break.
        for coord in coords:
            if coord == "NaN":
                nan += 1
                break

    total_frame -= 2
    result = []

    # File_Name, Total_Frames, NaN, Avg, Path
    result.append(src.split('/')[-1])
    result.append("%d" % total_frame)
    result.append("%d" % nan)
    percent = (nan / float(total_frame))
    result.append("%.1f" % exp(percent))
    result.append("%s" % src)
    fd.close()
    return result

'''
FUNCTION:
PARAMETERS:
USAGE:
'''
