import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id": str})
df_card = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_secure = pd.read_csv('card_security.csv', dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = str(hotel_id)
        self.hotel_name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        """Book hotel and mark hotel as unavailable"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Return boolean whether hotel is available for booking"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        print(availability)
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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, date, cvc, holder):
        card_info = {"number": self.number, "expiration": date,
                     "cvc": cvc, "holder": holder}
        if card_info in df_card:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_secure.loc[df_secure['number'] == self.number, 'password'].squeeze()
        print(password)
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_ID = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_ID)
creditcard = SecureCreditCard(number="1234")
if creditcard.validate(date="12/26", cvc="123", holder="JOHN SMITH"):
    if creditcard.authenticate(given_password='mypass'):
        if hotel.available():
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = Reservation(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Hotel is not available to book.")
else:
    print("Credit card is not valid")