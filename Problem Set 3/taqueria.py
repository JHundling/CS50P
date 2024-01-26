def main():


    menu = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
        }


    total = 0.00


    while True:

        try:

            item = input("Item: ").lower()


            total = total + menu[item] #I don't need a 'if' check here, because I have the KeyError below that catches if something weird is entered.
            print("Total: $" + '%.2f'%total)



        except KeyError:
            pass

        except EOFError: #This checks for cntrl+d as the escape
            break


main()
