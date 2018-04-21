# Measure the Future - Visualizations
#### Overview
Measure the Future involves placement of fixed cameras, called scouts, that track movements through public places.  We want to visualize the data collected by scouts in order to draw meaningful conclusions about where people tend to go, when they go there, and the paths they take to get there.

For more informaiton on Measure the Future, see http://measurethefuture.net/ and [Measure the Future's Github Account](https://github.com/MeasureTheFuture)

#### Dependencies
Jupyter Notebook - https://github.com/merrittkowaleski/notebook

PIL - https://github.com/merrittkowaleski/Pillow

pytz - https://github.com/merrittkowaleski/pytz

nbformat - https://github.com/merrittkowaleski/nbformat

nbparameterise - https://github.com/merrittkowaleski/nbparameterise

numpy - https://github.com/merrittkowaleski/numpy 

Matplotlib - https://github.com/merrittkowaleski/matplotlib

#### Format MtF data should be in before using this notebook
Each scout should have a folder containing data recorded by that scout.  The name of the folder should be the name of that scout as you wish it to be displayed in the visualizations, for example "Main 1 - LobbyHall".

A scout's folder should have several subfolders containing data from different ranges of dates.  The names of these folders should be of the form:
* \[shortened scout name]\_\[end date of range in the form MMDDYYYY]

Each of these subfolders should contain a jpeg calibration image, and four json files: scout_interactions, scout_summaries, scouts, and scout_healths.  For these visualizations, only scout_interactions and the calibration image are used.

#### Calibration image
Filename should be of the form:
* scout-\[anything can go here].jpg

This shows the view the scout sees during the date range of the subfolder it's in.  The reason there is a separete calibration image for each subfolder is that getting the data out of the scout and deleting it in preparation from more data collection involves touching the scout.  Doing so may move the scout slightly, so it must be recalibrated.  Thus, the calibration images will not always be identical for different date ranges.

These visualizations can be used to combine data from multiple date range subfolders of one scout.  If you do this, it is best to manually check the calibration images to make sure they are similar enough as to be negligible for the purpose of visualization.  If not, you will need to manually transform the image and the interaction data for non-conforming subfolders.

Additionally, you may select the "best" calibration image (the sharpest and most free of people and temoprary objects) and put a copy of it in the scout's folder (the main folder, not a date range subfolder).  If an image exists there, it will be chosen as the image to display on multi-date range visualizations. if not, an arbitrary one will be selected.

#### scout_interactions.json
Each "interaction" represents one person's path across the scout's frame of view.  An interaction is represented by a list of waypoints, represented by 2d coordinates on the calibration image.  

In addition, interactions are recorded with a duration (in seconds), an enter time (in UTC), a series of waypoint times (in seconds after the enter time), and a series of waypoint widths (representing the recorded width and height of the person at each waypoint).

#### main.ipynb
This notebook runs a set of visualization notebooks on a set of scouts.  It should be stored in the same folder as all the visualization notebooks you plan to run.

Which notebooks to run, and which scouts to run them on, can be set in constants.py

#### check_data.ipynb
A short notebook to use to quickly tell you which data is missing in your set, and find the date ranges represented in each scout.

#### Visualiztion Notebooks
There should be a set of notebooks (stored in the same folder a main.ipynb), each of which does one particular visualization on one particular scout.  Their names sould be of the form:
* MTF\_visualize\_\[name].ipynb

#### constants.py
Miscellaneous constants used by multiple programs.

#### load_mtf_data.py
A python script used by all the visualization notebooks that takes care of importing MtF data into a nice format.
