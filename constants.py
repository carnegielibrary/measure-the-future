from datetime import date
import os

#number of pixels on either side of MTF view frame where paths are not reliably detected
#left, top, right, bottom
MTF_DETECTION_PADDING = (30, 30, 30, 30)

#Set the folder containing all the MtF data you want to visualize:
#(It is assumed that all subfolders of this folder are data for one scout)
#currently set to a subfolder of the folder this file is in called "mtf_data"
MTF_PATH = os.path.dirname(os.path.realpath(__file__)) + os.sep + "mtf_data"


#set the names of mtf_visualize notebooks to use
MTF_VISUALIZE_NAMES = ['mtf_visualize_time', 'mtf_visualize_heatmap', 'mtf_visualize_paths']

#set the names of the scout folders you want to visualize
SCOUT_FOLDER_NAMES = ['DB1 - Entry', 'DB2 - Childrens']

# for mtf_visualize_5_paths
NUM_PATHS_TO_DISPLAY = 150

#for mtf_visualize_8_time
WEEKDAYS_TO_DISPLAY = list(range(7)) #Monday is 0, Sunday is 6

#for mtf_visualize_5_paths, mtf_visualize_5_heatmap, mtf_visualize_8_time
DATE_RANGE = (date(2017, 10, 25), date(2017, 11, 21))

LOCALTZ = 'US/Eastern'

MTF_JSON_ENCODING = 'ANSI'

