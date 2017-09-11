import os
import csv
import sys
import ntpath

iemo_dir = './IEMOCAP_full_release/'

# Check path
if not os.path.exists(iemo_dir):
    print "Could not find iemocap home dir"
    exit(1)

dat = sys.argv[1]
pho = sys.argv[2]
emo = sys.argv[3]

if os.path.isfile(dat):
    path = dat.replace(".dat", '')
    name = ntpath.basename(dat).split('.')[0]
    emo_fd = open(path + '.emo', 'r')
    emo_data = list(emo_fd)
    emo_fd.close()

    pho_fd = open(path + '.pho', 'r')
    pho_data = list(pho_fd)
    pho_fd.close()

    dat_fd = open(dat, 'r')
    dat_data = list(dat_fd)
    dat_fd.close()
    flen = len(dat_data)

    assert len(dat_data) == len(pho_data) == len(emo_data), "length different."
    efd = open('./' + name + '_filtered.emo', 'w')
    e_writer = csv.writer(efd, delimiter=' ')

    pfd = open('./' + name + '_filtered.pho', 'w')
    p_writer = csv.writer(pfd, delimiter=',')

    dfd = open('./' + name + '_filtered.dat', 'w')
    d_writer = csv.writer(dfd, delimiter=',')


    for frame in range(flen):
        emo_data[frame] = emo_data[frame].replace('\r\n', '').split(',')
        pho_data[frame] = pho_data[frame].replace('\r\n', '').split(',')
        dat_data[frame] = dat_data[frame].replace('\r\n', '').split(',')
        if pho in pho_data[frame] and emo in emo_data[frame]:
            e_writer.writerow(emo_data[frame])
            p_writer.writerow(pho_data[frame])
            d_writer.writerow(dat_data[frame])

    efd.close()
    pfd.close()
    dfd.close()

elif os.path.isdir(dat):
    file_list = os.listdir(dat)
    file_list.sort()


    efd = open('./' + ntpath.basename(dat) + '_filtered.emo', 'w')
    e_writer = csv.writer(efd, delimiter=' ')

    pfd = open('./' + ntpath.basename(dat) + '_filtered.pho', 'w')
    p_writer = csv.writer(pfd, delimiter=',')

    dfd = open('./' + ntpath.basename(dat) + '_filtered.dat', 'w')
    d_writer = csv.writer(dfd, delimiter=',')

    for _ in file_list:
        if _.endswith('.dat'):
            name = ntpath.basename(_).split('.')[0]
            emo_fd = open(dat + name + '.emo', 'r')
            emo_data = list(emo_fd)
            emo_fd.close()

            pho_fd = open(dat + name + '.pho', 'r')
            pho_data = list(pho_fd)
            pho_fd.close()

            dat_fd = open(dat + name + '.dat', 'r')
            dat_data = list(dat_fd)
            dat_fd.close()
            flen = len(dat_data)

            for frame in range(flen):
                emo_data[frame] = emo_data[frame].replace('\r\n', '').split(',')
                pho_data[frame] = pho_data[frame].replace('\r\n', '').split(',')
                dat_data[frame] = dat_data[frame].replace('\r\n', '').split(',')
                if pho in pho_data[frame] and emo in emo_data[frame]:
                    e_writer.writerow(emo_data[frame])
                    p_writer.writerow(pho_data[frame])
                    d_writer.writerow(dat_data[frame])

            print name, 'completed.'
    efd.close()
    pfd.close()
    dfd.close()

# set([a,b]).issubset(set[a,b,c]) true
