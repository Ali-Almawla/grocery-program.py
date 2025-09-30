groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
    }

shopping_cart = {}
while True:
    user_input = input("What do you want to buy? ")

    if user_input == "done":
        break

    list = user_input.split()
    item = list[0]

    if len(list) > 1:
     quantity = int(list[1])

    else:
     quantity =1

    if item in groceries:
        if item in shopping_cart:
            shopping_cart[item] += quantity
        else:
            shopping_cart[item] = quantity
    else:
        print("Sorry, we don’t have that item.")

total_cost = 0
for item, quantity in shopping_cart.items():
    price = groceries[item]

    if item == "milk" and quantity > 2:
        price -= 1

    total_cost += price * quantity

print(f"\nYou bought: {shopping_cart}")
print(f"Total = ${total_cost}")

if total_cost > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")