# This script will reorder the blendshapes, fuse head rotations,
# convert euler to qurternions, and normalize its coordinates to 0 and 1.

import os
import sys
import csv
import numpy as np


c3d_shapekeys = {'CH1', 'CH2', 'CH3', # Chin markers 0-2
				  'FH1', 'FH2', 'FH3', # Forehead markers 3-5
				  'LC1', 'LC2', 'LC3', 'LC4', 'LC5', 'LC6', 'LC7', 'LC8', # Left cheek markers 6-13
				  'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8', # Right cheek markers 14-21
				  'LLID', 'RLID', # Left eyelid and right eyelid markers 22-23
				  'MH', 'MNOSE', 'LNSTRL', 'TNOSE', 'RNSTRL', # Nose markers 24-28
				  'LBM0', 'LBM1', 'LBM2', 'LBM3', # Above left eyeblow 29-32
				  'RBM0', 'RBM1', 'RBM2', 'RBM3', # Above right eyeblow 33-36
				  'LBRO1', 'LBRO2', 'LBRO3', 'LBRO4', # Left eyeblow markers 37-40
				  'RBRO1', 'RBRO2', 'RBRO3', 'RBRO4', # Right eyeblow markers 41-44
				  'Mou1', 'Mou2', 'Mou3', 'Mou4', 'Mou5', 'Mou6', 'Mou7', 'Mou8', # Mouth markers 45-52
				  'LHD', 'RHD'} # Left head and right head markers 53-54


c3d_shapekeys_ordered = ['LHD', 'RHD', # Left head and right head markers
			  			 'FH1', 'FH2', 'FH3', # Forehead markers
			  			 'LBM0', 'LBM1', 'LBM2', 'LBM3', # Above left eyeblow
			  			 'RBM0', 'RBM1', 'RBM2', 'RBM3', # Above right eyeblow
			  			 'LBRO1', 'LBRO2', 'LBRO3', 'LBRO4', # Left eyeblow markers
		 	  			 'RBRO1', 'RBRO2', 'RBRO3', 'RBRO4', # Right eyeblow markers
		 	  			 'LLID', 'RLID', # Left eyelid and right eyelid markers
		 	  			 'LC1', 'LC2', 'LC3', 'LC4', 'LC5', 'LC6', 'LC7', 'LC8', # Left cheek markers
		 	  			 'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8', # Right cheek markers
		 	  			 'MH', 'MNOSE', 'LNSTRL', 'TNOSE', 'RNSTRL', # Nose markers
		 	  			 'Mou1', 'Mou2', 'Mou3', 'Mou4', 'Mou5', 'Mou6', 'Mou7', 'Mou8', # Mouth markers
		 	  			 'CH1', 'CH2', 'CH3'] # Chin markers


c3d_shpk_indice_ordered = [53, 54, 						# 'LHD', 'RHD' Left head and right head markers
 	     				   3, 4, 5, 						# 'FH1', 'FH2', 'FH3' Forehead markers
 	     				   29, 30, 31, 32,					# 'LBM0', 'LBM1', 'LBM2', 'LBM3' Above left eyeblow
 	     				   33, 34, 35, 36,					# 'RBM0', 'RBM1', 'RBM2', 'RBM3' Above right eyeblow
 	     				   37, 38, 39, 40,					# 'LBRO1', 'LBRO2', 'LBRO3', 'LBRO4' Left eyeblow markers
 	     				   41, 42, 43, 44,					# 'RBRO1', 'RBRO2', 'RBRO3', 'RBRO4' Right eyeblow markers
 	     				   22, 23, 						# 'LLID', 'RLID' Left eyelid and right eyelid markers
 	     				   6, 7, 8, 9, 10, 11, 12, 13, 	# 'LC1', 'LC2', 'LC3', 'LC4', 'LC5', 'LC6', 'LC7', 'LC8' Left cheek markers
 	     				   14, 15, 16, 17, 18, 19, 20, 21,	# 'RC1', 'RC2', 'RC3', 'RC4', 'RC5', 'RC6', 'RC7', 'RC8' Right cheek markers
 	     				   24, 25, 26, 27, 28,				# 'MH', 'MNOSE', 'LNSTRL', 'TNOSE', 'RNSTRL' Nose markers
 	     				   45, 46, 47, 48, 49, 50, 51, 52,	# 'Mou1', 'Mou2', 'Mou3', 'Mou4', 'Mou5', 'Mou6', 'Mou7', 'Mou8' Mouth markers
 	     				   0, 1, 2]						# 'CH1', 'CH2', 'CH3' Chin markers


'''
FUNCTION: reorder(path_to_input)
PARAMETERS:
    path_to_input - path of a input file
USAGE:
    reorder columns of an input file.
'''


def reorder(path_to_input):
 	if not path_to_input.endswith('.csv'):
 		return -1

 	output = []

 	with open(path_to_input, 'rb') as in_csv:
 		reader = csv.reader(in_csv)
 		for line in reader:
 			line = [line[i] for i in re_order]
 			output.append(line)

 	return output


def main():
	try:
		input_dir = sys.argv[1]
	except:
		print "reoder.py [retargetted_csv_file]"
		sys.exit(1)

	if not os.path.exists(input_dir):
		print input_dir, "path does not exist."
		sys.exit(1)

	# Reorder list.
	reordered_list = reorder(input_dir)

	# Write them into csv.
	out_file = input_dir.replace('.c3d.csv', '_reordered.csv')
	fd = open(out_file, 'wb')
	writer = csv.writer(fd, delimiter=',')
	writer.writerows([new_header])
	writer.writerows(reordered_list)


if __name__ == '__main__':
	main()
