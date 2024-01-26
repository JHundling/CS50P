
def main():

    intake = input("Input: ")

    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    for i in intake:

        for v in vowels:

            if i == v:
                i = ""

        print(i, end = "")

    print()

main()
