import sys
if __name__ == "__main__":
    print "HTTP/1.0 200 OK"
    print "Content-Type: text/html"
    print ""
    print "<p>"
    print sys.argv[1]
    print "</p>"
    #print >>fout,sys.argv[1]