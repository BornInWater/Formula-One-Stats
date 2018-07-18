import csv
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import codecs


##Code to create a dictionary containing lists of race ids from each year

csvfile = open('../Data/races.csv', 'rb')
reader = csv.reader(csvfile, delimiter = ',')

Dict = {}
reader.next()
try:
	for row in reader:
		if int(row[1]) not in Dict:
			Dict[int(row[1])] = [int(row[0])]
		else:
			Dict[int(row[1])].append(int(row[0]))
except:
	pass
print('We have had %d years of formula 1 racing'%(len(Dict)))

Refined_Dict = {}
for Key, Var in Dict.iteritems():
	Max = max(Var)
	Min = min(Var)
	Refined_Dict[Key] = [Min, Max]

print(Refined_Dict)
np.save('../Npy/Year_Races_Ids.npy',Refined_Dict)
