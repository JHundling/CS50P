import random
import sys

def main():

    n = get_level()
    score = 10
    question_count = 10

    while True:

        x, y = generate_integer(n)

        actual_answer = x + y

        local_count = 3

        while local_count > 0:

            if question_count == 0:
                print(f"Score: {score}")
                sys.exit(0)

            if score == 0:
                sys.exit("Score: 0")

            user_answer = int(input(f"{x} + {y} = "))

            if user_answer == actual_answer:
                question_count -= 1
                break

            else:
                print("EEE")
                local_count -= 1
                if local_count == 2:
                    score -= 1

                if local_count == 0:
                    print(f"{x} + {y} = {actual_answer}")
                    question_count -= 1



def get_level():

    while True:
        try:
            n = int(input("Level: "))

            if 0 < n < 4:
                return n
                break

        except ValueError:
            pass


def generate_integer(i):

    if i == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif i == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif i == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    else:
        sys.exit("Something has gone terribly wrong")

    return x, y


if __name__ == "__main__":
    main()
