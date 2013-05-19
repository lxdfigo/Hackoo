import httplib
import time
import os
import sys

fulltime = time.localtime(time.time())
year = fulltime.tm_year
mon = fulltime.tm_mon
day = fulltime.tm_mday
tot = 0


if day>1:
    if os.path.exists("log\\%d_%d_%d.log" % (year , mon , day-1)) == True:
        fin = open("log\\%d_%d_%d.log" % (year , mon , day-1), "a+")
        for line in fin:
            tot = tot + 1
        cmd = "delete from user where year = %d and month = %d and day = %d" % (year,mon,day-1)
        conn = httplib.HTTPConnection("localhost","8000")
        conn.request("GET","/cgi-bin/database.py?"+cmd)
        #response = conn.getresponse() 
        #print response.status 
        #print response.read().strip()
        cmd = "insert into user values ('%s',%d,%d,%d,%d)" %(sys.argv[1],tot,year,mon,day-1)
        conn = httplib.HTTPConnection("localhost","8000")
        conn.request("GET","/cgi-bin/database.py?"+cmd)
        #response = conn.getresponse() 
        #print response.status 
        #print response.read().strip()

tot = 0

if os.path.exists("log\\%d_%d_%d.log" % (year , mon , day)) == True:
    fin = open("log\\%d_%d_%d.log" % (year , mon , day), "a+")
    for line in fin:
        tot = tot + 1
    cmd = "delete from user where year = %d and month = %d and day = %d" % (year,mon,day)
    conn = httplib.HTTPConnection("localhost","8000")
    conn.request("GET","/cgi-bin/database.py?"+cmd)
    #response = conn.getresponse() 
    #print response.status 
    #print response.read().strip()
    cmd = "insert into user values ('%s',%d,%d,%d,%d)" %(sys.argv[1],tot,year,mon,day)
    conn = httplib.HTTPConnection("localhost","8000")
    conn.request("GET","/cgi-bin/database.py?"+cmd)
    #response = conn.getresponse() 
    #print response.status 
    #print response.read().strip()