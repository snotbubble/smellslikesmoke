import urllib.request
import xml.etree.ElementTree as et
import os
import subprocess
import re, html
from math import sin, cos, sqrt, atan2, radians

def getdist(la, lb, oa, ob) :
	# function posted by gwaramadze & fixed by Michael0x2a on stackexchange, referring to Andrew Hedges, who referred to Bob Chamberlain
	# https://andrew.hedges.name/experiments/haversine/
	# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
	
	# approximate radius of earth in km
	R = 6371.0

	lat1 = lb
	lon1 = ob
	lat2 = la
	lon2 = oa

	dlon = radians(lon2 - lon1)
	dlat = radians(lat2 - lat1)
	
	a = (sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2))
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c
	return(distance)
    
tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

cdr = os.path.split(os.path.realpath('redzone.py'))[0]
feed = cdr + "/feed.xml"
print(feed)

ac = []
b = [-33.683798, 150.555539]

#s = urllib.request.urlretrieve('http://www.rfs.nsw.gov.au/feeds/majorIncidents.xml', feed)
t = et.parse(feed).getroot()

bb = 'gst-launch-1.0 -q filesrc location=' + cdr + '/jno.wav ! decodebin ! autoaudiosink'
aa = 'gst-launch-1.0 -q filesrc location=' + cdr + '/jsu.wav ! decodebin ! autoaudiosink'

redburbs = ['faulconbridge', 'springwood', 'linden', 'winmalee', 'valley heights', 'warrimoo', 'woodford', 'bunyan', 'yellow rock', 'mount hay']
yellowburbs = ['tomah', 'bilpin', 'berambing', 'mount banks', 'wentworth falls', 'blaxland', 'glenbrook', 'bowen mountain', 'yarramundi', 'ruined castle']

for d in t.iter('item') :
	odk = 999.0
	tt = ""
	dd = ""
	cc = ""
	isred = False
	isyellow = False
	for m in list(d.iter()) : 
		if "title" in m.tag: tt = m.text
		if "description" in m.tag:
			dd = no_tags = tag_re.sub('', m.text)
			dd = html.escape(dd)
		if "polygon" in m.tag:
			pp = m.text
			c = iter(pp.split())
			ci = ([x ,next(c, '')] for x in c)
			o = list(ci)
			e = []
			for k in o :
				dk = getdist(float(k[0]), b[0], float(k[1]), b[1])
				if dk < odk:
					odk = dk
		if "category" in m.tag: cc = m.text
	for r in redburbs :
		if r in dd.lower() : isred = True
	for y in yellowburbs :
		if y in dd.lower() : isyellow = True
	if isred: print("isred = " + str(isred))
	if isyellow: 
		print("{0:.2f}".format(odk) + "Km : " + tt + " is on fire (" + cc + ")")
		for q in range(2) : subprocess.call(bb.split())
	if isred or odk < 12.0 or (isyellow and "emergency" in dd.lower()):
		print("{0:.2f}".format(odk) + "Km : " + tt + " : " + cc + "\n\t" + dd + "\n\n")
		for q in range(10) : subprocess.call(aa.split())


