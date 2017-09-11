import sys
from functions import get_medians

def main():
	dest_dir = sys.argv[1]
	iemo_home_dir = sys.argv[2]
	get_medians(iemo_home_dir, dest_dir)


if __name__ == '__main__':
	main()