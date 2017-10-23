import sys

#Finds data in a 2 column list of residue numbers and bfactors

if(len(sys.argv) < 4): #includes the name of this python script, input file, output file, and max value
	print('Please input inputfile, output file, and the maximum bfactor (non-inclusive)')
else:
	inputFile = open(sys.argv[1],'r')
	output = open(sys.argv[2],'w')
	maximum = float(sys.argv[3])
	for line in inputFile:
		if('#' in line): #the line is a comment
			continue;
		else:
			line = line.strip()
			data = line.split("   ")
			residue = data[0]
			bfactor = data[1]
			if(float(bfactor) < maximum):
				output.write(residue + '\t' + bfactor + '\n')

	inputFile.close()
	output.close()


