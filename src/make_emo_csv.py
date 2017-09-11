import os 
import csv
import sys

directory = sys.argv[1]

file_list = [directory + f for f in os.listdir(directory) if f.endswith('.head')]
print file_list

for file in file_list:
	emo_file = file.replace('.head', '.emo')
	writer = csv.writer(open(emo_file, 'w'), delimiter=',')

	emo = file.split('_')[-1].replace('.head', '')
	num_lines = sum(1 for line in open(file))

	print num_lines

	for row in range(0, num_lines):
		writer.writerow([emo])
	