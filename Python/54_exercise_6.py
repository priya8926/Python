class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addBook(self , book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def show(self):
        print(f"The laibrary has {self.nobooks} books.  The book are : ")
        for book in self.books:
            print(book)

l1 = library()
l1.addBook("Harry potter1 ")
l1.addBook("Harry potter2 ")
l1.addBook("Harry potter3 ")
l1.show()