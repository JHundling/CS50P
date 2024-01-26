def main():

    user_input = get_input("Fraction: ")

    try:
        if user_input >= 99:
            print("F")
        elif user_input <= 1:
            print("E")
        else:
            print(user_input, "%", sep="")

    except:
        pass

def get_input(s):

    while True:


        try:

            check_x, check_y = input(s).split(sep="/")

            if "." in check_x or "." in check_y:
                raise ValueError

            check_x = float(check_x)
            check_y = float(check_y)


            if check_y < check_x:
                check_y = 0

            if check_y < 0 or check_x < 0:
                check_y = 0


            z = check_x / check_y *100

            z_final = int(round(z))


        except:
            pass


        else:
            return z_final


main()
