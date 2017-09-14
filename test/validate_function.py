import os, sys, csv, profile, re, os
sys.path.append('/home/masa/HR/iemo-scripts/iemosrc')
import numpy as np
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from fuse_with_head_movement import combine_txt
from get_medians

'''
This file tests performances of functions.
'''

TEST_FILE = './test,txt'


def main():
	rotate_txt = './test-data/MOCAP_rotated_test.txt'
	head_txt = './test-data/MOCAP_head_test.txt'
	eval_txt = './test-data/emoeval_test.txt'

	with PyCallGraph(output=GraphvizOutput()):
        # test to a function from fuse_with_head_movement.py
		fuse_with_head(rotate_txt, head_txt)

		# test to functions from cehck_nan.py
		lis = [rotate_txt]
		#eval_files(lis)
		#eval_files_revised(rotate_txt)

		#profile.run('fuse_with_head("./test-data/MOCAP_rotated_test.txt", "./test-data/MOCAP_head_test.txt")')
		combine_txt(head_txt, rotate_txt)
		get_median('/Desktop/IEMOCAP_full_release')

if  __name__ == '__main__':
	main()
