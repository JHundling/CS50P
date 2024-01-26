def main():

    camelCase = input("camelCase: ")
    print("snake_case: ", end = "")
    
    for i in camelCase:
        if i.isupper():
            print("_" + i.lower(), end = "")
        else:
            print(i, end = "")

    print()

main()
