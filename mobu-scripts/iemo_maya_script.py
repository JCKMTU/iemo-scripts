import os
import csv
import maya.mel as mel
import maya.cmds as cmds

dir_path = os.path.exists('C:/outcsv')

# In windows system has to specify existing directory.
file_name = 'C:/Users/masa/Desktop/Datafiles/test.csv'
start_frame = 0
end_frame = mel.eval('playbackOptions -q -maxTime;')

# Open reader
fd = open(file_name, 'wb')
writer = csv.writer(fd, delimiter=',')

# Obtain key values of blend shapes 'head_BS'
head_bs = cmds.listAttr('head_BS.w', m=True)
len_hbs = len(head_bs)

# Write header to csv file
writer.writerow(head_bs)

# Get blendshape weights and write it in csv file
mel.eval('currentTime %s;' % start_frame)
while(start_frame < end_frame):
    keys = []
    for _ in range(0, len_hbs):
        attr = cmds.getAttr('head_BS.w[%d]' % _)
        keys.append(attr)
    writer.writerow(keys) 
    start_frame += 1
    mel.eval('currentTime %s;' % start_frame)
fd.close()

# Obtain key values of blend shapes 'eyelashes_collect_BS'
# Although key values stay zero throughout the all frames,
# so commenting out.
#eyel_bs = cmds.listAttr('eyelashes_collect_BS.w', m=True)
#len_ebs = len(eyel_bs)
#for _ in range(0, len_ebs):
#    attr = cmds.getAttr('eyelashes_collect_BS.w[%d]' % _)
#    keys.append(attr)
