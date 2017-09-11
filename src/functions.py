# This script file provides some functions to obtain information from the original IEMOCAP data folder.

import os
import sys
import csv
import wave
import numpy as np
from contextlib import closing


'''
FUNCTION: extract_phseg(file_dir, mlength)
PARAMETERS:
  file_dir - a directory to a files where phseg is located.
  mlength - the actual length of file that phoneme is being written in 
            this will be used to fill the differences of total frames
            and total length of file.
'''


def extract_phseg(file_dir, mlength):
    phonemes = []
    file = list(open(file_dir))[1:-1]

    count = 0

    for line in file:

        # Trim line and get starting and ending frame of phonemes
        line = line.replace('\t', '')
        sframe = int(line[2:5])
        eframe = int(line[8:11])
        print file_dir
        print sframe, eframe
        phone = line[22:].replace('\n', '')
        phone = phone.split(' ')

        # List of phone contains only one phoneme, duplicate it to 4.
        if len(phone) == 1:
            phone.append(phone[0])
            phone.append(phone[0])
            phone.append(phone[0])

        # Add phones to the list in frame interval of ending frame - starting frame + 1
        for i in range(0, eframe - sframe + 1):
            phonemes.append(phone)
            count += 1

    if count < mlength:
      for i in range(0, mlength - count):
        phone = ['SIL', 'SIL', 'SIL', 'SIL']
        phonemes.append(phone)

    return phonemes


'''
FUNCTION: combine_wav(file_dir, home_dir)
PARAMETERS:
  file_dir - a directory to store audio files.
  home_dir - a home directory to iemocap dataset
USAGE:
  combine .wav files.
'''


def combine_wav(file_dir, home_dir):

    # A list to store a collection of wave files to be stored.
    in_wav = []

    # Specify file name for combined wave output
    out_wav = file_dir.replace('_description.txt', '_combined.wav')

    # Open and get file descriptor and then iterate through
    fd = open(file_dir, 'r')
    for file_name in fd:
            # First get what session is in.
            session = 'Session' + file_dir.split('/')[0].split('_')[0][4:5] + '/'

            # Directory to wave file
            wav_file_dir = home_dir + session + each.replace('.txt', '.wav').replace('\r\n', '')
            
            # Append file name to the list 
            in_wav.append(each_dir)

            # Combine wave files
            with closing(wave.open(out_wav, 'wb')) as out:
                # get sample rate from the first wave file in the list.
                with closing(wave.open(in_wav[0], 'rb')) as inp:
                    out.setparams(inp.getparams())


                for audio in in_wav:
                    with closing(wave.open(audio)) as w:
                        out.writeframes(w.readframes(w.getnframes()))


'''
FUNCTION: fuse_with_head(rotated_dir, head_dir)
PARAMETERS:
  rotated_dir - a directory to a facial mocap data
  head_dir - a directory to head rotation data
USAGE:
  combine head and rotated motion data.
'''


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


'''
FUNCTION: get_medians(iemo_dir, dest_dir)
PARAMETERS:
  iemo_dir - a home directory to iemocap dataset
  dest_dir - a destination folder.
USAGE:
  get median values of each head file.
'''


def get_medians(iemo_dir, dest_dir):
  in_file = iemo_dir
  out_file = dest_dir

  if not iemo_dir.endswith('/'):
    in_file = in_file + '/'

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

      fd.write(line)

  fd.close()


'''
FUNCTION: add_restpose(file_dir, num)
          remove_restpose(file_dir, num)

PARAMETERS:
  file_dir - a path to a directory or a file.
  num - number of rows to be modified.

USAGE: 
  add_restpose() is used for adding restpose to mocap data since the software I used for 
  retargetting these mocap data to 3D model is Motionbuilder 2017. It needs a restpose of
  actor markers to determine its rest state; otherwise, retargetted animation will look awkward.
  By adding few frames of rest pose at the end of each files, it is easier to retarget facial 
  mocap data. Rest poses are different depdning on actors and sessions.

  remove_restpose() is used for removing few frames of restposes from files added by add_restpose().
  The function is used for csv file exported by Motionbuilder 2017 with corrected mocap data.
'''


def add_restpose(file_dir, num):
    rest_poses = json.load(open('./rest_pose.json'))

    files = [f for f in os.listdir(dir) if not f.endswith('_description.txt')]
    for file in files:
        actor = file.split('_')[0]
        with open(dir + file, 'a') as write:
            for _ in range(PREPEND_FRAMES):
                buf = str(rest_poses[actor]).replace(",", "")
                buf = buf.replace("]", "")
                buf = buf.replace("[", "") + "\r\n"
                write.write(buf)

        write.close()


def remove_restpose(file_dir, num):
    fd = open(file_dir)
    lines = fd.readlines()[:-5]

    writer = csv.writer(open(file_dir, 'w'), delimiter=',')
    for line in lines:
        writer.writerow(line.split(', '))


'''
FUNCTION: fuse_with_head(rotated_dir, head_dir)

PARAMETERS:
  rotated_dir - is a path to a .txt file which is to be combined with neck rotation data.
  head_dir - is a path to a .csv file which is to be combined with retargeted mocap data.

USAGE:
  this function combines facial mocap data and neck rotateion data. The facial mocap 
  has to be retargetted and normalized to 0 and 1. The neck rotation data also has to
  be converted from euler angles to quaternions, and normalized between 0 and 1: 
  it should not have any negative values.

'''


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





