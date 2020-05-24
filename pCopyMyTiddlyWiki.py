#!/usr/bin/env python3

# Directory where your original file is stored
# For example : /home/soandso/
# Do not forget to use / after the end
tw_dir = 'PATH_OF_YOUR_TIDDLY_WIKI_FILE/'

# Name of your TiddlyWiki file
# For example : myTiddlyWiki.html
tw_file = 'NAME_OF_YOUR_TIDDLY_WIKI_FILE'


# TiddlyWiki Download Directory. 
# For exemple  ~/Downloads/
# Do not forget to use / after the end
tw_download = 'YOUR_DEFAULT_DOWNLOAD_FOLDER/'

# flag to specify the days to maintain the downloaded_file: if day_maintain_downloaded_file is less than 0, the file will not be removed
day_maintain_downloaded_file = 2

import glob
import os
import os.path, time
from datetime import datetime
import shutil

def diff_days(d_recent, d_old):
	d1 = datetime.fromtimestamp(d_recent)
	d2 = datetime.fromtimestamp(d_old )

	return (d1-d2).days

print("Starting script "+str(datetime.now()))

tw_downloaded_files_name_pattern = tw_download+tw_file.split( '.')[0]+'*.'+tw_file.split( '.')[1]

mtime_tw_file = os.path.getmtime(tw_dir+tw_file)

tw_downloaded_files = glob.glob(tw_downloaded_files_name_pattern)
tw_downloaded_files.sort(key=os.path.getmtime, reverse=True)


for i in range(0, len(tw_downloaded_files)):
	mtime_downloaded_file = os.path.getmtime(tw_downloaded_files[i]) 		
		
	if (mtime_downloaded_file > mtime_tw_file):
		print("Modified time of the dowloaded file...: "+str(datetime.fromtimestamp(mtime_downloaded_file)))
		print("Modified time of the TW original file.: "+str(datetime.fromtimestamp(mtime_tw_file)))
		shutil.copyfile(tw_downloaded_files[i], tw_dir+tw_file)
		print("Copied file "+tw_downloaded_files[i]+" to "+tw_dir+tw_file);
		mtime_tw_file = os.path.getmtime(tw_dir+tw_file)

	if (day_maintain_downloaded_file >= 0):
		delta = diff_days( datetime.now().timestamp(), mtime_downloaded_file)
		if (delta > day_maintain_downloaded_file): 
			os.remove(tw_downloaded_files[i])
			print("File "+tw_downloaded_files[i]+" was removed - Date modified : "+str(datetime.fromtimestamp(mtime_downloaded_file)));

print("Script finished ")


