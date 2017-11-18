"# measure-the-future" 

# Measure the Future - Visualizations
#### Overview
Measure the Future involves placement of fixed cameras, called scouts, that track movements through public places.  We want to visualize the data collected by scouts in order to draw meaningful conclusions about where people tend to go, when they go there, and the paths they take to get there.

For more informaiton on Measure the Future, see http://measurethefuture.net/ and [Measure the Future's Github Account](https://github.com/MeasureTheFuture)

#### Format MtF data should be in before using this notebook
Each scout should have a folder containing data recorded by that scout.  The name of the folder should be the name of that scout, for example "Main 1 - LobbyHall".

A scout's folder should have several subfolders containing data from different ranges of dates.  The names of these folders should be of the form:
* \[shotened scout name]\_\[end date of range in the form MMDDYYYY]

Each of these subfolders should contain a jpeg calibration image, and four json files: scout_interactions, scout_summaries, scouts, and scout_healths. 

#### Calibration image
Filename should be of the form:
* scout-\[anything can go here].jpg

This shows the view the scout sees during the date range of the subfolder it's in.  The reason there is a separete calibration image for each subfolder is that getting the data out of the scout and deleting it in preparation from more data collection involves touching the scout.  Doing so may move the scout slightly, so it must be recalibrated after.  Thus, the calibration images will not always be identical for different date ranges.

#### scout_interactions.json
Each "interaction" represents one person's path across the scout's frame of view.  An interaction is represented by a list of waypoints, represented by 2d coordinates on the calibration image.  

In addition, interactions are recorded with a duration (in seconds), an enter time (in UTC), a series of waypoint times (in seconds after the enter time), and a series of waypoint widths (representing the recorded width and height of the person at each waypoint).

#### Visualiztion Notebooks
There should be a set of notebooks (stored in the same folder as this one), each of which does one particular visualization on one particular scout.  You can choose which of these notebooks to run, and each one you choose will be run on every scout.  Their names sould be of the form:
* MTF\_visualize\_\[name].ipynb

Some notebooks only do visualizations on the most recent date range subfolder for a scout.  Others combine the data across all date ranges.

You shouldn't need to touch these unless you want to change something about the visualizations they do.  If you simply want to run them on your own data, you need only change parameters in main.ipynb.

#### main.ipynb
This notebook runs a set of visualization notebooks on all scouts in a given folder.  The folder containing the scout data, and the set of notbooks to run, can both be specified as parameters in main.

#### load_mtf_data.py
A python script imported by all the visualization notebooks that takes care of importing MtF data.  You shouldn't need to touch this.
