#  Shopping Cart Manager

cart = []

item1 = input("Enter_item 1: ")
item2 = input("Enter_item 2: ")
item3 = input("Enter_item 3: ")

cart.append(item1)
cart.append(item2)
cart.append(item3)

print("Your cart:", cart)
print("Total items:", len(cart))