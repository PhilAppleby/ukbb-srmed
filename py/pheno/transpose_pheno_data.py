#
# print records for all participants for all codes found in the input (eliminates blank records)
#
# NOTE: Assumes relevant data starts in the second column (1) - (eid) is the first column (0).
# 
import time
import datetime
import re
import os, sys
import random
import json

def main():

  codes = []
  count = 0
  hdr = sys.stdin.readline()
  print "eid,code"

  for line in sys.stdin:
    data = line.strip().split(',')
    for elem in data[1:]:
      if elem != "":
        print "%s,%s" % (data[0], elem)

  return count 


# execution flow starts here
#
start_time = time.time()

count = main()
#print "END:", time.time() - start_time, "seconds", count

