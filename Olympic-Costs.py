import matplotlib.pyplot as plt
# create a list
costs = [1, 8, 15, 7, 5, 14, 43, 40]
# print the list
print(costs)
# draw a bar plot
fig, ax = plt.subplots()

OlympicGames = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing2008', 'London 2012']
counts = [1,8,15,7,5,14,43,40]
bar_labels = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing2008', 'London 2012']
bar_colors = ['tab:pink', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:blue', 'tab:cyan', 'tab:green', 'tab:blue']

ax.bar(OlympicGames, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('costs')
ax.set_title('Olympic Games')
ax.legend(title='bar colors')

plt.show()