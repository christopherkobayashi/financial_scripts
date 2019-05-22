#! /usr/bin/env python2.7

# This script takes the ofx.qif output from American Express Japan website,
# converts to Unicode, calculates foreign exchange rate if any, and emits a
# QIF.

import csv
import os
import unicodedata
import sys
import re
import time
from decimal import *
from datetime import date
from datetime import datetime

with open ( sys.argv[1], 'r' ) as file:
	for line in file:
		line = line.decode('shift-jis').encode('utf-8')
		line = unicodedata.normalize('NFKC', line.decode('utf8'))
		line = re.sub("\s\s+", " ", line)
		line = line.rstrip(" ")
		if line:
			if line[0] == "T":
				amount = abs(float(line[1:].replace(',','')))
				line = line.replace(',','')
			if line[0] == "M" and len(line) > 2:
				forex = line.split(" ")
				orig_currency = forex[1]
				orig_amount = forex[0].replace(',','')
				orig_amount = float(orig_amount[1:])
				rate = amount / orig_amount
				line = line + " rate: " + str(rate) + " " + str(orig_currency) + "/JPY"
			if line[0] == "P":
				rep = u"\u2212"
				line = line.replace("?", rep)
		print (line.encode('UTF-8'))
