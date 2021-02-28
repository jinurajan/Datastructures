"""
Number of Days Between Two Dates

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Constraints:

The given dates are valid dates between the years 1971 and 2100.

"""

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        [date1,date2] = sorted([date1,date2])
        y1,m1,d1 = list(map(int,date1.split('-')))
        y2,m2,d2 = list(map(int,date2.split('-')))
        self.day31 = {1,3,5,7,8,10,12}
        if y1==y2:
            return self.get_day(y2,m2,d2) - self.get_day(y1,m1,d1)
        else:
            sm = self.day_of_year(y1) - self.get_day(y1,m1,d1)
            sm += self.get_day(y2,m2,d2)
            for y in range(y1+1,y2):
                sm += self.day_of_year(y)
            return sm

    def get_day(self, year, month, day):
        sm = 0
        for m in range(1,month):
            sm += self.day_of_month(year,m)
        sm += day
        return sm

    def day_of_month(self,year,month):
        if month in self.day31:
            return 31
        elif month == 2:
            if self.day_of_year(year)==366:
                return 29
            else:
                return 28
        else:
            return 30

    def day_of_year(self,year):
        if year%100==0:
            if year%400==0:
                return 366
            else:
                return 365
        else:
            if year%4==0:
                return 366
            else:
                return 365
