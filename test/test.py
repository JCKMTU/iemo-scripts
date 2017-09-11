import os
import sys
import csv
import numpy as np 

shpk = np.array(['brow_center_DN', 'brow_center_UP',										 # 0-1
			 'brow_inner_DN.L', 'brow_inner_UP.L', 'brow_inner_DN.R', 'brow_inner_UP.R', # 2-5
			 'brow_outer_DN.L', 'brow_outer_UP.L', 'brow_outer_DN.R', 'brow_outer_up.R', # 6-9
			 'wince.L', 'wince.R', 														 # 10-11
			 'lip-JAW.DN', 																 # 12
			 'eye-blink.LO.L', 'eye-flare.LO.L', 'eye-blink.LO.R', 'eye-flare.LO.R', 	 # 13-16 
			 'eye-blink.UP.L', 'eye-flare.UP.L', 'eye-blink.UP.R', 'eye-flare.UP.R', 	 # 17-20
			 'lips-wide.L', 'lips-narrow.L', 'lips-wide.R', 'lips-narrow.R', 			 # 21-24
			 'lips-frown.L', 'lips-frown.R', 											 # 25-26
			 'lip-DN.C.DN', 'lip-DN.C.UP', 												 # 27-28
			 'lip-DN.L.DN', 'lip-DN.L.UP', 'lip-DN.R.DN', 'lip-DN.R.UP', 				 # 29-32
			 'lips-smile.L', 'lips-smile.R', 											 # 33-34
			 'lip-UP.C.DN', 'lip-UP.C.UP', 												 # 35-36
			 'lip-UP.L.DN', 'lip-UP.L.UP', 'lip-UP.R.DN', 'lip-UP.R.UP', 				 # 37-40
			 'sneer.L', 'sneer.R'])														 # 41-42

orig = np.array(['B_CenterDn', 'B_CenterUp',											 # 0-1
 				 'B_InnerLeftDn', 'B_InnerLeftUp', 'B_InnerRightDn', 'B_InnerRightUp',   # 2-5 
 				 'B_OuterLeftDn', 'B_OuterLeftUp', 'B_OuterRightDn', 'B_OuterRightUp',   # 6-9
 				 'C_SquintLeft', 'C_SquintRight', 										 # 10-11
 				 'J_Open', 																 # 12
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
 				 'N_SneerLeft', 'N_SneerRight'])

# [13:27]
# [0:26] = mouth movement, [26:] = eye, blow movement.
reorder = [10, 11, 12, 21, 22, 
		   23, 24, 25, 26, 27,
		   28, 29, 30, 31, 32,
		   33, 34, 35, 36, 37,
		   38, 39, 40, 41, 42,
		   0, 1, 2, 3, 4,
		   5, 6, 7, 8, 9,
		   13, 14, 15, 16, 17,
		   18, 19, 20]

orig = np.delete(orig, np.s_[13:27], axis=0)
orig = orig[reorder]
print orig

orig = np.delete(orig, np.s_[25:], axis=0)
print orig

#print orig

