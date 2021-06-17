import datetime
import pytz

def create_datetime(*args, timezone_str=None):
    if timezone_str:
        tz = pytz.timezone(timezone_str)
        d = datetime.datetime(*args)
        d = tz.localize(d)
    else:
        d = datetime.datetime(*args)
    return d

def print_formatted_datetime(datetime_obj, datetime_str):
    print(datetime_obj.strftime(datetime_str))

def print_difference(dt_first_obj, dt_second_obj, timezone_str=None):
    if timezone_str:
        tz = pytz.timezone(timezone_str)
        if not dt_first_obj.tzinfo:
            dt_first_obj = tz.localize(dt_first_obj)
        else:
            dt_first_obj = dt_first_obj.astimezone(tz)
        if not dt_second_obj.tzinfo:
            dt_second_obj = tz.localize(dt_second_obj)
        else:
            dt_second_obj = dt_second_obj.astimezone(tz)
        d = dt_first_obj - dt_second_obj
    else:
        first = datetime.datetime(dt_first_obj.year,
                                  dt_first_obj.month,
                                  dt_first_obj.day,
                                  dt_first_obj.hour,
                                  dt_first_obj.minute,
                                  dt_first_obj.second)
        second = datetime.datetime(dt_second_obj.year,
                                  dt_second_obj.month,
                                  dt_second_obj.day,
                                  dt_second_obj.hour,
                                  dt_second_obj.minute,
                                  dt_second_obj.second)
        d = first - second
    print(d)
