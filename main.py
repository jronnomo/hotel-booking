import pandas as pd

df = pd.read_csv('hotels.csv')


class Hotel:
    def __init__(self, id):
        pass

    def book(self):
        pass

    def available(self):
        pass

class Reservation:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass


print(df)
id = input("Enter the ID of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name")
    reservation_ticket = Reservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available to book.")