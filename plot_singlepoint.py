import matplotlib.pyplot as plot

plot.style.use('fivethirtyeight')
fig, ax = plot.subplots()
ax.scatter(2,4,s=200)

#Set chart title and label axis
ax.set_title("Sqaure Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major',labelsize=14)

plot.show()
