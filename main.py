import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        """Book hotel and mark hotel as unavailable"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Return boolean whether hotel is available for booking"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    def generate(self):
        content = f"""
        Booking confirmed for {self.customer_name} to hotel {self.hotel_object.hotel_name}
        """
        return content


print(df)
hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = Reservation(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available to book.")