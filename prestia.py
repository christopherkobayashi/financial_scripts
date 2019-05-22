#! /usr/bin/env python2.7

import csv
import os
import unicodedata
import sys
import re
import time
from datetime import date
from datetime import datetime

print ('!Type:Bank')

with open( sys.argv[1], 'rb') as csvfile:
	rows = csv.reader(csvfile, delimiter=',')

	for row in rows:
		if not row:
			break
		year, month, day = row[0].split('/')
		trans_date = date(int(year), int(month), int(day))
		payee = row[1].decode('shift-jis').encode('utf-8')
		payee = unicodedata.normalize('NFKC', payee.decode('utf8'))
		payee = re.sub("\s\s+", " ", payee)
		amount = int( (row[2].replace(',','').split())[0])
		comment = row[3].replace('\'','')

		print ('D' + trans_date.strftime('%Y/%m/%d'))
		print ('T' + str(amount))
		print ('Cc')
		print ('P' + payee.encode('UTF-8'))
		print ('M' + comment.encode('UTF-8'))
		print ('^')