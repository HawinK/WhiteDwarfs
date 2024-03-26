import numpy as np
import matplotlib.pyplot as plt

# first we load the data
# there are many ways to do this but this is one of them
d = np.loadtxt('fake_table.dat',skiprows=2)
#"skiprows" tells python how many lines (that are not commented out) to ignore

# now we can load the different columns, python starts counting from zero 
X = d[:,0] # first column
Y = d[:,1] # second column
YERR = d[:,2] # third column

# now that we loaded the data, we can plot!

# here we set the size of the plot, you can change to whatever is best
fig = plt.figure(figsize=(7,6))

# we can plot things as a scatter plot or as a regular plot
# plotting points with errorbars, to showcase I shifted Y values by 2
plt.errorbar(X,Y+2,marker='s',markersize=15,yerr=YERR,capsize=5,elinewidth=0.7,color='#c0c0c0',ls=':',label='Error bar')
# capsize = size of error bar cap
# elinewidth = width of error bar lines
# color = can be a string such as 'black' or a hexadecimal color like '#707070'
# ls = line style (for example: '-', '--', ':')
# marker = shape of marker (for example: 'd', 's', 'D', '.', 'o', 'x', '+')
# label = what will show up in the legend if you decide to put one in

# scatter plot example
plt.scatter(X,Y,marker='o',s=100,color='dodgerblue',label='Scatter',zorder=100)
# the same result can be found by using
#plt.plot(X,Y,marker='o',color='dodgerblue',markersize=15,ls='none')

# zorder = optional keyword that is to set which element is plotted "on top", can take any value
# s = marker size

# legend, loc specifices location (1,2,3,4)
plt.legend(loc=1,fontsize='x-large')

# title if you wanted
plt.title('Title of fake plot!',size=16)

# if you want to set specific ax limits
plt.xlim(0,9)
plt.ylim(0.23)

# if you wanted to change the axes to be in a log scale (it will look ugly with this data)
#plt.xscale('log')
#plt.yscale('log')

# setting axes
plt.xlabel('X [fake example]',size=16)
plt.ylabel('Y [fake example]',size=16)
# setting size of ticks
plt.xticks(size=14)
plt.yticks(size=14)

plt.tight_layout() ## this makes things fit nicely in the window
plt.savefig('fake_plot.png') # or ".pdf", ".jpg", for example
#plt.show() # to show the plot as an interactive pop-up window 
plt.clf() # cleans the frame, needed if you then plot something else
