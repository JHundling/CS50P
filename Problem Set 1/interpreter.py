def main():

    user_input = input("What would you like to calculate? ")

    x, y, z = string_split(user_input)

    x = int(x)
    z = int(z)

    if y == "+":
        answer = x+z
    elif y == "-":
        answer = x-z
    elif y == "*":
        answer = x*z
    elif y == "/":
        answer = x/z
    else:
        answer = "IDK what to do"

    answer = float(answer)
    print(answer, end="")

def string_split(a):
    x,y,z = a.split(" ")
    return x,y,z

main()
