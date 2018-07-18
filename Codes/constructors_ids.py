import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio


##Code to create a dictionary of team ids belonging to different countries

csvfile = open('../Data/constructors.csv', 'rb')

reader = csv.reader(csvfile, delimiter = ',')

reader.next()

Count_Driver = {}

for row in reader:
	id = row[0]
	Country = row[3]
	if Country not in Count_Driver:
		Count_Driver[Country] = [id]
	else:
		Count_Driver[Country].append(id)

np.save('../Npy/country_and_constructor_id.npy',Count_Driver)
