
import os
import json
from PIL import Image

from datetime import date, datetime
import pytz #time zone info

from constants import LOCALTZ, MTF_JSON_ENCODING

#----------
#private

def interaction_data(scout_subfolder_path):    
    interactions = None
    try:
        interactions_path = scout_subfolder_path + os.sep + "scout_interactions.json"
        assert(os.path.isfile(interactions_path))
        with open(interactions_path, 'r', encoding=MTF_JSON_ENCODING) as interactions_file:
            interactions = json.load(interactions_file)
    except Exception as e:
        print("Problem loading interaction data in " + scout_subfolder_path + "\n" + str(e))
        interactions = None
    finally:
        return interactions
    
def calibration_image(scout_subfolder_path, grayscale=True):
    im = None
    try:
        image_path = None
        for filename in os.listdir(scout_subfolder_path):
            if filename.endswith("jpg") and filename.startswith("scout"):
                image_path = scout_subfolder_path + os.sep + filename
        im = Image.open(image_path)
        if grayscale: im = im.convert('L')
    except Exception as e:
        print("Problem loading calibration image in " + scout_subfolder_path + "\n" + str(e))
    finally:
        return im
 
def parsed_set_date(set_subfolder_name):
    #set_subfolder_name should be of the form "[scoutname]_[MMDDYYYY]"
    try:
        datestr = folder_name.split("_")[1]
        date = datetime.strptime(datestr, "%m%d%Y").date()
    except:
        print("problem parsing date string in " + folder_name)
        date = date(10, 1, 1)
    finally:
        return date
        
def parsed_interaction_time(interaction_time_string):

    #parse the time string into a python datetime object
    dt = datetime.strptime(interaction_time_string, "%Y-%m-%dT%H:%M:%SZ")
    #mtf records timestamps in UTC, so we need to tell the datetime object to interpret the parsed dates at UTC
    dt = pytz.utc.localize(dt)
    #tell the datetime object to change time display to eastern
    dt = dt.astimezone(pytz.timezone(LOCALTZ))
    
    return dt
    
def parse_interaction_times(interactions):
    #replace string in "EnteredAt" field with a parsed datetime object in the local timezone.
    for i in interactions: i['EnteredAt'] = parsed_interaction_time(i['EnteredAt'])
    return interactions
    
# from https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
def deduplicate(list_of_jsons):
    #return [elem for n, elem in enumerate(list) if elem not in list[n + 1:]] 
    #return [dict(t) for t in set([tuple(d.items()) for d in list])]
    set_of_jsons = {json.dumps(d, sort_keys=True) for d in list_of_jsons}
    return [json.loads(t) for t in set_of_jsons]
 
#returns tuple of (interactions, calibration image) 
#entertimes returned in strings, not parsed into datetime objects
def from_set_private(scout_folder_path, set_subfolder_name):
    path = scout_folder_path + os.sep + set_subfolder_name
    if os.path.isdir(path): return (interaction_data(path), calibration_image(path))
    else: return (None, None)
 
#-------------------
#public
 
def from_set(scout_folder_path, set_subfolder_name):
    (interactions, im) = from_set_private(scout_folder_path, set_subfolder_name)
    return (parse_interaction_times(interactions), im)
 
#returns tuple of (interactions, calibration image, set subfolder name)
def from_most_recent_set(scout_folder_path):
    
    #iterate through subfolders, sorted by parsed date from most recent to oldest
    for set_subfolder_name in sorted(os.listdir(scout_folder_path), key=parsed_set_date, reverse=True):
        (interactions, im) = from_set_private(scout_folder_path, set_subfolder_name)
        if interactions != None and im != None:
            return (interactions, im, set_subfolder_name)
    print("No usable set subfolders in " + scout_folder_path + "\n")
    return (None, None, None) 
 
#the calibration image returned from the following methods is a bit tricky.=
#combining data with different calibration images can be dubious if the images
#are angled differently to a signifigant degree (which is very possible).
#so using the following options assumes that either:
#   a) the calibration image won't be used (such as in the case of time charts)
#   b) the user has already looked through the images manually and confirmed
#       that they are all sufficiently similar in angle for the data to
#       match up reasonably. 
#
#additionally, in the case of b) the user should select the "best" calibration
#image (the sharpest and most free of people and temoprary objects and 
#put a copy of it in the scout's folder (the main folder, not a set subfolder).
#if an image exists there, these functions will return it as the overall calibration
#image to display as background. if not, an arbitrary one will be selected.
 
#returns tuple of (interactions, calibration image)    
def combined_from_sets(scout_folder_path, set_subfolder_names):
    im_overall = None
    im_overall = calibration_image(scout_folder_path)
    
    interactions_all = []
    for set_subfolder_name in set_subfolder_names:
        (interactions, im) = from_set_private(scout_folder_path, set_subfolder_name)
        if interactions != None: interactions_all = interactions_all + interactions
        if im_overall == None: im_overall = im
        
    return (parse_interaction_times(deduplicate(interactions_all)), im_overall) 
    #dedupe interactions_all in case data was not cleared between collecting datasets
 
#returns tuple of (interactions, calibration image)    
def combined_from_all_sets(scout_folder_path):
    return combined_from_sets(scout_folder_path, os.listdir(scout_folder_path))
    
#returns tuple of (interactions, calibration image)    
#min_date and max_date should be datetime objects
#weeksdays to include should be a list of numbers between 1 and 7 
def from_date_range(scout_folder_path, date_range, weekdays_to_include=range(7)):
    (interactions, im) = combined_from_all_sets(scout_folder_path)
    
    clipped_interactions = []
    for i in interactions:
        dt = i['EnteredAt']
        if dt.weekday() in weekdays_to_include and date_range[0] <= dt.date() <= date_range[1]:
            clipped_interactions.append(i)
            
    return (clipped_interactions, im)
    
    '''
    relevant_sets = []
    #iterate through subfolders, sorted by parsed date from oldest to most recent
    for set_subfolder_name in sorted(os.listdir(scout_folder_path), key=parsed_set_date):
        if parsed_set_date(set_subfolder_name)
        
        (interactions, im) = from_set_private(scout_folder_path, set_subfolder_name)
        if interactions != None and im != None:
            return (interactions, im, set_subfolder_name)
    print("No usable set subfolders in " + scout_folder_path + "\n")
    return (None, None, None) 
    '''
            