import csv
import matplotlib.pyplot as plot

filename = 'Pitching.csv'

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    #for index, column in enumerate(header_row):
    #    print(index, column)

    player, highs = [], []
    for row in reader:
        current_player = str(row[0])
        high = int(row[5])
        player.append(current_player)
        highs.append(high)

    plot.style.use('fivethirtyeight')
    fig, ax = plot.subplots()
    #ax.plot(player, highs, c='red')
    ax.scatter(player, highs, c=highs, cmap=plot.cm.Reds, s=10)

    #plot.title("Highest Strikeout Totals by Pitcher")
    #plot.xlabel("Pitcher", fontsize=16)
    #plot.ylabel('Strikeouts', fontsize=16)
    #plot.tick_params(axis="both", which='major', labelsize=16)
    ax.set_title("Highest Strikeout Totals by Pitcher", fontsize=16)
    ax.set_xlabel("Player", fontsize=12)
    ax.set_ylabel("Strikeouts", fontsize=16)
    ax.tick_params(axis="both", which='major', labelsize=14)

    plot.show()
