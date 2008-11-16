import os
import pickle
import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)

serie = 0

while (True):
	if (os.path.exists("%d.pickle" % serie)):
		try:
			d = pickle.load(file("%d.pickle" % serie))
			twitter = d['taxa_twitter']
			flickr  = d['taxa_flickr']

			print "Taxa twitter = %d" % twitter
			print "Taxa flickr = %d"  % flickr

			str1 = chr(twitter)
			str2 = chr(flickr)

			ser.write(str1 + str2)
			serie += 1
		except Exception, e:
			print e
