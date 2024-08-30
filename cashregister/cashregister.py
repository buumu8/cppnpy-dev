first_price = float(input("Enter price of the first item: "))
second_price = float(input("Enter price of the second item: "))
club_card = input("Does customer have a club card? (Y/N): ")
tax_rate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))

base_price = first_price + second_price
print("Base price = %2.2f" % (round(base_price, 2)))

price_after_discount = base_price

if first_price > second_price:
    price_after_discount = first_price + second_price / 2
else:
    price_after_discount = second_price + first_price / 2

if club_card == "Y" or club_card == "y":
    price_after_discount = price_after_discount * 0.9

print("Price after discounts = %2.2f" % (round(price_after_discount, 2)))

price_with_tax = price_after_discount + price_after_discount * tax_rate / 100
print("Total price = %2.2f" % (round(price_with_tax, 2)))
