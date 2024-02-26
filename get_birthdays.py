from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    try:
        for usr in users:
            name = usr["name"]
            bday = usr["birthday"].date()
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:
                if bday_this_year.weekday() < 5 or (
                    today.weekday() != 0 and today.weekday() != 6
                ):
                    bday_this_year = bday_this_year.replace(
                        year=bday_this_year.year + 1
                    )

            weekday = bday_this_year.weekday()
            if weekday >= 5:
                bday_this_year += timedelta(days=7 - weekday)

            delta = (bday_this_year - today).days
            if delta < 7:
                weekdays[bday_this_year.strftime("%A")].append(name)

        bdays = {}
        for k, v in weekdays.items():
            if v != []:
                bdays.update({k: v})
        if bdays != {}:
            for k, v in bdays.items():
                print(f"\033[96m{k}\x1b[0m: {", ".join(v)}")
        else:
            print("There is no one to congratulate during the week")

    except TypeError:
        print("\033[41mSomething wrong in input data, pls check it\x1b[0m")
