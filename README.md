Fire data from:  
http://www.rfs.nsw.gov.au/feeds/majorIncidents.xml  


Variable b is the most vunerable evac route location, not home address.  
In this case: the site of a probable traffic jam to get out of the suburb.

redburbs contain locations that trigger an evac if burning.  
yellowburbs are to watch carefully if burning. 

Evac alarm will trigger if:
* any fire (poly points) is within 12km.
* any redburbs are on fire (sometimes there isn't a polygon yet).
* any redburbs are mentioned in other fires.
* any yellowburbs are on fire and flagged as emergency by RFS.

Warning notification will trigger if:
* any fire is within 20km and flagged as out-of-control by RFS.
* any yellowburbs are on fire or mentioned in other fires.

Uses a distance function from Bob Chamberlain, via Andrew Hedges, via 'gwaramadze' via 'Michael0x2a' (latter two on stackexchange).  
https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude  
Distances may not be totally accurate.  

run in terminal as:
> watch -n 600 'python3 redzone.py'

Works OK on Jolla Sailfish 3.2, Sony Xperia XA2. 
Phone has to be kept out of suspended state overnight. 
Nightly-Clock app by Paul Wallace will do this, just leave it running overnight (will drain battery).  
https://openrepos.net/content/allstar12345/nightly-clock  
