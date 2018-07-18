import matplotlib.pyplot as plt
import csv
import numpy as np
import seaborn
import seaborn as sns

##code to plot graph between different countries and number of constructors


csvfile = open('../Output_Csv/Country_And_Constructors.csv', 'rb')
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
Xdata = Xdata[:12] + ['Others']
Ydata = Ydata[:12] + [sum(Ydata[12:])]
X = np.arange(len(Xdata))

hue = X
seaborn.set_style('whitegrid')
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
barplot = seaborn.barplot(X, Ydata, palette = sns.color_palette(flatui))
XDATA = ['Britain', 'America', 'Italy', 'France', 'Germany', 'Japan', 'Swiss', 'Dutch', 'South Africa', 'Russia', 'Cannada', 'Malaysia', 'Others']
#Others = ['India', 'Brazil', 'Australia', 'Rhodes', 'East Germany', 'Hong Kong', 'Ireland','Belgium', 'New Zealand', 'Mexico', 'Spain', 'Austria']

plt.title('#Of Constructors from Different Countries', fontsize = 16)
plt.xticks(np.arange(len(Xdata)),XDATA)
plt.yticks(np.arange(0, max(Ydata)+5,5), np.arange(0, max(Ydata)+5,5))
plt.xlabel('Constructor country', fontsize = 16)
plt.ylabel('#Of Constructors', fontsize = 16)
barplot_fig = barplot.get_figure()
barplot_fig.set_size_inches(11.7, 8.27)
barplot_fig.savefig('../Plots/Proper_Ones/Constructors.png', dpi = 1000, bbox_inches = 'tight')


