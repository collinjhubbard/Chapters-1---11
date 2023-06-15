import matplotlib.pyplot as plot

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plot.style.use('fivethirtyeight')
fig, ax = plot.subplots()
#ax.scatter(x_values, y_values, s=10)
#ax.scatter(x_values, y_values,c='red', s=10)
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
ax.scatter(x_values, y_values,c=y_values, cmap=plot.cm.Blues, s=10)

#Set chart title and label axis
ax.set_title("Sqaure Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major',labelsize=14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1100000])


#plot.show()
plot.savefig('squares_polt.png', bbox_inches='tight')