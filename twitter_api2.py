from urllib import urlopen

url = 'http://search.twitter.com/search.json?q=%s'

def query_twitter(term):
    s = urlopen(url % (term)).read()
    dic = eval(s.replace('null', 'None'))
    #print dic
    return dic

if __name__ == '__main__':
    d = {}
    for post in query_twitter("brhackday")['results']:
        
    print d
