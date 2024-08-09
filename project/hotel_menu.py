menu = {
    'pizza': 99,
    'maggie': 80,
    'momos' : 50,
    'gulab jamun': 30,
    'soda': 50
}
print("\n\nWelcome to our python restaurant. Here's the menu:\n")
tittle = "menu".upper()
print(tittle.center(50, "="))
print("\npizza: Rs99\nmaggie: Rs80\nmomos : Rs50\ngulab jamun: Rs30\nsoda: Rs50")

orderTotal = 0

item1 = input("Enter the name of the item you want to order = ")

if item1 in menu:
    orderTotal += menu[item1]
    print(f"your item {item1} has been added in your order")

else:
    print(f"Ordered item {item1} is not available yet!!")

anotherOrder = input("do you want to ordered another item: (yes/no): ")
if anotherOrder == "yes":
    item2 = input("Enter the name of the second item")
    if item2 in menu:
        orderTotal += menu[item2]
        print(f"your item {item2} has been added in your order")
    else:
        print(f"Ordered item {item2} is not available yet!!")

print(f"The total amount of item is pay is {orderTotal}")
