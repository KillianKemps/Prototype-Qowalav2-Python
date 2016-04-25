import time
from threading import Thread

import praw

def test():
    print('QReddit ok!')

def async_getter():
    for i in range(0,10):
        r = praw.Reddit(user_agent='my_cool_application')
        submissions = r.get_subreddit('opensource').get_hot(limit=5)

        print([str(x) for x in submissions])
        time.sleep(1)

def initialize():
    _thread = Thread(target=async_getter)
    _thread.start()
