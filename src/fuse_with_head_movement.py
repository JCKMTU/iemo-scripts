import tf
import sys
import csv
import numpy as np


def fuse_with_head(rotated_dir, head_dir):

  # Load csv file of facial mocap.
  r_file = open(rotated_dir, 'rb')
  r_reader = csv.reader(r_file, delimiter=',')
  r_list = list(r_reader)
  rotated_header = r_list[0]
  rotated_data = r_list[1:]

  # Load csv file of normalized head rotation.
  h_file = open(head_dir, 'rb')
  h_reader = csv.reader(h_file, delimiter=',')
  h_list = list(h_reader)
  head_header = h_list[0]
  head_data = h_list[1:]

  #rotated_list = np.genfromtxt(rotated_dir, skip_header=1)
  #head_list = np.genfromtxt(head_dir, skip_header=1)

  # Concatenate lists
  header = head_header + rotated_header
  output = []
  for i in range(0, len(head_data)):
    output.append(head_data[i] + rotated_data[i])

  print header
  return header, output



def main():
  try:
    r_dir = sys.argv[1]
    h_dir = sys.argv[2]
  except:
    print "directory not specified."
    sys.exit(1)

  header, output = fuse_with_head(r_dir, h_dir)  
  output_file = h_dir.replace('_normalized.csv', '_fused.csv')
  fd = open(output_file, 'wb')
  writer = csv.writer(fd, delimiter=',')
  writer.writerow(header)
  writer.writerows(output)
  fd.close()

if __name__ == '__main__':
  main()
