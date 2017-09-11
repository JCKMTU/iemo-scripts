'''
FILENAME: emo_filter.py
DESCRIPTION:
    
'''

import os
import sys
import shutil as sh

IEM_DIR = sys.argv[1]
OUT_DIR = './sorted/'

EMOTIONS = {'ang': 'Anger',
            'hap': 'Happy',
            'sad': 'Sadness',
            'neu': 'Neutral',
            'fru': 'Frustration',
            'exc': 'Excited',
            'fea': 'Fearful',
            'dis': 'Disgusted',
            'sur': 'Surprise',
            'oth': 'Other',
            'xxx': 'Undefined'}

ADD_RESTPOSE = False

if not os.path.exists(IEM_DIR):
    sys.exit(1)

if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

for emotion in EMOTIONS:
    if not os.path.exists(OUT_DIR + EMOTIONS[emotion]):
        os.mkdir(OUT_DIR + EMOTIONS[emotion])

sessions = [x for x in os.listdir(IEM_DIR) if x.startswith('Session')]
sessions.sort()

for session in sessions:
    emo_dir = IEM_DIR + session + '/dialog/EmoEvaluation/'
    file_list = [x for x in os.listdir(emo_dir) if x.endswith('.txt')]
    file_list.sort()

    for _ in file_list:
        emo_data = list(open(emo_dir + _, 'r'))[2:]
        for index in range(len(emo_data)):
            if emo_data[index].startswith('['):
                line = emo_data[index].split('\t')

                file_name = line[1]
                emotion = line[2]
                if(emotion == 'xxx'):
                    iterator = index + 1
                    partial_emotion_list = []
                    while not emo_data[iterator].startswith('A'):
                        partial_emotion_list.append(emo_data[iterator])
                        iterator += 1

                if os.path.exists(IEM_DIR + '/' + session + '/sentences/MOCAP_rotated/' + _.replace('.txt', '') + '/' + file_name + '.txt') and file_name.split('_')[0][5] == file_name.split('_')[-1][0]:
                    sh.copyfile(IEM_DIR + '/' + session + '/sentences/MOCAP_rotated/' + _.replace('.txt', '') + '/' + file_name + '.txt', OUT_DIR + EMOTIONS[emotion] + '/' + file_name + '.txt')
                    print IEM_DIR + '/' + session + '/sentences/MOCAP_rotated/' + _.replace('.txt', '') + '/' + file_name + '.txt', "done."

                    if os.path.exists(IEM_DIR + '/' + session + '/sentences/wav/' + _.replace('.txt', '') + '/' + file_name + '.wav'):
                        sh.copyfile(IEM_DIR + '/' + session + '/sentences/wav/' + _.replace('.txt', '') + '/' + file_name + '.wav', OUT_DIR + EMOTIONS[emotion] + '/' + file_name + '.wav')
                        print IEM_DIR + '/' + session + '/sentences/wav/' + _.replace('.txt', '') + '/' + file_name + '.wav', "done."
                    else:
                        print 'Could not find', IEM_DIR + '/' + session + '/sentences/wav/' + _.replace('.txt', '') + '/' + file_name + '.wav', 'skipping...'

                else:
                    print 'Could not find', IEM_DIR + '/' + session + '/sentences/MOCAP_rotated/' + _.replace('.txt', '') + '/' + file_name + '.txt', 'skipping...'

                