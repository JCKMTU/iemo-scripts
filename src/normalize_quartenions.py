import tf
import os
import sys
import csv
import math
import numpy as np

# Header for output csv file.
header = ['head_x', 'head_y', 'head_z', 'head_w']

'''
Euler to quaternion transformation can be done using following formula,
q = [cos(psi/2), 0, 0, sin(psi/2)][cos(theta/2), 0, sin(theta/2), 0][cos(phi/2), sin(phi/2), 0, 0]

Above formula leads to...
q = [cos(phi/2)*cos(theta/2)*cos(psi/2) + sin(phi/2)*sin(theta/2)*sin(psi/2),
	 sin(phi/2)*cos(theta/2)*cos(psi/2) - cos(phi/2)*sin(theta/2)*sin(psi/2),
	 cos(phi/2)*sin(theta/2)*cos(psi/2) + sin(phi/2)*cos(theta/2)*sin(psi/2),
	 cos(phi/2)*cos(theta/2)*sin(psi/2) + sin(phi/2)*sin(theta/2)*cos(psi/2)]
'''

def vec4_sub(vec1, vec2):
	result = []
	result.append(vec1[0] - vec2[0])
	result.append(vec1[1] - vec2[1])
	result.append(vec1[2] - vec2[2])
	result.append(vec1[3] - vec2[3])

	return result

def euler_to_quaternion(roll, pitch, yaw):
	sin_phi = math.sin(yaw * 0.5)
	cos_phi = math.cos(yaw * 0.5)
	sin_theta = math.sin(roll * 0.5)
	cos_theta = math.cos(roll * 0.5)
	sin_psi = math.sin(pitch * 0.5)
	cos_psi = math.cos(pitch * 0.5)

	x = cos_phi * cos_theta * cos_psi + sin_phi * sin_theta * sin_psi
	y = sin_phi * cos_theta * cos_psi - cos_phi * sin_theta * sin_psi
	z = cos_phi * sin_theta * cos_psi + sin_phi * cos_theta * sin_psi
	w = cos_phi * cos_theta * sin_psi + sin_phi * sin_theta * cos_psi

	return x, y, z, w


# Convert MOCAP_head data to quaternions from euler angles
def quaternion_conversion(file_dir):
	head_data = np.genfromtxt(file_dir, skip_header=2)
	angles = head_data[::5]
	quaternions = []

	#quaternions = normalize_min_max(quaternions)
	angles = normalize_median_np(angles)

	for frame in angles:

		# Convert degrees to radians.
	   	roll = np.deg2rad(-frame[1])
	   	pitch = np.deg2rad(-frame[0])
	   	yaw = np.deg2rad(frame[2])
	   	
	   	# Convert to euler angles to quaternions.
	   	x, y, z, w = euler_to_quaternion(roll, pitch, yaw)

	   	# Append quaternions.
	   	quaternions.append([x, y, z, w])

	# Unity based normalization
	quaternions = normalize_min_max(quaternions)

	# Write converted data to new csv file.
	out_file = file_dir.replace('.head', '_head.dat')
	fd = open(out_file, 'wb')
	writer = csv.writer(fd, delimiter=',')
	#writer.writerow(header)

	for line in quaternions:
		writer.writerow(line)
	fd.close()
	
	print out_file, "created."


'''
Standardization of range can be done by calculating...
(x - min(x,...)) / (max(x,...) - min(x,...))
'''
def normalize_min_max(list_of_vec):
	max_val = 0
	min_val = 0
	for vector in list_of_vec:
		max_tmp = max(vector)
		if max_val < max_tmp: max_val = max_tmp
		
		min_tmp = min(vector)
		if min_val > min_tmp: min_val = min_tmp

	vectors = []
	for vector in list_of_vec:
		vec = []
		for element in vector:
			element = (element - min_val) / (max_val - min_val)
			vec.append(element)
		vectors.append(vec)
	return vectors


def scale_vec(list_of_vec, s_min, s_max):
	max_val = s_max
	min_val = s_min

	vectors = []
	for vector in list_of_vec:
		vec = []
		for element in vector:
			element = element * (max_val - min_val) + min_val
			vec.append(element)
		vectors.append(vec)
	return vectors

def normalize_median(list_of_vec):
	list_sorted = sorted(list_of_vec)
	list_length = len(list_of_vec)

	median = list_sorted[list_length / 2]
	vectors = []
	for vector in list_of_vec:
		vectors.append(vec4_sub(vector, median)) 
	return vectors

def normalize_median_np(list_of_vec):
	list_sorted = np.sort(list_of_vec)
	list_length = len(list_of_vec)
	median = list_sorted[list_length / 2]
	vectors = []

	for vector in range(0, list_length):
		list_of_vec[vector] = np.subtract(list_of_vec[vector], median)
	return list_of_vec

def main():
	try:
		# A directory to files or a file to be modified.
		directory = sys.argv[1]

		# Home directory to IEMOCAP_full_release folder.
		# iemo_home_dir = sys.argv[2]

	except:
		print "normalize_quartenions.py [-file|-dir] [-iemo_home_dir]"
		sys.exit(1)

	

	if os.path.isfile(directory):
		quaternion_conversion(directory)

	# If directory is specified, iterate	
	elif os.path.isdir(directory):
		if not directory.endswith('/'):
			directory = directory + '/'

		files = [directory + f for f in os.listdir(directory) if f.endswith('.head')]
		for file in files:
			quaternion_conversion(file)

if __name__ == '__main__':
	main()