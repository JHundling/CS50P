def main():

    month_list = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
    }

    while True:

        try:

            user_input = input("Date: ").strip()
            if "/" in user_input:

                month, date, year = user_input.split(sep = "/")

                if int(date) >31 or int(month) >12 or int(date) <1 or int(month) <1:
                    raise ValueError

                print(year, f"{int(month):02d}", f"{int(date):02d}", sep = "-")
                break


            elif "," in user_input:
                month_date, year = user_input.split(sep = ",")
                month, date = month_date.split(sep =" ")
                year = year.strip()

                if int(date) >31 or int(month_list[month]) >12 or int(date) <1 or int(month_list[month]) <1:
                    raise ValueError

                print(year, month_list[month], f"{int(date):02d}", sep = "-")
                break

        except ValueError:
            pass

        except KeyError:
            pass

        except EOFError:
            break

        else:
            pass

main()
