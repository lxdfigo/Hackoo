import sys
if __name__ == "__main__":    
    sample_list = [0,1132,4110,3120,1544,534]
    print "HTTP/1.0 200 OK"
    print "Content-Type: text/html"
    print ""
    print "<html>"   
    print "<style type=\"text/css\">"
    print "    #mychart1 {"
    print "    width: 600px;"
    print "    height: 600px;"
    print "}"
    print "</style>"
    print "<script src=\"http://yui.yahooapis.com/3.10.1/build/yui/yui-min.js\"></script>"
    print "<script language=\"javascript\" type=\"text/javascript\"> "
    print "YUI().use(\'charts\', function (Y) "
    print "{ "
    print "   var myDataValues1 = ["
    print "            {actions:\"<10\", days:%d}, " % (sample_list[1])
    print "            {actions:\"10-30\", days:%d}, " % (sample_list[2])
    print "            {actions:\"30-50\", days:%d}," % (sample_list[3])
    print "            {actions:\"50-70\", days:%d}," % (sample_list[4])
    print "            {actions:\">70\", days:%d}" % (sample_list[5])
    print "    ];"		
    print "    var pieGraph = new Y.Chart({	"	
    print "            render:\"#mychart1\", "
    print "            categoryKey:\"actions\", "
    print "            seriesKeys:[\"days\"], "
    print "            dataProvider:myDataValues1, "
    print "            type:\"pie\", "
    print "            seriesCollection:["
    print "                {"
    print "                    categoryKey:\"actions\","
    print "                    valueKey:\"days\""
    print "                }"
    print "            ]"
    print "        });"
    print "});"
    print "</script> "
    print "<body align=center >"
    print "<div  \"center\" id=\"mychart1\"></div>"
    print "</body>"
    print "</html>"