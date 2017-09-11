import os
import sys
import numpy as np
import matplotlib.pyplot as plt


mobu_shpk = ['B_CenterDn', 'B_CenterUp',
             'B_InnerLeftDn', 'B_InnerLeftUp', 'B_InnerRightDn', 'B_InnerRightUp',
             'B_OuterLeftDn', 'B_OuterLeftUp', 'B_OuterRightDn', 'B_OuterRightUp',
             'C_SquintLeft', 'C_SquintRight',
             'J_Open',
             'KF_M_FrownLeft_x_M_EeLeftInside', 'KF_M_FrownRight_x_M_EeRightInside',
             'KF_M_LowerLipLeftDn_x_M_LowerLipCenterDn', 'KF_M_LowerLipLeftDn_x_M_LowerLipCenterDn_x_M_LowerLipRightDn',
             'KF_M_LowerLipLeftDn_x_M_LowerLipRightDn', 'KF_M_LowerLipRightDn_x_M_LowerLipCenterDn',
             'KF_M_SmileLeft_x_M_EeLeftInside', 'KF_M_SmileLeft_x_M_FrownLeft',
             'KF_M_SmileRight_x_M_EeRightInside', 'KF_M_SmileRight_x_M_FrownRight',
             'KF_M_UpperLipLeftUp_x_M_UpperLipCenterUp', 'KF_M_UpperLipLeftUp_x_M_UpperLipCenterUp_x_M_UpperLipRightUp',
             'KF_M_UpperLipLeftUp_x_M_UpperLipRightUp', 'KF_M_UpperLipRightUp_x_M_UpperLipCenterUp',
             'L_LowerLidLeftDn', 'L_LowerLidLeftUp', 'L_LowerLidRightDn', 'L_LowerLidRightUp',
             'L_UpperLidLeftDn', 'L_UpperLidLeftUp', 'L_UpperLidRightDn', 'L_UpperLidRightUp',
             'M_EeLeftInside', 'M_EeLeftOutside', 'M_EeRightInside', 'M_EeRightOutside',
             'M_FrownLeft', 'M_FrownRight',
             'M_LowerLipCenterDn', 'M_LowerLipCenterUp',
             'M_LowerLipLeftDn', 'M_LowerLipLeftUp', 'M_LowerLipRightDn', 'M_LowerLipRightUp',
             'M_SmileLeft', 'M_SmileRight',
             'M_UpperLipCenterDn', 'M_UpperLipCenterUp',
             'M_UpperLipLeftDn', 'M_UpperLipLeftUp', 'M_UpperLipRightDn', 'M_UpperLipRightUp',
             'N_SneerLeft', 'N_SneerRight']


faceshift_shpk = ['m_headRotation.x', 'm_headRotation.y', 'm_headRotation.z', 'm_headRotation.w', 
                  'm_headTranslation.x', 'm_headTranslation.y', 'm_headTranslation.z', 
                  'm_neckRotation.x', 'm_neckRotation.y', 'm_neckRotation.z', 
                  'm_neckRotation.w', 'm_eyeGazeLeftPitch', 'm_eyeGazeLeftYaw', 
                  'm_eyeGazeRightPitch', 'm_eyeGazeRightYaw', 
                  'EyeBlink_L', 'EyeBlink_R', 
                  'EyeSquint_L', 'EyeSquint_R', 
                  'EyeDown_L', 'EyeDown_R', 
                  'EyeIn_L', 'EyeIn_R', 
                  'EyeOpen_L', 'EyeOpen_R', 
                  'EyeOut_L', 'EyeOut_R', 
                  'EyeUp_L', 'EyeUp_R', 
                  'BrowsD_L', 'BrowsD_R', 
                  'BrowsU_C_L', 'BrowsU_C_R', 
                  'BrowsU_L', 'BrowsU_R', 
                  'BrowsSqueeze_L', 'BrowsSqueeze_R', 
                  'JawOpen', 
                  'LipsTogether', 
                  'JawLeft', 'JawRight', 
                  'JawFwd', 
                  'LipsUpperUp_L', 'LipsUpperUp_R', 
                  'LipsLowerDown_L', 'LipsLowerDown_R', 
                  'LipsUpperClose', 'LipsLowerClose', 
                  'LipsLowerOpen', 'LipsUpperOpen', 
                  'MouthSharpCornerPull_L', 'MouthSharpCornerPull_R', 
                  'MouthSmile_L', 'MouthSmile_R', 
                  'MouthDimple_L', 'MouthDimple_R', 
                  'LipsStretch_L', 'LipsStretch_R', 
                  'MouthFrown_L', 'MouthFrown_R', 
                  'MouthPress_L', 'MouthPress_R', 
                  'LipsPucker_L', 'LipsPucker_R', 
                  'LipsFunnel_L', 'LipsFunnel_R', 
                  'MouthLeft', 'MouthRight', 
                  'ChinLowerRaise', 'ChinUpperRaise', 
                  'Sneer_L', 'Sneer_R', 
                  'Puff', 
                  'CheekSquint_L', 'CheekSquint_R']


key_name = ['10.wince.L', '11.wince.R', '12.lip-JAW.DN', '21.lips-wide.L', '22.lips-narrow.L',
            '23.lips-wide.R', '24.lips-narrow.R', '25.lips-frown.L', '26.lips-frown.R', '27.lip-DN.C.DN',
            '28.lip-DN.C.UP', '29.lip-DN.L.DN', '30.lip-DN.L.UP', '31.lip-DN.R.DN', '32.lip-DN.R.UP',
            '33.lips-smile.L', '34.lips-smile.R', '35.lip-UP.C.DN', '36.lip-UP.C.UP', '37.lip-UP.L.DN',
            '38.lip-UP.L.UP', '39.lip-UP.R.DN', '40.lip-UP.R.UP', '41.sneer.L', '42.sneer.R']


'''
FUNCTION: plot(face_path, phon_path, key_index)
PARAMETERS:
    face_path - a path to a *_face.dat file which contains facial mocap data.
    phon_path - a path to a *.pho file which contains phonemedata of above file.
    key_index - an index that indicates a blendshape.
USAGE:
    The function plot a graph which shows a relation of phonemes and
    shapekey values.
'''


def plot(face_path, phon_path, key_index):
    mocap_data = np.genfromtxt(face_path, delimiter=',') / 100

    # Get phonemes and create new np.array that contains 0, "SIL" and 1 otherwise.
    phon_data = np.genfromtxt(phon_path, delimiter=',', dtype=str)

    pho_list = []
    for line in phon_data:
        if line[0] == 'SIL':
            pho_list.append(0)
        else:
            pho_list.append(1)
    phon_data = np.array(pho_list)
    length = len(mocap_data)

    shpk = np.arange(len(mocap_data[0]))
    time = np.arange(len(mocap_data))

    plt.clf()
    plt.title("shapekey %s" % mobu_shpk[key_index])
    plt.xlim([0, length])
    legend = []

    plt.plot(time, mocap_data[:, key_index], time, phon_data)
    legend.append(key_index)

    plt.legend(legend)

    file_name = face_path.split('/')[-1]
    print file_name, mobu_shpk[key_index], "Saving..."

    plt.savefig("./png/%s_%s.png" % (file_name, mobu_shpk[key_index]))


def plot_faceshift(face_path, key_index):
    mocap_data = np.genfromtxt(face_path, delimiter=',')[1:]

    shpk = np.arange(len(mocap_data[0]))
    time = np.arange(len(mocap_data))

    length = len(mocap_data)

    plt.clf()
    plt.title("shapekey %s" % faceshift_shpk[key_index])
    plt.xlim([0, length])
    legend = []
    print time  

    new_mocap = np.empty([sum(1 for i in xrange(length) if i % 48 == 0), 77])
    new_time_list = []

    for i in xrange(length):
        if i % 48 == 0:
            np.append(new_mocap, mocap_data[i])
            new_time_list.append(i)
    new_time = np.array(new_time_list)

    plt.plot(new_time_list, new_mocap[:, key_index])
    legend.append(faceshift_shpk[key_index])

    plt.legend(legend)

    file_name = face_path.split('/')[-1]
    print file_name, faceshift_shpk[key_index], "Saving..."

    fig = plt.gcf()
    fig.set_size_inches(30, 10)
    fig.savefig("./png/%s_%s.png" % (file_name, faceshift_shpk[key_index]))


def main():
    try:
        directory = sys.argv[1]
        key = int(sys.argv[2])
    except:
        print('make-plots [DIRECTORY] [SHPK-INDEX]')

    if not os.path.exists('./png'):
        os.mkdir('./png')

    files = [directory + f for f in os.listdir(directory) if f.endswith('.csv')]

    for face_path in files:
        plot_faceshift(face_path, key)


if __name__ == "__main__":
    main()

# 36