class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return self.name + " (" + self.email + ")"


class Member(Person):
    def __init__(self, member_id, name, email):
        super().__init__(name, email)
        self.member_id = member_id
        self.loans = []


class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        if self.available:
            status = "Available"
        else:
            status = "On loan"
        return self.title + " by " + self.author + " - " + status


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.is_active = True

    def return_book(self):
        if not self.is_active:
            raise ValueError("This book has already been returned.")
        self.is_active = False
        self.book.available = True


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, isbn, member_id):
        book = self.find_book(isbn)
        member = self.find_member(member_id)

        if book is None:
            raise ValueError("Book not found.")
        if member is None:
            raise ValueError("Member not found.")
        if not book.available:
            raise ValueError("This book is already on loan.")

        loan = Loan(book, member)
        book.available = False
        member.loans.append(loan)
        self.loans.append(loan)
        return loan

    def return_book(self, isbn, member_id):
        for loan in self.loans:
            if (
                loan.book.isbn == isbn
                and loan.member.member_id == member_id
                and loan.is_active
            ):
                loan.return_book()
                return loan

        raise ValueError("No active loan was found for this book and member.")

    def list_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book)
        return available_books


if __name__ == "__main__":
    library = Library("Community Library")

    first_book = Book("978", "Fluent Python", "Luciano Ramalho")
    second_book = Book("977", "Learning Python", "Mark Lutz")
    member = Member("M001", "Alex Taylor", "alex@example.com")

    library.add_book(first_book)
    library.add_book(second_book)
    library.add_member(member)

    loan = library.borrow_book("977", "M001")
    print(member.name + " borrowed " + loan.book.title)
    print("Available books:")
    for book in library.list_available_books():
        print(book.display_info())

    library.return_book("977", "M001")
    print("After the return:")
    for book in library.list_available_books():
        print(book.display_info())
