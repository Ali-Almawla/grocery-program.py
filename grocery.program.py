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
