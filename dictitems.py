from calendar import c


reference_dict = {
    "apple" : .99,
    "butter": 3.99,
    "milk": 5.99,
    "eggs": 2.99,
    "poptart": 1.37,
    "steak": 13.99,
    "bacon": 7.99,
}

shopping_list = {}

def ordering():
    for x in range(10000):
        order = input("What would you like to add to Cart? To see options press 'f'. To quit enter 'q'. To check cart 'c'. Return to Main Menu 'm'. To delete an item 'd'\n--> ")
        if order.lower() == 'f':
            for y, z in reference_dict.items():
                print(f"Item: {y.title()} --- Price: ${z}")
        # if order.lower() in reference_dict and shopping_list:        I TRIED TO MAKE A way to add onto existing order but it broke my entire program
        #     quantity = input("How much would you like?\n--> ")
        #     quantity = int(quantity) + int(shopping_list[order])
        #     shopping_list.update({order: quantity})
            # print(f"You have added {quantity} {order.title()}!")
        if order.lower() in reference_dict:
            quantity = input("How much would you like?\n--> ")
            shopping_list.update({order: quantity})
            print(f"You have added {quantity.title()} {order.title()}!")
        if order.lower() == 'd':
            for y, z in shopping_list.items():
                print(f"Item: {y} --- Quantity: {z}")
            remitem = input("Which item would you like to remove? ")
            if remitem in shopping_list:
                for y, z in shopping_list.items():
                    if y == remitem:
                        print(f"You have removed {z} {y} from your list!")
                        del shopping_list[remitem]
                        ordering()
            if remitem not in shopping_list:
                print("Please enter a valid answer")
        if order.lower() == 'q':
            quit() #Run price funtion with kill
        if order.lower() == 'c':
            price_check()
        if order.lower() == 'm':
            shopping_adder()
        

def quit():  #Run price funtion with kill
    print("Thank you For Shopping ShoppaCart!")
    total = 0
    for item, cost in reference_dict.items():
        if item in shopping_list:
            item_total = cost * int(shopping_list[item])
            total += item_total    
            print(f"{shopping_list[item]} {item} : {item_total}")
    print(f"Your Total: {total}")

def price_check(): #Observe this monster, took hours to figure out
    print("Your Current Cart:")
    total = 0
    for item, cost in reference_dict.items():
        if item in shopping_list:
            item_total = cost * int(shopping_list[item])
            total += item_total    
            print(f"{shopping_list[item]} {item} : {item_total}")
    print(f"Your Total: {total}")
            

def admin():
    pass

def shopping_adder(): # THIS IS THE MAIN FUNCTION
    for x in range(10000):
        progress = input("Welcome to Shoppa-Cart your online convienence cart Main Menu: What would you like to do?\n-Order ('o')\n-Quit ('q')\n-check cart ('c')\n-Delete Item ('d')\n-->  ")
        if progress.lower() == 'o':
            ordering()
        if progress.lower() == 'q':
            quit()
        if progress.lower() == 'c':
            price_check()
        if progress.lower() == 'd':
            for y, z in shopping_list.items():
                print(f"Item: {y} --- Quantity: {z}")
            remitem = input("Which item would you like to remove? ")
            if remitem in shopping_list:
                for y, z in shopping_list.items():
                    if y == remitem:
                        print(f"You have removed {z} {y} from your list!")
                        del shopping_list[remitem]
                        shopping_adder()
            if remitem not in shopping_list:
                print("Please enter a valid answer")
        if progress.lower() == 'admin':
            update = input("Welcome ADMIN. What changes would you like to make today?")
            pass 
        else:
            print("Please Enter a Valid Answer!")



shopping_adder()





# Test THings

# reference_dict = {
#     "apple" : .99,
#     "butter": 3.99,
#     "milk": 5.99,
#     "eggs": 2.99,
#     "poptart": 1.37,
#     "steak": 13.99,
#     "bacon": 7.99,
# }

# shopping_list = {"apple" : 5}

# def price_check(): #Observe this monster
#     for key, value in reference_dict.items():
#         if key in shopping_list:
#             for x, y in shopping_list.items():
#                 item_total = value * y
#                 print(type(value))
#                 print(type(y))
#                 print(item_total)
# price_check()

# for k, v in reference_dict.items():
#     if k == "apple":
#         print(k, v)


#         add hidden admin priveledges