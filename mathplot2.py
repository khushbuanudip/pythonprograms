import matplotlib.pyplot as plt
genres = ["Mystery", "Romance", "Science Fiction", "Fantasy", "Thriller"]
books_sold = [120, 90, 80, 110, 70]
plt.bar(genres, books_sold)
plt.xlabel("Genre")
plt.ylabel("Number of Books Sold")
plt.title("Books Sold by Genre Over a Year")
plt.show()
