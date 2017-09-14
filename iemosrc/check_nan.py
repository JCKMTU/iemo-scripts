import os
import csv
import sys
import math
import numpy as np
import pandas as pd

# To read csv or txt files use Pandas

'''
FUNCTION: eval_files(files)
PARAMETERS:
    files - list of files the function evaluates
'''
def eval_files_revised(file):

    # Reading csv files using numpy functions genfromtxt or loadtxt is
    # significantly slower than pandas read_csv.
    data = pd.read_csv(file, delimiter=' ', header=0, skiprows=2)
    npdata = data.values
    nan_sum = sum(data.apply(lambda x: sum(x.isnull()), axis = 1) > 0)

    num_frame = data[-1]
    err = float(nun_sum) / num_frame
    print nan_sum, num_frame, err

def eval_files(files):
    avg_err = 0.0
    all_frames = 0
    num_files = len(files)
    results = []

    for file in files:
        in_file = open(file)
        total_frame = 0
        nan_counter = 0

        # Go through the line
        for line in in_file:
            total_frame += 1

            # Split line and make it to list
            coords = line.split(" ")

            # Go through each coordinates and if NaN increment
            # counter and then break.
            for coord in coords:
                if coord == "NaN":
                    nan_counter += 1
                    break

        # take an account of first two rows of headers.
        total_frame -= 2
        percent = (float(nan_counter) / float(total_frame)) * 100
        result = "%s\tNan = %d" % (file.split('/')[-1], nan_counter)
        result += "\tTotal_frame = %d" % total_frame
        result += "\tError = %.1f%%\n" % percent
        avg_err += percent
        all_frames += total_frame
        results.append(result)

        in_file.close()

    avg_err /= num_files
    end_result = "Average: %.1f\tTotal_frame: %d" % (avg_err, all_frames)
    results.append(end_result)

    return results


if __name__ == "__main__":

    # Default path to iemocap dataset. Assuming it is in parent directory.
    iemocap_path = '../../IEMOCAP_full_release/'
    result_path = '../../check-nan-results/'

    try:
        iemocap_path = sys.argv[1]
    except:
        if not os.path.exists(iemocap_path):
            print "Failed to find a path to a directory for IEMOCAP dataset. \n \
                   check_nan.py [IEMOCAP-PATH]"
            sys.exit(1)

    if not iemocap_path.endswith('/'):
        iemocap_path = iemocap_path + '/'

    # The script creates a directory in a parent directory,
    # storing results in each session.
    if not os.path.exists(result_path):
        os.mkdir(result_path)
        print("A directory is created at '../check-nan-results'")

    sessions = [s for s in os.listdir(iemocap_path) if s.startswith('Ses')]

    for session in sessions:
        # Get the list of all the files in the directories.
        mocap_path = iemocap_path + session + '/dialog/MOCAP_rotated/'
        files = [mocap_path + f for f in os.listdir(mocap_path) if f.endswith('.txt')]

        # For each session, this script creates a file that contains results.
        out_path = result_path + session + '_eval_result.txt'
        out_file = open(out_path, 'w')

        # Call eval_files()
        results = eval_files(files)

        for result in results:
            out_file.write(result)

        out_file.close()

    print "Evaluation done."
