class Calendar():

    def __init__(self):
        self.first_year = 1900

    def get_days_in_year(self, year):
        days = 0
        for i in range(1, 13):
            days += self.get_days_in_month(i, self.is_leap_year(year))
        return days

    def get_days_in_month(self, month, leap_year = False):
        if month in [4, 6, 9, 11]:
            return 30
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month == 2:
            if leap_year:
                return 29
            else:
                return 28
        else:
            print 'Error in month:', month

    def get_weekday(self, date):
        days = 0
        for i in range(self.first_year, date[0]):
            days += self.get_days_in_year(i)

        for i in range(1, date[1]):
            days += self.get_days_in_month(i, self.is_leap_year(date[0]))
        days += date[2]

        return days % 7

    def get_weekdays_on_first_day_of_month_count_for_period(self, date_start, date_end, weekday_pos):
        days = 0
        for i in range(date_start[0], date_end[0]+1):
            for j in range(1, 13):
                if self.get_weekday([i, j, 1]) == 0:
                    days += 1

        return days

    def is_leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False



def solve():
    calendar = Calendar()
    print calendar.get_weekday([2000, 12, 31])
    print calendar.get_weekdays_on_first_day_of_month_count_for_period([1901, 1, 1], [2000, 12, 31], 0)
    pass