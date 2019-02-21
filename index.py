#!/usr/bin/env python

import time

from datetime import datetime
today = datetime.now()
day = today.day
month = today.month
year = today.year



print "Content-type: text/html\n\n"
print "<html>\n<body>"

print "<meta http-equiv=\"refresh\" content=\"1\" >"

print "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">"
#print "<h1>Python Script Test Page</h1>"
print "<h1>Curso de Python Script</h1>"
print "Data: ", time.strftime('%d %b %Y'),time.strftime ('%H:%M:%S')


print "</div>\n</body>\n</html>"
