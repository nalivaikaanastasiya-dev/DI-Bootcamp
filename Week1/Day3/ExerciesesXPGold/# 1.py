# Part 1: Simple Price List Dictionary
items_price_list = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("--- Part 1: Item and Price Listing ---")

# Iterate through the dictionary and print each item and its price in a sentence
for item, price in items_price_list.items():
    print(f"The price of one **{item}** is **${price:.2f}**.")

print("\n" + "="*40 + "\n")


# Part 2: Advanced Stock and Price Dictionary
items_stock_list = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

print("--- Part 2: Total Cost Calculation ---")

total_cost = 0

# Iterate through the dictionary
for item, data in items_stock_list.items():
    # Extract price and stock for the current item
    price = data["price"]
    stock = data["stock"]
    
    # Calculate the cost for all units of this item
    item_total = price * stock
    
    # Add to the overall total
    total_cost += item_total
    
    print(f"**{item.title()}**: {stock} in stock @ ${price:.2f} each = **${item_total:.2f}**")

print("--------------------------------------")
# Print the final total cost
print(f"The total cost to buy everything in stock is: **${total_cost:.2f}**")