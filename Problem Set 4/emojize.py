import emoji

def main():

    user_input = input("Input: ")
    converted_input = emoji.emojize(user_input, language='alias')
    print ("Output: ", converted_input)

main()
