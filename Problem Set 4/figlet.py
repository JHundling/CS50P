import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def main():

    if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:

        if sys.argv[2] in figlet.getFonts():

            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(user_input))

        else:
            sys.exit("Invalid usage")


    elif len(sys.argv) == 1:
        user_input = input("Input: ")
        font_choice = random.choice(figlet.getFonts())
        figlet.setFont(font = font_choice)
        print(figlet.renderText(user_input))


    else:
        sys.exit("Invalid usage")


main()
