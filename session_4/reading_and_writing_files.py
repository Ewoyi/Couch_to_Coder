# import csv

# open an array (list)
# books = []

# open a file
# with open("bestsellers with categories.csv", "r") as csv_file:
#     print(csv_file)


# import csv

# books = []

# with open("bestsellers with categories.csv", "r") as csv_file:
# # inspect the csv file
# # how the csv package works
# # some csv packages needs to be imported manually
#     reader = csv.reader(csv_file, skipinitialspace=True)
    # next(reader) # Jump over to the next interchange
#     for row in reader:
#         # create a dictionary that represent thet book
#         new_book = {}
#         new_book["name"] = row[0]
#         new_book["author"] = row[1]
#         new_book["user rating"] = row[2]
#         new_book["reviews"] = row[3]
#         new_book["price"] = row[4]
#         new_book["year"] = row[5]
#         new_book["genre"] = row[6]
#         books.append(new_book)
# print(books)


import csv
from collections import namedtuple

Book = namedtuple("Books", "name author user_rating reviews price year genre")
books = []

with open("bestsellers with categories.csv", "r") as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    next(reader)
    for row in reader:
        new_book = Book(*row) # identical with the line of code above
        books.append(new_book)
# print(book[0].user_rating)


# import csv
# from collections import namedtuple

# Book = namedtuple("Book ", "name author user_rating reviews price year genre")

# with open("bestsellers with categories.csv", "r") as csv_file:
#     reader = csv.reader(csv_file, skipinitialspace=True)
#     next(reader)
    
#     books = [Book(*row) for row in reader]
# # print(books[0].author)

# TASKS
# Create a list with all of the bestsellers from 2009 to 2012!
# How expensive is the most expensive book?
# Create a list with all books whose author has the first name George!


# Create a list with all of the bestsellers from 2009 to 2012!

# filtered_bestsellers = []
# for book in books:
#     if int(book.year)  >= 2009 and int(book.year) <= 2012:
#         filtered_bestsellers.append(book)
# print(len(filtered_bestsellers))

# How expensive is the most expensive book?

# most_expensive_book = books[0]
# for book in books:
#     if(int(book.price) > int(most_expensive_book.price)):
#         most_expensive_book = book
# print(most_expensive_book)

# Create a list with all books whose author has the first name George!
# Geroge_books = []
# for book in books:
#     if("George" in book.author):
#         Geroge_books.append(book)
# print(Geroge_books)

# how to write to a separate csv file
# how top read info in a csv file and write on a separate csv file

modified_books = []
for book in books:
    british_price_book = Book(
        book.name,
        book.author, 
        book.user_rating, 
        book.reviews, 
        float(book.price) * 0.79, 
        book.year, 
        book.genre
        )
    modified_books.append(british_price_book)
print(len(modified_books))

with open("bestsellers_british_price.csv", "w") as british_csv_file:
    writer = csv.writer(british_csv_file, quoting=csv.QUOTE_ALL)
    writer.writerow(Book("name", "author", "User Rating", "reviews", "price", "year", "genre"))
    for book in books:
        writer.writerow(book)