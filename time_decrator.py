#!env/bin/python
# -*- coding: utf-8 -*-

import time

def time_counter(func):
        def wrapper(*args, **xargs):
            start_time = time.time()
            result = func(*args, **xargs)
            end_time = time.time()
            print("{} seconds spent".format(end_time - start_time))
            return result
        return wrapper
