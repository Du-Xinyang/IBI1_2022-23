import matplotlib.pyplot as plt
# create a dictionary:movie
movie = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War':7}
# print the dictionary
print(movie)
# create a variable that can be modified and print the number of university students who prefer a movie genre taken from the input list.
a = 'Comedy'
print(a,":", movie[a])
# construct a pie chart
labels = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.show()
