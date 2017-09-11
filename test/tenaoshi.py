import os
import sys
import csv
import numpy as np 

'''
Universally divide the column that are responsible for jaw opening
by 100 during SIL appears on the .pho file.

Special instruction for 'Sadness'
Multiply the column that are responsible for jaw opening by 3
notes on sadness data
'''

SIL = 100
JAW = 3

mout_data = np.loadtxt(sys.argv[1], delimiter=',') / 100
phon_data = np.loadtxt(sys.argv[2], delimiter=',', dtype=str)


for i, mout in enumerate(mout_data):
	# mout[0] *= 3
	if phon_data[i][0] == 'SIL':
		mout[0] /= SIL


writer = csv.writer(open(sys.argv[1].replace('.dat', '_scaled.dat'), 'w'), delimiter=',')
writer.writerows(mout_data)