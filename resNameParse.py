import os
import sys
from collections import OrderedDict

##Author: Kwesi Daniel
#Parses replylog residue data from chimera to a standard format
#example:

# residue id #0:134 type ARG
# residue id #0:135 type GLY
# residue id #0:218 type GLN
# residue id #0:79 type GLY
# residue id #0:193 type GLY
# residue id #0:61 type SER
# residue id #0:194 type CYX
# residue id #0:132 type ARG

# to:

# #0  <the chimera file number (not chain)
# SER61 <parsed data
# GLY79
# GLY135
# CYX194
# ARG132
# GLN218
# GLY193
# ARG134



inputName = ""
outputName = ""

if(len(sys.argv) < 2):
	print("Input file not found!!")
	exit()
else:
	fileName = sys.argv[1]

if(len(sys.argv) < 3):
	print("Output file not found!!")
	exit()
else:
	outputName = sys.argv[2]
inputFile = open(fileName,'r')
residueData = inputFile.read()  #reads the entire file into the residueData 
inputFile.close()
residueData = residueData.split("\n")
residues = {}
for residue in residueData:
	if(residue.strip() == ""):
		continue
	temp = residue.split(" ")   # ex:   residue id #0:132 type ARG

	#This should be parsed to an int so that, for example 134 > 42 (a string would make 42 > 134)
	fileNum = temp[2].split(":")[0] #the file, such as file #0, #1, or #2 when opened in chimera. Will give sorting errors above 100
	resNum = int(temp[2].split(":")[1])
	resName = temp[-1];
	if(fileNum not in residues):
		residues[fileNum] = {}
	
	residues[fileNum][resNum] = resName


outputData = ""



for fileNum in residues:
	outputData += fileNum + "\n"
	residues[fileNum] = OrderedDict(sorted(residues[fileNum].items()))
	for key,val in residues[fileNum].items():
		outputData += val + str(key) + ","
		#print(k,v)
	# for res in residues[fileNum]:
	# 	outputData += residues[fileNum][res] + res + ","
	outputData = outputData[:-1] #deletes last character (a comma)
	outputData += "\n"
	

outputFile = open(outputName,'w')
outputFile.write(outputData)
outputFile.close()

