# 
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def load_count_data(fh):
  ukbb_counts = {}

  for line in fh:
    data = line.strip().split(',')
    ukbb_counts[data[0]] = data[1]

  return ukbb_counts

def main(options):
  count = 0
  last_molno = ""
  related_synonyms = []

  # try to load the UK counts file
  try:
    fh = open(options.ukbcfile, "r")
    ukbb_counts = load_count_data(fh)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    print "I/O error:", sys.exc_info()
    exit()
  except TypeError as e:
    print "Missing arguments ", e
    exit()
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  for line in sys.stdin:
    data = line.strip().split(',')
    count = '0'
    if data[1] in ukbb_counts:
      count = ukbb_counts[data[1]]
    data.append(count)
    #if int(count) > 10:
    #  print ','.join(data)
    print ','.join(data)
# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-u", "--ukbcfile", dest="ukbcfile",
  help="UKB count file", metavar="FILE")

(options, args) = parser.parse_args()

count = main(options)
#print "END:", time.time() - start_time, "seconds", count

