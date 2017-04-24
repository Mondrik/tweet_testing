from retrieve_tweets import get_tweets

def test():
    tweets = get_tweets.get_tweets('shaka_lulu',10)
    if len(tweets) != 10:
        raise AssertionError('tweets obtained != tweets retrieved')
    return
