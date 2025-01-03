import datetime
from modules.timex.timex import get_now
def add_one(number):
    return number + 1


def time_add(seconds):
    now_time = get_now()
    return now_time + datetime.timedelta(seconds=seconds)