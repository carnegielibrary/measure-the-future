from datetime import date

#Set the folder containing all the MtF data you want to visualize:
#(It is assumed that all subfolders of this folder are data for one scout)
MTF_PATH = None

#set the names of mtf_visualize notebooks to use
MTF_VISUALIZE_NAMES = ['mtf_visualize_7_time', 'mtf_visualize_5_heatmap', 'mtf_visualize_5_paths']

NUM_PATHS_TO_DISPLAY = 150

WEEKDAYS_TO_DISPLAY = [5, 6] #Monday is 0, Sunday is 6
DATE_RANGE = (date.min, date.max)
