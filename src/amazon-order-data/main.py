#!/usr/bin/env python3
import pandas

ORDER_DATA = "../../reports/Retail.OrderHistory.1/Retail.OrderHistory.1.csv"

data = pandas.read_csv(ORDER_DATA)
data["Unit Price"] = data["Unit Price"].str.replace(",", "")

subtotal = 0
highest_price = 0
for price in data["Unit Price"]:
    price = price.replace(",", "")
    subtotal += float(price)
    if float(price) > highest_price:
        highest_price = float(price)

tax = 0
for price in data["Unit Price Tax"]:
    tax += float(price)

subtotal = round(subtotal, 2)
tax = round(tax, 2)
total = subtotal + tax

print(f"Subtotal: {subtotal}")
print(f"Tax: {tax}")
print(f"Total: {total}")

print(highest_price)

#data.plot.bar(x="Order Date", y="Unit Price", rot=90)
