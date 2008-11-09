from urllib import urlopen,urlencode

class Dummy():
   def __init__(self,dummy):
      self.dummy = dummy

   def relevant_content(self):
      return self.dummy

   def __str__(self):
      return "dummy: %s"%(self.dummy)

   __repr__ = __str__
   


def extractKeyWords(contextable):
   dic_params ={
      "appid" : "teventomeeter",
      "context" : contextable.relevant_content(),
      "output" : 'json', 
   }
   params = urlencode(dic_params)
   urlbase = "http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction?%s"%(params)
   results = urlopen(urlbase)
   jsonResults = results.read()
   dic = eval(jsonResults)
   return dic['ResultSet']['Result']
   

if __name__ == '__main__':
   dummy = Dummy(raw_input("Enter Text\n"))
   print extractKeyWords(dummy)