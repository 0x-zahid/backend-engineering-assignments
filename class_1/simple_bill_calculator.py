price = float(input())
quantity = int(input())

total_price = price * quantity

tax = total_price * 5 / 100

price_after_tax = total_price + tax

print(f"Total price: {total_price}")
print(f"Price after added tax: {price_after_tax}")