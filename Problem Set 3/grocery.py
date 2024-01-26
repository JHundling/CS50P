def main():

    grocery_dict = {}


    while True:

        try:

            item = input().upper()

            if item not in grocery_dict:

                grocery_dict[item] = 1

            else:
                grocery_dict[item] +=1

        except EOFError:

            grocery_list = list(grocery_dict.items())

            sorted_list = sorted(grocery_list)

            sorted_dict = dict(sorted_list)

            for item in sorted_dict:
                print(sorted_dict[item], item)

            break


main()
