import sys
import httplib
import time
if __name__ == "__main__":    
    sample_list = [0,32,10,0,14,24,12,12,45,74,12,12,45,15,0,12,75,45,12,45,0,0,0,0,0,0,0,0,0,0,0,0]
    fulltime = time.localtime(time.time())
    year = fulltime.tm_year
    mon = fulltime.tm_mon
    day = fulltime.tm_mday
    strmon = "%d" % (mon)
    stryear = "%d" % (year)
    print "HTTP/1.0 200 OK"
    print "Content-Type: text/html"
    print ""
    print "<html>"   
    print "<style type=\"text/css\">"
    print "    #mychart1 {"
    print "    width: 1340px;"
    print "    height: 600px;"
    print "}"
    print "</style>"
    print "<script src=\"http://yui.yahooapis.com/3.10.1/build/yui/yui-min.js\"></script>"
    print "<script language=\"javascript\" type=\"text/javascript\"> "
    print "YUI().use(\'charts\', function (Y) "
    print "{ "
    print "    var myDataValues1 = [ "
    for vari in range(1,32):
        response = "%d" % (sample_list[vari])
        #cmd = "select count(data) from user where year = %d and mon = %d and day = %d" % (year,mon,vari)
        #conn = httplib.HTTPConnection("localhost","8000")
       # conn.request("GET","/cgi-bin/database.py?"+cmd)
        #response = conn.getresponse() 
        stri = "%d" % (vari)
        if vari == 31:
            print "        {category:\""+stri+"\", action:"+response+"}"
        else :
            print "        {category:\""+stri+"\", action: "+response+"},"
    print "    ]; "
    print "    var mychart1 = new Y.Chart({dataProvider:myDataValues1, render:\"#mychart1\"});"
    print "});"
    print "</script> "
    print "<body align=\"center\" >"
    print "<div  \"center\" id=\"mychart1\"></div>"
    print "</body>"
    print "</html>"