def main():

    user_input = input("What is the time? ")

    updated_user_input = convert(user_input)


    if 7 <= updated_user_input <=8:
        print ("Breakfast Time")
    elif 12 <= updated_user_input <=13:
        print ("Lunch Time")
    elif 18 <= updated_user_input <=19:
        print ("Dinner Time")
    else:
        print ("")


def convert(z):

    a, b = z.split(":")

    a = int (a)
    b = int (b)
    b = b/60

    updated_user_input = a + b

    return updated_user_input


if __name__ == "__main__":
    main()
