import sys
if __name__ == "__main__":    
    sample_list = [0,132,310,120,414,234,124,12,345,741,212,312,451,315]
    print "HTTP/1.0 200 OK"
    print "Content-Type: text/html"
    print ""
    print "<html>"   
    print "<style type=\"text/css\">"
    print "    body{"
    print "    text-align:center;"
    print "    margin:auto;"
    print "    }"
    print "    #mychart1 {"
    print "    width: 1335px;"
    print "    height: 600px;"
    print "}"
    print "</style>"
    print "<script src=\"http://yui.yahooapis.com/3.10.1/build/yui/yui-min.js\"></script>"
    print "<script language=\"javascript\" type=\"text/javascript\"> "
    print "YUI().use(\'charts\', function (Y) "
    print "{ "
    print "    var myDataValues1 = [ "

    for vari in range(1,13):
        response = "%d" % (sample_list[vari])
        #cmd = "select count(data) from user where year = %d and mon = %d % (year,vari)
        #conn = httplib.HTTPConnection("localhost","8000")
       # conn.request("GET","/cgi-bin/database.py?"+cmd)
        #response = conn.getresponse() 
        stri = "%d" % (vari)
        if vari == 12:
            print "        {category:\""+stri+"\", action:"+response+"}"
        else :
            print "        {category:\""+stri+"\", action: "+response+"},"

#    print "        {category:\"5/1/2010\", action:2000}, "
#    print "        {category:\"5/2/2010\", action:50}, "
#    print "        {category:\"5/3/2010\", action:400}, "
#    print "        {category:\"5/4/2010\", action:200}, "
#    print "        {category:\"5/5/2010\", action:5000}"
    print "    ];"
    print "    var mychart1 = new Y.Chart({"
    print "        dataProvider: myDataValues1,"
    print "        render: \"#mychart1\","
    print "        type: \"column\"" 
    print "    });"
    print "});"
    print "</script> "
    print "<body align=\"center\" >"
    print "<div  \"center\" id=\"mychart1\"></div>"
    print "</body>"
    print "</html>"