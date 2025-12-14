class BOOK:
    def __init__(self, title, author, date, number=0):
        self.title = title
        self.author = author
        self.date = date
        self.number = number    

    def bookissue(self, issue):
        self.number += issue

    def bookreturned(self, number):
        self.number -= number   

    def show_details(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Issue Date:", self.date)
        print("Books Remaining to return:", self.number)


b = BOOK("God of War", "Napoleon", "25 Sep 2025")

b.bookissue(1)
b.bookreturned(0)

b.show_details()
