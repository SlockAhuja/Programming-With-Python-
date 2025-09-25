# AHuja Slock

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ₹{self.price:.2f}")
        print("-" * 30)

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount


# (a) Create two objects and display their details
book1 = Book("Python Programming", "Guido van Rossum", 500)
book2 = Book("Learning AI", "Andrew Ng", 800)

print("=== Book Details Before Discount ===")
book1.display_details()
book2.display_details()

# (b) Apply 10% discount to one of the books
print("Applying 10% discount to Book 2...\n")
book2.apply_discount(10)

print("=== Book Details After Discount ===")
book1.display_details()
book2.display_details()
