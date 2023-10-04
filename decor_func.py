import csv
from functools import wraps
import json


def c_s_v_data(csv_file):
    def dec(func):
        res = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(csv_file, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    args = map(int, row)
                    res.append(func(*args, **kwargs))
            return res

        return wrapper

    return dec


def write_json_file(json_f):
    def dec(func):
        js = []

        @wraps(func)
        def wrapper(args, **kwargs):
            res = func(*args, **kwargs)
            my_dict = {'args': args,
                       'result': res}
            js.append(my_dict)
            with open(json_f, 'w', encoding='uft-8') as ff:
                json.dump(js, ff, indent=2)
            return my_dict

        return wrapper

    return dec
