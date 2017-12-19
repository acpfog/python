#!/usr/bin/python

import re
import MySQLdb
import datetime
from sys import stdin
from email.Parser import Parser

# load a message data from stdin and extract a subject of the message 
message = Parser().parse(stdin)
subject = message.get('Subject')

# start processing if the subject about a delivery failure
if subject == 'Delivery Status Notification (Failure)':

# open the log file, then write a starting record
    f = open('/storage/project/logs/dead_email_addresses_parser.log', 'a')

    now = datetime.datetime.now()
    print >>f, "%s #1 A message with Failure Delivery Notification was detected" % (str(now))

# extract a body of the message
    if not message.is_multipart():
        body = message.get_payload(decode=True)
    else:
        for part in message.get_payload():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)

# generate an expression and look for e-mail addresses in the body
    r = re.compile(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
    results = r.findall(body)    

# connect to a database
    db = MySQLdb.connect("127.0.0.1","db_user","db_pass","db_name" )
    cursor = db.cursor()

# check and store each new e-mail address in the dead_email_addresses table and write to the log
    for x in results:

        now = datetime.datetime.now()
        print >>f, "%s #2 Email address %s was found in the message" % (str(now), x)

        sql = "SELECT * FROM dead_email_addresses WHERE email_address = '%s'" % (x)
        number_of_rows = cursor.execute(sql)

        if number_of_rows == 0:

            now = datetime.datetime.now()
            print >>f, "%s #3 Email address %s was stored in database" % (str(now), x)

            sql = "INSERT INTO dead_email_addresses (date, email_address) VALUES (CURRENT_TIMESTAMP(), '%s')" % (x)
            cursor.execute(sql)
    
    db.close()
    f.close()
 
