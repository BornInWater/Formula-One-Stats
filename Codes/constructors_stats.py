import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

##Code to create csv files containing number of constructors from different countries and an to create another csv file containing names of different constructors from their respective countries


def GetLen(elem):
	return len(Count_Constructor[elem])


csvfile = open('../Data/constructors.csv', 'rb')

reader = csv.reader(csvfile, delimiter = ',')

reader.next()

Count_Constructor = {}

for row in reader:
	Name = row[2]
	Country = row[3]
	if Country not in Count_Constructor:
		Count_Constructor[Country] = [Name]
	else:
		Count_Constructor[Country].append(Name)


Sorted_Count_Constructor = sorted(Count_Constructor, reverse = True,key=GetLen)
print(Sorted_Count_Constructor)

f = open('Country_And_Constructors.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Country', '#Of Constructors'])
for i in Sorted_Count_Constructor:
	writer.writerow([i, len(Count_Constructor[i])])

f.close()


f = open('Country_And_Constructor_Names.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Country', '#Of Constructors', 'Constructor Names'])
for i in Sorted_Count_Constructor:
	writer.writerow([i, len(Count_Constructor[i]), ' ,'.join(Count_Constructor[i])])
	
f.close()
