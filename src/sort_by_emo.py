# This script is used to combine HEAD_rotated in each sentences mocap data by each actors.
import os
import sys
import csv
import wave
import add_restpose

IEMO_sorted = '../sorted/'
IEMO_combined = '../combined/'

try:
	IEMO_sorted = sys.argv[1]
except:
	print 'using default directory.'

try: 
	IEMO_combined = sys.argv[2]
except:
	print 'using default directory.'

if not os.path.exists(IEMO_sorted):
	print 'specified directory not found.'
	sys.exit(1)

if not os.path.exists(IEMO_combined):
	os.mkdir(IEMO_combined)

emos = sorted(os.listdir(IEMO_sorted))	
doesExist = 0
for emo in emos:

	# Path for the directories for each emotions. 
	emo_path = IEMO_sorted + emo + '/'


	files = sorted([f for f in os.listdir(emo_path) if f.endswith('.txt')])
	print files
	for file in files:
		# Get session and gender from the name of the file
		actor = file.split('_')[0] + '_' + file.split('_')[1] + '_' + emo + '.txt'

		# Set up paths.
		r_dir = emo_path + file
		w_dir = IEMO_combined + emo + '/'	

		if not os.path.exists(w_dir):
			os.mkdir(w_dir)

		with open(r_dir) as in_file:
			w_file = w_dir + actor 
			

			if os.path.exists(w_file) is False: 
				doesExist = 1

			# Open combined file.
			fd = open(w_file, 'a')
			
			# Directory for a file that writes what files have been combined.
			w_file_desc = w_file.replace('.txt', '_description.txt')
			fd_desc = open(w_file_desc, 'a')

			if file.endswith('.txt'):
				fd_desc.write(file + '\r\n')

			if doesExist:
				fd.write(in_file.readline())
				fd.write(in_file.readline())
				doesExist = 0
			else:
				in_file.readline()
				in_file.readline()

			for line in in_file:	
				fd.write(line)

			fd.close()
			in_file.close()