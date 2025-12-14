class Movie:
    def __init__(self,name,ticketprice,showtime):
        self.name = name
        self.ticketprice = ticketprice
        self.showtime = showtime
    def show_details(self):
        print("Movie Name:",self.name)
        print("Ticket Price",self.ticketprice)
        print("showtime",self.showtime)
b =Movie("dhurandhar",280,"10 AM")
b.show_details()