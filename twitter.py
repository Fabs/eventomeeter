from urllib import urlopen
import datetime
import pickle
import time

serie = 0
while (True):
    n = 0
    next_url = 'http://search.twitter.com/search.json?q=brhackday08'
    contador = 0
    posts_na_ultima_hora = 0
    twits = []
    while n<3:
        data = urlopen(next_url).read()
        data = eval(data.replace('null', 'None'))
        next_url = "http://search.twitter.com/search.json"+data['next_page']
        #print "Querying twitter (%s)" % (next_url)
        for post in data['results']:
            #print data['results'][0]['created_at']
            dia = int(post['created_at'].split()[1])
            hora, min, seg = map(int, post['created_at'].split()[4].split(':'))
            now = datetime.datetime.now()
            horario_post = datetime.datetime(now.year, now.month, dia, hora, min, seg) - datetime.timedelta(hours=2)

            #print horario_post
            tempo_passado = now - horario_post
            #print tempo_passado
            if (tempo_passado < datetime.timedelta(hours=1)):
                posts_na_ultima_hora +=1
                twits.append((post['from_user'], post['text']))
                print "* %s (%s)" % (tempo_passado, post['from_user'])
            #print "%s (%s)" % (tempo_passado, post['from_user'])
            #print data
            #if (tempo_passado <
            contador += 1
        n+=1

    print "posts_na_ultima_hora = %d" % posts_na_ultima_hora
    if (posts_na_ultima_hora >= 0):
        saida_arduino = 1

    if (posts_na_ultima_hora > 3):
        saida_arduino = 2

    if (posts_na_ultima_hora > 6):
        saida_arduino = 3

    if (posts_na_ultima_hora > 8):
        saida_arduino = 4

    if (posts_na_ultima_hora > 12):
        saida_arduino = 5

    print saida_arduino

    twits_tratados = []

    taxa_flickr = [] 

    for twit in twits:
        twits_tratados.append({'type': 'twitter', 'text': twit[1], 'user': twit[0]})

    to_pickle = {   'taxa_twitter' : saida_arduino,
                    'taxa_flickr' : taxa_flickr,
                    'items': twits_tratados,                    
                                            }

    pickle.dump(to_pickle, file(str(serie) + ".pickle", 'w'))
    serie += 1
    time.sleep(60)
    
