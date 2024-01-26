def main():

    plate = input("Plate: ")

    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    symbols = [" ", ".", "?", "!", ",", ":" ";" "(",
    ")", "[", "]", "'", "-", '"', "/", "\\", "`", "@", "#", "*"]

    if not s[0:2].isalpha():
        return False

    if len(s) > 6 or len(s) < 2:
        return False

    i = 0
    num_string = ""
    for _ in range(len(s)):

        if s[i].isdigit() == True:

            if s[i:len(s)].isdigit() == False:

                return False

            num_string = num_string + s[i]

        i += 1

    if num_string != "" and num_string[0] == "0":
        return False

    for ch in s:
        if ch in symbols:
            return False


    return True

main()
