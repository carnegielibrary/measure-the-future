
import os
import json
from PIL import Image
from datetime import datetime

def load_interaction_data(scout_subfolder_path):    
    interactions_path = scout_subfolder_path + os.sep + "scout_interactions.json"
    interactions = None
    try:
        assert(os.path.isfile(interactions_path))
        with open(interactions_path, 'r') as interactions_file:
            interactions = json.load(interactions_file)
    except Exception:
        print("Problem loading interaction data in " + scout_subfolder_path + "\n")
    finally:
        return interactions
    
def load_calibration_image(scout_subfolder_path, grayscale=True):
    im = None
    try:
        for filename in os.listdir(scout_subfolder_path):
            if filename.endswith("jpg") and filename.startswith("scout"):
                image_path = scout_subfolder_path + os.sep + filename
        im = Image.open(image_path)
        if grayscale: im = im.convert('L')
    except Exception as e:
        print("Problem loading calibration image in " + scout_subfolder_path + "\n" + str(e))
    finally:
        return im
    
def combine_interaction_data_from_subfolders(scout_folder_path):
    interactions = []
    for filename in os.listdir(scout_folder_path):
        scout_subfolder_path = scout_folder_path + os.sep + filename
        if os.path.isdir(scout_subfolder_path):
            next_interaction_set = load_interaction_data(scout_subfolder_path)
            if next_interaction_set != None: interactions = interactions + next_interaction_set
    return interactions

def sort_key(folder_name):
    #folder should be of the form scoutname_date
    #where date is MMDDYYYY
    try:
        datestr = folder_name.split("_")[1]
        date = datetime.strptime(datestr, "%m%d%Y")
    except:
        print("problem parsing date string in " + folder_name)
        date = datetime(10, 1, 1)
    finally:
        return date
    
#returns tuple of (interactions, calibration image, subfolder name)
def from_most_recent_subfolder(scout_folder_path):
    
    #iterated through subfolders, sorted by parsed date from most recent to oldest
    for filename in sorted(os.listdir(scout_folder_path), key=sort_key, reverse=True):
        scout_subfolder_path = scout_folder_path + os.sep + filename
        if os.path.isdir(scout_subfolder_path):
            interactions = load_interaction_data(scout_subfolder_path)
            im = load_calibration_image(scout_subfolder_path)
            if interactions != None and im != None:
                return (interactions, im, filename)
    print("No usable subfolders in " + scout_folder_path + "\n")
    return (None, None)