import tf
import sys
import csv
# Checked

'''
FUNCTION: combine_txt(src1, src2)
PARAMETERS:
    src1 - 1st source file.
    src2 - 2nd source file.
USAGE:
    combines two files, src1 + src2.
'''


def combine_txt(src1, src2):

  # Load csv file of facial mocap.
  r_file = open(src1, 'rb')
  r_reader = csv.reader(r_file, delimiter=',')
  r_list = list(r_reader)
  rotated_header = r_list[0]
  rotated_data = r_list[1:]

  # Load csv file of normalized head rotation.
  h_file = open(src2, 'rb')
  h_reader = csv.reader(h_file, delimiter=',')
  h_list = list(h_reader)
  head_header = h_list[0]
  head_data = h_list[1:]

  # Concatenate lists
  header = head_header + rotated_header
  output = []
  for i in range(0, len(head_data)):
    output.append(head_data[i] + rotated_data[i])

  return header, output


def main():
  try:
    r_dir = sys.argv[1]
    h_dir = sys.argv[2]
  except:
    print "directory not specified."
    sys.exit(1)

  header, output = fuse_with_head(r_dir, h_dir)

  out = h_dir.split('.')[-2] + '_combined' + h_dir.split('.')[-1]
  fd = open(out, 'wb')
  writer = csv.writer(fd, delimiter=',')
  writer.writerow(header)
  writer.writerows(output)
  fd.close()

if __name__ == '__main__':
  main()
