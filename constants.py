from datetime import date
import os

#Set the folder containing all the MtF data you want to visualize:
#(It is assumed that all subfolders of this folder are data for one scout)
#currently set to a subfolder of the folder this file is in called "mtf_data"
MTF_PATH = os.path.dirname(os.path.realpath(__file__)) + os.sep + "mtf_data"

#set the names of mtf_visualize notebooks to use
MTF_VISUALIZE_NAMES = ['mtf_visualize_time', 'mtf_visualize_heatmap', 'mtf_visualize_paths']

#set the names of the scout folders you want to visualize
SCOUT_FOLDER_NAMES = ['Main 1 - LobbyHall', 'Main 2 - LobbyCS', 'Main 3 - MFA']

#encoding of json files gathered from MTF
MTF_JSON_ENCODING = 'ANSI'

#if you want to load data from a specific date range, ignoring boundaries between datasets, using load_mtf_data.from_date_range
#boundary dates are inclusive
DATE_RANGE = (date(2017, 10, 21), date(2017, 12, 15))

#number of pixels on either side of MTF view frame where paths are not reliably detected
#left, top, right, bottom
MTF_DETECTION_PADDING = (30, 30, 30, 30)

# for mtf_visualize_5_paths
NUM_PATHS_TO_DISPLAY = 150
COLORBAR_UPPER_CUTOFF = 30 
#this is the maximum interaction duration to have a color on the colorbar
#(just uses max duration color for longer durations)
#set as None if you want it to automatically set max duration to color as max duration represented in the data
#be aware that not having a standard scale for the colorbar makes it harder to compare multiple graphs

#for mtf_visualize_8_time
WEEKDAYS_TO_DISPLAY = list(range(7)) #Monday is 0, Sunday is 6

LOCALTZ = 'US/Eastern'



