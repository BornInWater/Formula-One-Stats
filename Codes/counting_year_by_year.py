import csv
import numpy as np

##Code to create dictionaries containing driver/constructor ids from each of the countries for every year from 1950 to 2017 with an interval of 5 years.


Country_And_Driver = np.load('../Npy/country_and_driver_id.npy').tolist()
Country_And_Constructor = np.load('../Npy/country_and_constructor_id.npy').tolist()

Year_And_Races = np.load('../Npy/Year_Races_Ids.npy').tolist()
del Year_And_Races[2018]   #No valid entries for races of 2018

csvfile = open('../Data/results.csv', 'rb')
reader = csv.reader(csvfile, delimiter = ',')
Dict_Driver = {}
Dict_Constructor = {}
for key, val in Year_And_Races.iteritems():
	for year in range(val[0], val[1]+1):
		Dict_Driver[year] = []
		Dict_Constructor[year] = []
reader.next()
for row in reader:
	raceid = int(row[1])
	driverid = int(row[2])
	constructorid = int(row[3])
	Dict_Driver[raceid].append(driverid)
	Dict_Constructor[raceid].append(constructorid)

Union_Dict_Driver = {}
Union_Dict_Constructor = {}
i = 0
for key, _ in Year_And_Races.iteritems():
	if i %5 == 0:
		Union_Dict_Driver[key] = []	
		Union_Dict_Constructor[key] = []
	if i == len(Year_And_Races) - 1:
		Union_Dict_Driver[key] = []
		Union_Dict_Constructor[key] = []
	i = i+1
i = 0
for key,val in Year_And_Races.iteritems():
	if key in Union_Dict_Driver:
		add_year = key
	for raceid in range(val[0],val[1]+1):
		Union_Dict_Driver[add_year] += Dict_Driver[raceid]
		Union_Dict_Constructor[add_year] += Dict_Constructor[raceid]

for key,_ in Union_Dict_Driver.iteritems():
	Union_Dict_Driver[key] = list(set(Union_Dict_Driver[key]))
	Union_Dict_Constructor[key] = list(set(Union_Dict_Constructor[key]))

All_Driver_Combinations = {}
All_Constructor_Combinations = {}

for Key,Val in Country_And_Constructor.iteritems():
	All_Constructor_Combinations[Key] = {}
	for key,val in Union_Dict_Constructor.iteritems():
		All_Constructor_Combinations[Key][key] = []
		for num in Val:
			if int(num) in val:
				All_Constructor_Combinations[Key][key].append(num)


for Key,Val in Country_And_Driver.iteritems():
	All_Driver_Combinations[Key] = {}
	for key,val in Union_Dict_Driver.iteritems():
		All_Driver_Combinations[Key][key] = []
		for num in Val:
			if int(num) in val:
				All_Driver_Combinations[Key][key].append(num)

np.save('../Npy/All_Constructor_Combinations.npy',All_Constructor_Combinations)
np.save('../Npy/All_Driver_Combinations.npy',All_Driver_Combinations)
