# Define the menu
menu = {
    'pizza': 40,
    'burger': 60,
    'pasta': 50,
    'salad': 70,
    'coffee': 80
}

print("Welcome to the Python Restaurant")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# First item
item1 = input("\nEnter the name of the item you want to order: ").lower()
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item '{item1}' has been added to your order.")
else:
    print("Sorry, we don’t serve that item.")

# Another order?
another_order = input("Do you want to add another item? (yes/no): ").lower()

if another_order == "yes":
    item2 = input("Enter the second item: ").lower()
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item '{item2}' has been added to the order.")
    else:
        print(f"Sorry, we don’t serve '{item2}'.")

print(f"\nThe total amount of your order is: Rs{order_total}")
