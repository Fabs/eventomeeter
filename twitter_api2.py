from urllib import urlopen

url = 'http://search.twitter.com/search.json?q=%s'

def query_twitter(term):
    s = urlopen(url % (term)).read()
    dic = eval(s.replace('null', 'None'))
    return dic

if __name__ == '__main__':
    d = {}
    for post in query_twitter("brhackday")['results']:
        try:
            d[post['from_user']] += 1
        except KeyError:
            d[post['from_user']] = 1

    print d
