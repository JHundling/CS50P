def main():

    user_input = input("What is the time? ")

    if user_input.endswith("p.m."):
        user_input = user_input.removesuffix(" p.m.")
        updated_user_input = convert_pm(user_input)

    elif user_input.endswith("a.m."):
        user_input = user_input.removesuffix(" a.m.")
        updated_user_input = convert_24h(user_input)

    else:
        updated_user_input = convert_24h(user_input)



    if 7 <= updated_user_input <=8:
        print ("Breakfast Time")
    elif 12 <= updated_user_input <=13:
        print ("Lunch Time")
    elif 18 <= updated_user_input <=19:
        print ("Dinner Time")
    else:
        print ("No Snacking!")


def convert_24h(z):

    a, b = z.split(":")

    a = int (a)
    b = int (b)


    b = b/60

    updated_user_input = a + b

    return updated_user_input


def convert_pm(z):

    a, b = z.split(":")

    a = int (a) +12 
    b = int (b)


    b = b/60

    updated_user_input = a + b

    return updated_user_input



main()


