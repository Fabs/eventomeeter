from urllib import urlopen

def extractKeyWords(context,query=""):
   context = context.replace(" ","+")
   query = query.replace(" ","+")
   urlbase = "http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction?appid=EventOMeeter&output=json&context=%s&query=%s"%(context,query)
   results = urlopen(urlbase)
   jsonResults = results.read()
   dic = eval(jsonResults)
   return dic['ResultSet']['Result']
   

if __name__ == '__main__':
   print extractKeyWords(raw_input("Enter Text\n"),"cold war")