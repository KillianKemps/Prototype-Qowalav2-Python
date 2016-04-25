import time
from threading import Thread

import praw

def test():
    print('QReddit ok!')

def get_subreddit():
    r = praw.Reddit(user_agent='my_cool_application')

    # Request the page 10 times
    for i in range(0, 10):
        submissions = r.get_subreddit('opensource').get_hot(limit=5)

        # Display result and sleep in between
        print([str(x) for x in submissions])
        time.sleep(1)

def initialize():
    # Start the subreddit getter function in another thread
    _thread = Thread(target=get_subreddit)
    _thread.start()
