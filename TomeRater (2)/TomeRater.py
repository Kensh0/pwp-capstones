#User Class: Creates basic information such as name and email
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}


    def get_email(self):
        return self.email


    def change_email(self, address):
        self.email = address
        return print("{user} email has been updated to {new_email}".format(user=self.name, new_email=self.email))


    def __repr__(self):
        return print("User {name}, email: {email}, books read: {numbooks}".format(name=self.name, email=self.email, numbooks=self.books))


    def __eq__(self, other_user):
        if (self.name == other_user.name) and (self.name == other_user.email):
            return True
        else:
            return False


    def read_book(self, book, rating=None):
        self.book = book
        self.rating = rating
        self.books.update({self.book: self.rating})


    def get_average_rating(self):
        total = 0
        number_of_books = 0
        average = total / number_of_books
        for ratings in self.books.values():
            if ratings >= 0:
                total += ratings
                number_of_books += 1
        return average


#Book Class: Creates books tracked by title, ISBN and a list of Ratings. Can also compare books to match title and ISBN
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []


    def get_title(self):
        return self.title


    def get_isbn(self):
        return self.isbn


    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return print("{title}: ISBN updated to {new_isbn}".format(title=self.title, new_isbn=self.isbn))


    def add_rating(self, rating):
        if (rating >= 0) and (rating <= 4):
            self.ratings.append(rating)
            return print("{rating} added successfully, thank you!".format(rating=rating))
        else:
            return print("Invalid Rating")


    def __eq__(self, other_book):
        if (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return print("{self} is the same book as {other_book}. Their title is {title} and their ISBN is {isbn}.".format(self=self.title, other_book=other_book.title, title=self.title, isbn=self.isbn))

        else:
            return print("{self} and {other_book} are different books. Their titles are {self}, {other_book} and their ISBN's are {self_isbn}, {other_isbn}.".format(self=self.title, other_book=other_book.title, self_isbn=self.isbn, other_isbn=other_book.isbn))


    def get_average_rating(self):
        number_of_ratings = 0
        total = 0
        average = total / number_of_ratings
        for rating in self.ratings:
            number_of_ratings += 1
            total += rating
        return average


    def __hash__(self):
        return hash((self.title, self.isbn))


#Subclass of Book: Fiction
class Fiction(Book):
    def __init__(self, title, author, isbn):
        self.title = title
        self.isbn = isbn
        self.author = author


    def get_author(self):
        return self.author


    def __repr__(self):
        return print("{title} by {author}".format(title=self.title, author=self.author))


#Subclass of Book: Non-Fiction
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.title = title
        self.isbn = isbn
        self.subject = subject
        self.level = level


    def get_subject(self):
        return self.subject


    def get_level(self):
        return self.level


    def __repr__(self):
        return print("{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject))


#Class TomeRater: Application that stores Users and Books
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}


    def create_book(self, title, isbn):
        self.title = title
        self.isbn = isbn
        return Book(self.title, self.isbn)


    def create_novel(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        return Fiction(self.title, self.author, self.isbn)


    def create_non_fiction(self, title, subject, level, isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn
        return Non_Fiction(self.title, self.subject, self.level, self.isbn)


    def add_book_to_user(self, book, email, rating=None):
        self.book = book
        self.email = email
        self.rating = rating
        key_to_check = self.users[self.email]

        if key_to_check not in self.users:
            print("No user with email {email}".format(email=self.email))
        else:
            user = self.users[self.email]
            user.read_book(self.book, self.rating)
            add_rating(self.book, self.rating)
            for books in self.books.keys():
                if books not in self.books.keys():
                    self.books[books] = 1
                else:
                    self.books[books] += 1


    def add_user(self, name, email, user_books=None):
        self.name = name
        self.email = email
        self.user_books = user_books
        User(self.name, self.email)
        self.users[self.email] = self.name
        if self.user_books != None:
            for book in self.user_books:
                self.add_book_to_user(book, self.email)


    def print_catalog(self):
        print(list(self.books))



    def print_users(self):
        for users in self.users.values():
            print(users)

    def print_users_email(self):
        print(self.users.keys())


    def most_read_book(self):
        most_read = 0
        most_book = None
        for key, value in self.books.items():
            if value >= most_read:
                most_read = value
                most_book = key
        return print(most_book)



    def highest_rated_book(self):
        highest_rating = 0
        highest_book = None
        for book in self.books.keys():
            average = book.get_average_rating()
            if average >= highest_rating:
                highest_rating = average
                highest_book = book
        return highest_book


    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for email, name in self.users.items():
            user = User(email, name)
            average = user.get_average_rating()
            if average >= highest_rating:
                highest_rating = average
                highest_user = name
        return highest_user
