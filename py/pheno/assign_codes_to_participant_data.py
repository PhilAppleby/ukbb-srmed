# 
# Assign Classification System codes to participant data
# Outputs "NA" where no code is present
# 
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser
from datahelper import Datahelper

def load_cs_codes(fh):
  code_lookup = {}

  for line in fh:
    data = line.strip().split(',')
    if data[0] not in code_lookup:
      code_lookup[data[0]] = []
    code_lookup[data[0]].append(data[2])

  return code_lookup

def main(options):
  count = 0
  match_count = 0
  miss_count = 0
  dh = Datahelper()

  try:
    fh = open(options.codefile, "r")
    code_lookup = load_cs_codes(fh)
    #print len(synonyms)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()
  except TypeError as e:
    print "Missing arguments ", e
    exit()
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print "Unexpected error:", sys.exc_info()
    exit()

  hdr = sys.stdin.readline().strip()
  print "%s,%s" % (hdr, "cs_code")

  for line in sys.stdin:
    count += 1
    data = line.strip().split(',')
    data.append("NA")
    if data[1] in code_lookup:
      for code in code_lookup[data[1]]:
        data[-1] = code
        match_count += 1
        print ",".join(data)
    else:
      miss_count += 1
      print ",".join(data)

  return count, match_count, miss_count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-c", "--codefile", dest="codefile",
  help="UKBB vs CS code file", metavar="FILE")

(options, args) = parser.parse_args()

count, ycount, ncount = main(options)
#print "END:", time.time() - start_time, "seconds", count, ycount, ncount

