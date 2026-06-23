# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

total_investment = 0

n = int(input("Kitne stocks add karne hain? "))

for i in range(n):
    stock = input("Stock Name: ").upper()
    quantity = int(input("Quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Investment =", investment)

    else:
        print("Stock available nahi hai")

print("\nTotal Investment =", total_investment)

# Save result in text file
with open("result.txt", "w") as file:
    file.write(f"Total Investment = {total_investment}")

print("Result result.txt file me save ho gaya")