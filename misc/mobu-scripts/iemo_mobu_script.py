import os
import csv
import math
from pyfbsdk import *

home_dir = os.path.expanduser("~")
#There are 55 markers in iemocap data and 57 blendshapes on mimic maya rig.
markers = ['CH1', 'CH2', 'CH3', 'FH1', 'FH2', 
           'FH3', 'LC1', 'LC2', 'LC3', 'LC4',
           'LC5', 'LC6', 'LC7', 'LC8', 'RC1',
           'RC2', 'RC3', 'RC4', 'RC5', 'RC6',
           'RC7', 'RC8', 'LLID', 'RLID', 'MH',
           'MNOSE', 'LNSTRL', 'TNOSE', 'RNSTRL', 'LBM0',
           'LBM1', 'LBM2', 'LBM3', 'RBM0', 'RBM1',
           'RBM2', 'RBM3', 'LBRO1', 'LBRO2', 'LBRO3',
           'LBRO4', 'RBRO1', 'RBRO2', 'RBRO3', 'RBRO4',
           'Mou1', 'Mou2', 'Mou3', 'Mou4', 'Mou5',
           'Mou6', 'Mou7', 'Mou8', 'LHD', 'RHD']


def GetBlendShapeProp(aModel):
   myproplist = list()
   for prop in aModel.PropertyList:
       if prop != None and prop.IsAnimatable() and prop.GetDataTypeName().lower()=="shape":
           myproplist.append(prop)
   return myproplist

   
def GetBlendShapePropName(aModel):
   mypropnamelist = list()
   for prop in aModel.PropertyList:
       if prop != None and prop.IsAnimatable() and prop.GetDataTypeName().lower()=="shape":
           mypropnamelist.append(prop.Name)
   return mypropnamelist


def select(m_name):
    marker = FBFindModelByLabelName('C3D:' + m_name)
    try:
        marker.Selected = True
    except:
        print 'Could not find', m_name    

        
def delete(m_name):
    marker = FBFindModelByLabelName('C3D:' + m_name)
    try:
        marker.Selected = True
        marker.FBDelete()
    except:
        print 'Could not find', m_name

        
def import_c3d(path):
    c3d = FBApplication()
    if c3d.FileImport(path, True) == False:
        print 'Failed to read from"', path, '"'
    else:
        print 'Imported.'

        
def list_files(file_path):
    if os.path.exists(home_dir + file_path) is not True:
        print 'Error.'
        return
        
    file_list = os.listdir(home_dir + file_path)
    c3d_list = []
    
    for item in file_list:
        if item.endswith('.c3d'):
            c3d_list.append(item)
            
    print c3d_list
    return c3d_list

    
def c3d_rotate(x, y, z):   
    markers = FBFindModelByLabelName('C3D:optical')
    markers.Selected = True
    markers.Rotation = FBVector3d(x, y, z)

    
def c3d_translate(x, y, z):
    markers = FBFindModelByLabelName('C3D:optical')
    markers.Selected = True
    markers.Translation = FBVector3d(x, y, z)

	
# Directory of input and output file are not absolute
# Directory starts from home '~/'
def get_blendshapes(dir_path):
    # Get head_geo
    char = FBFindModelByLabelName('head_geo')
    
    
    # Get list of files from directory 
    c3d_list = list_files(dir_path)
    
    for c3d in c3d_list:
        # Import input c3d file
        import_c3d(home_dir + dir_path + c3d)
        
        # Open csvfile
        fd = open(home_dir + dir_path + c3d + '.csv', 'wb')
        writer = csv.writer(fd, delimiter=',')
        
        # This get starting frame and endframe
        scene = FBSystem().Scene
        ctrl = FBPlayerControl()
        fStart = int(ctrl.ZoomWindowStart.GetFrame())
        fStop = int(ctrl.ZoomWindowStop.GetFrame())
    
        # Go to starting frame
        ctrl.GotoStart()
        
        # Iterate over each frames that are available
        for frame in range(fStart, fStop+1):
            #scene.Evaluate()
            blend_shapes = GetBlendShapeProp(char)
            
            if(math.isnan(blend_shapes[0])):
                list_of_zeros = [0] * 57
                writer.writerow(list_of_zeros)
            else:
                writer.writerow(blend_shapes)
            ctrl.StepForward()
        print 'done.'
        fd.close()
        

def write2csv(dir_path):
    # Get head_geo
    char = FBFindModelByLabelName('head_geo')
    
    # Open csvfile
    fd = open(home_dir + dir_path + '.csv', 'wb')
    writer = csv.writer(fd, delimiter=',')    
        
    # This get starting frame and endframe
    scene = FBSystem().Scene
    ctrl = FBPlayerControl()
    fStart = int(ctrl.ZoomWindowStart.GetFrame())
    fStop = int(ctrl.ZoomWindowStop.GetFrame())
    
    # Go to starting frame
    ctrl.GotoStart()
        
    # Iterate over each frames that are available
    for frame in range(fStart, fStop+1):
        #scene.Evaluate()
        blend_shapes = GetBlendShapeProp(char)
            
        if(math.isnan(blend_shapes[0])):
            list_of_zeros = [0] * 57
            writer.writerow(list_of_zeros)
        else:
            writer.writerow(blend_shapes)
        ctrl.StepForward()
    print 'done.'
    fd.close()
    