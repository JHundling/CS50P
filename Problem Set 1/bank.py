def main():

    text = input("Greeting: ")

    text = text.strip()

    if text.startswith("Hello") == True:
            print("$0")
    elif text.startswith("H") == True:
            print("$20")
    else:
           print ("$100")

main()
