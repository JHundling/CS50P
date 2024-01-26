def main():

    words = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    words = convert(words)

    if words == "42":
        output = "Yes"

    elif words == "forty-two":
        output = "Yes"

    else:
        output = "No"

    print(output)

def convert(d):
    words = d.strip()
    words = words.lower().replace(" ", "-")
    return words

main()
