import sys
import json
import requests

def main():

    try:
        n = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except IndexError:
        sys.exit("Missing command line argument")

    index = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    price = (((index["bpi"])["USD"])["rate"])

    price = price.replace(",", "")
    price = float(price)

    total = price * n

    print(f"${total:,.4f}")


main()



