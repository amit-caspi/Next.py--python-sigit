# Next.py- Exercise 4.4 by Amit Caspi 
# A program that knows how to produce dates and times from a certain date to infinity.

from datetime import datetime 

def gen_secs():
    """
    The function returns a generator that produces all possible second ranges (numbers between 0 and 59).
    """
    for sec in range(0, 60):
        yield sec

def gen_minutes():
    """
    The function returns a generator that produces all possible minute ranges (numbers between 0 and 59).
    """
    for min in range(0, 60):
        yield min

def gen_hours():
    """
    The function returns a generator that produces all possible hour ranges (numbers between 0 and 23).
    """
    for hour in range(0, 24):
        yield hour

def gen_time():
    """
    The function uses the gen_secs, gen_minutes, and gen_hours generators to print the time in the following format: 00:00:00.
    (The generator must generate all possible hours of the day starting at 00:00:00).
    """
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"

def gen_years(start = datetime.now().year):
    """
    The function receives as a parameter a number representing a year (with a default value of the current year),
	and produces the year received as a parameter and all the years from it onwards.
    """
    while True:
        yield start
        start += 1

def gen_months():
    """
    The function returns a generator that produces all the numbers of the months in a year (numbers between 1 and 12).
    """
    for month in range(1, 13):
        yield month

def gen_days(month, leap_year = True):
    """
    The function returns a generator that produces the number of days in that month 
	(depending on the given month and regarding a leap year or not).
	:param month: month number
    :param leap_year: a variable that represents whether it is a leap year or not.
    :type month: integer
    :type leap_year: bool
    """
    for day in range(1, 29):
        yield day
    if month != 2 or leap_year:
        day += 1
        yield day
    if month != 2:
        day += 1
        yield day
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day += 1
        yield day

def is_leap_year(year):
    """
    The function determine if a year is a leap year or not (returns True/False).
    :param year: the year to check
    :type year: integer
    """
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

def gen_date():
    """
    The function returns a generator that produces a full date signature,
	in the following format: dd / mm / yyyy hh: mm: ss.
    """
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for time in gen_time():
                    yield f"{day:02d}/{month:02d}/{year} {time}"

def main():
	# Print the value generated from the generator returned from the gen_date generator function after every 1000000 iterations.
    i = 0
    full_date = gen_date()
    for date in full_date:
        i += 1
        if i % 1000000 == 0:
            print(next(full_date))


if __name__ == '__main__':
    main()
