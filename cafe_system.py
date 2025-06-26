#Define the menu of restaurant
menu = {
    'Pizza':150, 
    'Pasta':90,
    'Burger':80,
    'Salad':70,
    'HotChocolate':120,
    'ColdCoffee':100,
    'BlackCoffee':80,
    'Tea':40,
    'Sandwich':60,
    'AppleJuice':50,
}

#Greet
print("Welcome to PYTHON Restaurant\n")
print("Our Menu")
print("Pizza: Rs.150\nPasta: Rs.90\nBurger: Rs.80\nSalad: Rs.70\nHotChocolate: Rs.120\nColdCoffee: Rs.100\nBalckCoffee: Rs.80\nTea: Rs.40\nSandwich: Rs.60\nAppleJuice: Rs.50\n") 

order_total = 0

#first order
while True:
    item_1 = input("Enter the name of item you want to order : ")
    
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order.")
    
    else:
        print(f"Sorry! Ordered item {item_1} is not available!")

    #another order
    another_order = input("Do you want to add another item? (Yes/No): ")
    if another_order != "Yes":
        break
        
        
print(f"The total amount of items to pay is Rs.{order_total}") 