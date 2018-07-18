import matplotlib.pyplot as plt
import csv
import numpy as np
import seaborn
import seaborn as sns

##Code to plot graph between different countires and number of drivers

csvfile = open('../Output_Csv/Country_And_Driver.csv', 'rb')
reader = csv.reader(csvfile)
row = reader.next()
xlabel = row[0]
ylabel = row[1]

Xdata = []
Ydata = []
for row in reader:
	Xdata.append(row[0])
	Ydata.append(row[1])
Ydata = [int(x) for x in Ydata]
print Xdata, Ydata


Xdata = Xdata[:17] + ['Others']
Ydata = Ydata[:17] + [sum(Ydata[17:])]
X = np.arange(len(Xdata))
print Xdata, Ydata
hue = X
seaborn.set_style('whitegrid')
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]


barplot = seaborn.barplot(X, Ydata, palette = sns.color_palette(flatui))
XDATA = ['Britain', 'America', 'Italy', 'France', 'Germany', 'Brazil','Argentina', 'Belgium', 'South Africa', 'Swiss','Japan', 'Dutch','Australia', 'Spain', 'Austria', 'Cannada', 'Sweden', 'Others']
#Others = ['Finland', 'New Zealand', 'Mexico', 'Denmark', 'Ireland', 'Rhodes', 'Uruguay', 'Portugal', 'Venezuela', 'Columbia', 'East Germany', 'Monaco', 'India', 'Argentina','Indonesia', 'Hungary', 'Thailand', 'Chile', 'Malaysia', 'Poland', 'Czech']

plt.xticks(np.arange(len(Xdata)),XDATA)
plt.title('#Of Drivers from Different Countries',fontsize = 16)
plt.yticks(np.arange(0, max(Ydata)+5,5), np.arange(0, max(Ydata)+5,5))
plt.xlabel('Driver country', fontsize = 16)
plt.ylabel('#Of Drivers', fontsize = 16)
barplot_fig = barplot.get_figure()
barplot_fig.set_size_inches(15.7, 11.2)
barplot_fig.savefig('../Plots/Proper_Ones/Drivers2.png', dpi = 1000, bbox_inches = 'tight')


