class Library:
    def __init__(self):
        self.books = []

#def __getitem__(self, key) takes this format.
    def __getitem__(self, index):
        return self.books[index]

    def add_books(self, books):
        return self.books.append(books)
    
my_Library = ["Things fall apart","A thousand splendid suns" ]
my_Library.add_books("The Secret Lives of Baba Segi's Wives")

for books in my_Library:
    print (books)

print(my_Library)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
  #you dont need return len() as it will be a number so no need to return a number again
    def __len__(self):
        return self.pages


    #isinstance()function that checks whether an object or variable is an instance of a specified type or class
    def __eq__(self, other):
        if isinstance(other, Book):
            if other.title == self.title and self.author == other.author:
                return True
        return False
    
book1 = Book("Things fall apart", "Chinua Achebe")
book2 = Book("A thousand splandid suns", "Housseini")
book3 = Book("Things fall apart", "Chinua Achebe")

print f"The title and the Author are equal: {book1 is book3}"

#A closure is simply a function inside another function, where the inner function remembers variables from
#the outer function even after the outer function has finished running.

def permission_check(required_role):
   def wrapper(self):
   if self.user_role == required_role:
       print f"Access granted"
    else:
       print f"Access denied"


def track_access (func):

#A decorator is a function that wraps around another function to add extra behaviour to it 
# without changing the original function.