import praw

def test():
    print('QReddit ok!')

def initialize():
    r = praw.Reddit(user_agent='my_cool_application')

    submissions = r.get_subreddit('opensource').get_hot(limit=5)

    print([str(x) for x in submissions])
