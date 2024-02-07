import random
import sys

def main():

    while True:

        try:
            level = int(input("Level: "))

            if level > 0:
                break
            else:
                pass
        except:
            pass

    answer = random.randint(1, level)

    while True:
        try:
            user_guess = int(input("Guess: "))

            if user_guess > answer:
                print("Too large!")

            elif user_guess < answer:
                print("Too small!")

            elif user_guess == answer:
                sys.exit("Just right!")

        except ValueError:
            pass


main()
