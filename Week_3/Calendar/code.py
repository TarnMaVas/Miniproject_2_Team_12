''' calendar '''
import calendar as calend

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    if 0 <= number <= 6:
        n = calend.day_name[number][0:3]
    return n.lower()

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    num = date.split(".")
    if int(num[0]) <= 31:
        n = calend.weekday(int(num[2]), int(num[1]), int(num[0]))
    return n

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> calendar(8 , 2015)
    'mon tue wed thu fri sat sun\\n                      1   2\\n  3   4   5   \
6   7   8   9\\n 10  11  12  13  14  15  16\\n 17  18  19  20  21  22  23\\n \
24  25  26  27  28  29  30\\n 31'
    """

    if year > 1583:
        listok = [weekday_name(x) for x in range(7)]
        c = calend.month(year, month, w=3)
        cal = c.split("\n")[1:]
        cal.pop()
        a = "\n".join(cal)
        return a.lower()

def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> transform_calendar(calendar(5, 2002))
    'mon   6 13 20 27\\ntue   7 14 21 28\\nwed 1 8 15 22 29\\nthu 2 9 \
16 23 30\\nfri 3 10 17 24 31\\nsat 4 11 18 25  \\nsun 5 12 19 26'
    >>> transform_calendar(calendar(8 , 2015))
    'mon   3 10 17 24 31\\ntue   4 11 18 25  \\nwed   5 12 19 26  \\nthu   \
6 13 20 27  \\nfri   7 14 21 28  \\nsat 1 8 15 22 29  \\nsun 2 9 16 23 30'
    """
    cal = calendar.split("\n")[1:]
    listok = []
    sp = []

    for i, value in enumerate(cal):
        value = value.split(" ")
        res = list(filter(lambda x: x.isdigit(), value))
        listok.append(res)
    spisochok = []
    value = listok[0]
    listok[0] = [" "] * (7 - len(value)) + listok[0]

    value = listok[-1]
    listok[-1] += [" "] * (7 - len(value))
    dni = [weekday_name(x) for x in range(7)]
    for h in listok:
        spisochok.append(h[i])
        sp.append(spisochok)
    hgh = list(zip(*listok))
    output = ""

    for j in range(7):
        output += dni[j] + " " + " ".join(hgh[j]) + "\n"
    return output.strip()


if __name__ == "__main__":
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print(calendar(month, year))
    except ValueError as err:
        print(err)