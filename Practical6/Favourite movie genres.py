import matplotlib.pyplot as plt
# create a dictionary:movie
movie = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War':7}
# print the dictionary
print(movie)
# print the number of university students who prefer a movie genre taken from the input list.
print("Comedy:", movie['Comedy'])
# construct a pie chart
labels = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)
plt.show()
