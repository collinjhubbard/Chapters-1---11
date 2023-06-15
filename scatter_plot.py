import matplotlib.pyplot as plot

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plot.style.use('fivethirtyeight')
fig, ax = plot.subplots()
ax.scatter(x_values, y_values, s=100)


#Set chart title and label axis
ax.set_title("Sqaure Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Sqaure of Value", fontsize=14)

#Set size of tick labels
ax.tick_params(axis='both', which='major',labelsize=14)

plot.show()