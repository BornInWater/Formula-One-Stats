import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

##Code to create csv files containing number of drivers from different countries and an to create another csv file containing names of different drivers from their respective countries



def GetLen(elem):
	return len(Count_Driver[elem])

csvfile = open('../Data/drivers.csv', 'rb')

reader = csv.reader(csvfile, delimiter = ',')

reader.next()

Count_Driver = {}

for row in reader:
	Name = row[4] +' ' +row[5] #first name + surname
	Country = row[7]
	if Country not in Count_Driver:
		Count_Driver[Country] = [Name]
	else:
		Count_Driver[Country].append(Name)


Sorted_Count_Driver = sorted(Count_Driver, reverse = True,key=GetLen)
print(Sorted_Count_Driver)

f = open('Country_And_Driver.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Country', '#Of Drivers'])
for i in Sorted_Count_Driver:
	writer.writerow([i, len(Count_Driver[i])])

f.close()


f = open('Country_And_Driver_Names.csv', 'w')
writer = csv.writer(f)
writer.writerow(['Country', '#Of Drivers', 'Driver Names'])
for i in Sorted_Count_Driver:
	writer.writerow([i, len(Count_Driver[i]), ' ,'.join(Count_Driver[i])])

f.close()
