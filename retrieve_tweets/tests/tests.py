from retrieve_tweets import get_tweets

def test():
    tweets = get_tweets.get_tweets('shaka_lulu',10)
    if len(tweets) != 10:
        raise AssertionError('tweets obtained != tweets retrieved')
    return

def test_trend():
	tweets = get_tweets.get_trends('2508428')
    if len(tweets) != 10:
        raise AssertionError('tweets obtained != tweets retrieved')
    return