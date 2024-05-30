import random
from datetime import datetime


def generate_date(day: int = 0, month: int = 0, year: int = 0, hour: int = None, minute: int = None,
                  second: int = None) -> GeneratedDate:
    """
    Generates a random date and optional time.

    :param day: Day of the month. If 0, a random value from 1 to 28 is generated.
    :param month: Month of the year. If 0, a random value from 1 to 12 is generated.
    :param year: Year. If 0, a random value from 1970 to 2050 is generated.
    :param hour: Hour of the day. If None, it is not included in the output.
    :param minute: Minute of the hour. If None, it is not included in the output.
    :param second: Second of the minute. If None, it is not included in the output.
    :return: A GeneratedDate object with the specified or random values.
    """
    if day < 0 or day > 31:
        raise ValueError("Invalid day. Please provide a day between 0 and 31.")
    if month < 0 or month > 12:
        raise ValueError("Invalid month. Please provide a month between 0 and 12.")
    if hour is not None and (hour < 0 or hour > 23):
        raise ValueError("Invalid hour. Please provide an hour between 0 and 23.")
    if minute is not None and (minute < 0 or minute > 59):
        raise ValueError("Invalid minute. Please provide a minute between 0 and 59.")
    if second is not None and (
