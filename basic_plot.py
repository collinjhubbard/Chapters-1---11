import matplotlib.pyplot as plot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plot.style.use('fivethirtyeight')
figure, ax = plot.subplots()
ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axis
#ax.set_title("Sqaure Numbers", fontsize=24)
#ax.set_xlabel("Value", fontsize=14)
#ax.set_ylabel("Sqaure of Value", fontsize=14)

#Set size of tick labels
#ax.tick_params(axis='both', labelsize=14)

plot.show()