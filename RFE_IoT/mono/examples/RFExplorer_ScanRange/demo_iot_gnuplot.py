#!/usr/bin/env python
#
# RF Explorer ScanRange display script
#
# Automatic display of latest captured CSV file spectrum on screen
#
#Example for python 3.5 - use as "python3 demo_iot_gnuplot.py" from command line
#Files with data are expected to be localed in csv folder, off current folder. You can easily change that in code below
#It requires gnuplot installed, just by doing "sudo apt-get install gnuplot" in your system
#You can change display parameters in file gnuplot_params

import os, sys, time, shutil, subprocess, glob

#we repeat this forever, but can be easily changed to limit to a subset of cases
while(True):

    list_csv=os.listdir("./csv")
    #list all files to delete those older than 10 minutes, so HD space remains limited
    #It will do this only if more than 20 files are found
    if (len(list_csv)>20):
        for file_csv in os.listdir("./csv"):
            if ((file_csv.lower().find(".csv")>0) and (os.stat("csv/"+file_csv).st_mtime < time.time() - 600)):
                print("removing old file " + file_csv)
                os.remove("csv/" + file_csv)

    #Get the newest file
    list_of_files = glob.glob('csv/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    #format gnuplot command
    sCommand="gnuplot -e \"filename='" + latest_file + "'\" gnuplot_params"
    print(sCommand)

    #call gnuplot
    subprocess.call(sCommand, shell=True)
