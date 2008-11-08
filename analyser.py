from urllib import urlopen

def extractKeyWords(context,query=""):
   context = context.replace(" ","+")
   urlbase = "http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction?appid=EventOMeeter&output=json&context=%s&query=%s"%(context,query)
   results = urlopen(urlbase)
   jsonResults = results.read()
   dic = eval(jsonResults)
   return dic['ResultSet']['Result']
   

print extractKeyWords("Italian sculptors and painters of the renaissance favored the Virgin Mary for inspiration")