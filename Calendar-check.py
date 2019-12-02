

def call(day, month, year):
    dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if year % 4 == 0 and month == 2 and day == 29:
        return True
    elif month > 12:
        return False
    elif dict[month] < day:
        return False
    else:
        return True


print(call(29, 2, 5))
