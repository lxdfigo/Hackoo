import sqlite3
import sys
con=sqlite3.connect('yahoo')
cur=con.cursor()
con.isolation_level=None
i=0
cmd=""
for s in sys.argv:
    i=i+1
    if i>1:
        cmd=cmd+" "+s
rec=cur.execute(cmd)
#conn.commit()
print cur.fetchall()
