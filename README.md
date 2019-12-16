get fire data from:  
http://www.rfs.nsw.gov.au/feeds/majorIncidents.xml  
look for polygons,  
get distance from evac route to nearest polygon point,  
report and alert if conditions are met.  

uses a distance function from Bob Chamberlain, via Andrew Hedges, via 'gwaramadze' via Michael0x2a (latter two on stackexchange) https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

wav files are temps; sound bad on the XA2 phone.

run in terminal as:
> watch -n 600 'python3 redzone.py'

works OK on Jolla Sailfish 3.2, Sony Xperia XA2.
