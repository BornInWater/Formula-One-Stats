import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

##Code to plot graph for number of drivers from 6 countiries between 1950 and 2017

data = np.load('../Npy/All_Driver_Combinations.npy').tolist()
Britain = data['British']
America = data['American']
Italy = data['Italian']
France = data['French']
Germany = data['German']
Brazil = data['Brazilian']

Names = ['Britain', 'America', 'Italy', 'France', 'Germany', 'Brazil']
Countries = [Britain, America, Italy, France,Germany, Brazil]

Countries_Dict = {}
sns.set_style('whitegrid')
for i in range(len(Countries)):
	Countries_Dict[Names[i]] = {}
	for key, val in Countries[i].iteritems():
		Countries_Dict[Names[i]][key] = len(Countries[i][key])
	
	Years = sorted(Countries[i])
	Values = []
	print Years
	print Countries_Dict[Names[i]]
	for j in range(len(Years)):
		#Values.append(Countries[i][Years[j]])
		Values.append(Countries_Dict[Names[i]][Years[j]])
	plt.title('#Of Drivers from %s over the years'%(Names[i]))
	plt.ylabel('#Of Drivers', fontsize = 16)
	plt.xlabel('#Years', fontsize = 16)

	plt.yticks(np.arange(0,max(Values)+4,4), np.arange(0,max(Values)+4,4))
	ax = sns.pointplot(Years, Values, color = 'black')
	ax.grid(True)
	plot_fig = ax.get_figure()
	plot_fig.set_size_inches(7.7, 5.46)
	plot_fig.savefig('../Plots/%s_Drivers.png'%(Names[i]), dpi = 1000, bbox_inches = 'tight') 

	plt.clf()



