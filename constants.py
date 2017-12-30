import os
from datetime import date

#Set the folder containing all the MtF data you want to visualize:
#(It is assumed that all subfolders of this folder are data for one scout)
#currently set to a subfolder of the folder this file is in called "mtf_data"
MTF_PATH = os.path.dirname(os.path.realpath(__file__)) + os.sep + "mtf_data"

LOCALTZ = 'US/Eastern'

#if you want to load data from a specific date range, ignoring boundaries between datasets, using load_mtf_data.from_date_range
#boundary dates are inclusive
DATE_RANGE = (date(2017, 10, 17), date(2017, 10, 30))

#number of pixels on either side of MTF view frame where paths are not reliably detected
#left, top, right, bottom
MTF_DETECTION_PADDING = (30, 30, 30, 30)

BG_IMG_GREYSCALE = True

BG_IMG_SIZE = (1280, 720)
