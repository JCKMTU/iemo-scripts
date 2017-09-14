import os
import csv
import sys
import itertools


'''
FILENAME: copy_head.py
DESCRIPTION:
	This script creates neck rotataion data using the files from IEMOCAP data.
	It needs a _description.txt file which contains information of what files 
	combined facial mocap data consists of. Based on the _description.txt file,
	this script fetches IEMO_head files and combine into one.
'''


def main():
	directory = sys.argv[1]
	iemo_full_release = sys.argv[2]

	if not directory.endswith('/'):
		directory = directory + '/'

	if not iemo_full_release.endswith('/'):
		iemo_full_release = iemo_full_release + '/'



	file_list = [directory + f for f in os.listdir(directory) if f.endswith('_description.txt')]

	# Go through each file name written in the file.
	for file in file_list:
		file_name_list = open(file)
		writer = csv.writer(open(file.replace('_description.txt', '.head'), 'w'), delimiter=',')

		
		for line in file_name_list:
			line_list = line.split('_')
			if len(line_list) == 3:
				sess = iemo_full_release + 'Session' + line_list[0][4:5] + '/sentences/MOCAP_head/' \
										 + line_list[0] + '_' + line_list[1] + '/' + line.replace('\r\n', '')
			else:
				sess = iemo_full_release + 'Session' + line_list[0][4:5] + '/sentences/MOCAP_head/' \
										 + line_list[0] + '_' + line_list[1] + '_' + line_list[2] + '/' + line.replace('\r\n', '')
				
			iteration = 0
			reader = csv.reader(open(sess, 'r'), delimiter=',')
			for row in reader:
				if(iteration > 1):
					writer.writerow(row)
				iteration += 1

		file_name_list.close()


if __name__ == "__main__":
	main()


		