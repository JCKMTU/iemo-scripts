import sys
from functions import get_medians

'''
FUNCTION: get_medians(iemo_dir, dest_dir)
PARAMETERS:
  iemo_dir - a home directory to iemocap dataset
  dest_dir - a destination folder.
'''


def get_medians(iemo_dir, dest_dir):
    in_file = iemo_dir
    out_file = dest_dir

    if not iemo_dir.endswith('/'):
	    in_file = in_file + '/'

	# Create dict and open file
    medians = {}
    fd = open(out_file, 'w')
    sessions = [sess for sess in os.listdir(iemo_dir) if sess.startswith('Session')]

    for session in sessions:
        file_dest = in_file + session + '/dialog/MOCAP_head/'
        file_list = [file_dest + f for f in os.listdir(file_dest) if f.startswith('Ses')]

    for file in file_list:
		# Get file content as a numpy array and sort it. Also get number of rows.
		head_data = np.sort(np.genfromtxt(file, skip_header=2))
		head_data = head_data[:,2:5]
		num_rows = len(head_data)

        # Get median.
		median = head_data[num_rows / 2]
		line = file + '/' + np.array_str(median) + '\r\n'
		medians[line] = median
    fd.close()
	print medians
	return medians

def main():
	dest_dir = sys.argv[1]
	iemo_home_dir = sys.argv[2]
	get_medians(iemo_home_dir, dest_dir)


if __name__ == '__main__':
	main()
