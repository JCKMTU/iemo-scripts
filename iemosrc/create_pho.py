import os
import csv
import sys
from functions import extract_phseg

'''
FUNCTION: create_pho(combined_dir, iemo_home_dir)
PARAMETERS:
	combined_dir - a directory that contains files which is categorized and combined by emotion.
	iemo_home_dir - a home directory of iemocap dataset.
'''

def create_pho(combined_dir, iemo_home_dir):
	directory = combined_dir
	iemo_full_release = iemo_home_dir

	if not directory.endswith('/'):
		directory = directory + '/'


	file_list = [directory + f for f in os.listdir(directory) if f.endswith('_description.txt')]

	# Go through each file name written in the file.
	for file in file_list:
		file_name_list = open(file)
		writer = csv.writer(open(file.replace('_description.txt', '.pho'), 'w'), delimiter=',')

		
		for line in file_name_list:
			line_list = line.split('_')
			if len(line_list) == 3:
				sess = 'Session' + line_list[0][4:5] + '/sentences/ForcedAlignment/' + line_list[0] + '_' + line_list[1] + '/'
				head = 'Session' + line_list[0][4:5] + '/sentences/MOCAP_head/' + line_list[0] + '_' + line_list[1] + '/'
			else:
				sess = 'Session' + line_list[0][4:5] + '/sentences/ForcedAlignment/' + line_list[0] + '_' + line_list[1] + '_' + line_list[2] + '/'
				head = 'Session' + line_list[0][4:5] + '/sentences/MOCAP_head/' + line_list[0] + '_' + line_list[1] + '_' + line_list[2] + '/'

			max_line = sum(1 for l in open(iemo_full_release + head + line.replace('\r\n', ''))) - 2


			line = iemo_full_release + sess + line.replace('.txt', '.phseg').replace('\r\n', '')
			phonemes = extract_phseg(line, max_line)

			for phoneme in phonemes:
				writer.writerow(phoneme)


if __name__ == "__main__":
	create_pho(sys.argv[2], sys.argv[1])