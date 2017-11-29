from shutil import copyfile
from subprocess import call
import os
sourceDir = "/Volumes/NIKON D750/DCIM/112ND750/"
targetDir = "/Users/nickysemenza/Pictures/2017/11/28-4/"
#TRAILING SLASHSES!!!!!

selects = []
others = []

for file in os.listdir(sourceDir):
	print file
	st = os.stat(sourceDir+file)
	if(st.st_flags == 2):
		print("select detected!")
		selects.append(file)
		copyfile(sourceDir+file,targetDir+file)
		call(["exiftool", "-P", "-label=Winner", "-overwrite_original", targetDir+file])
	else:
		others.append(file)
	print("------")
print("processed "+str(len(selects))+" selects, updated labels")

for file in others:
	copyfile(sourceDir+file,targetDir+file)
print("copied "+str(len(others))+" others.")