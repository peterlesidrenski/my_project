total_pages = int (input("enter a number: "))
pages_per_hour = int(input("enter pages: "))
days = int(input("enter days: "))
from math import floor
houurs_per_day = floor(total_pages/pages_per_hour/days)
print(houurs_per_day)