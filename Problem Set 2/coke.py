
def main():

    total = 50

    while total > 0:

        print("Amount Due: ", end="")
        print(total)

        deduction = int(input("Insert coin: "))

        if deduction == 5 or deduction == 10 or deduction == 25:

                total = total - deduction

    print("Change Owed: ", end = "")
    print(abs(total))


main()
