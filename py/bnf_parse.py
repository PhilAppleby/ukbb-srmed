#
# Transform BNF code to formatted version
#
import time
import datetime
# import re
import os, sys
from datahelper import Datahelper

def main():
  count = 0
  dh = Datahelper()
  hdr = sys.stdin.readline().strip()
  print hdr

  for line in sys.stdin:
    count += 1
    data = line.strip().split(',')
    data[0] = dh.format_digit_code(data[0], 3)
    data[1] = data[1].lower()
    print ','.join(data)

  return count 

# execution flow starts here
#
start_time = time.time()

count = main()
#print "END:", time.time() - start_time, "seconds", count

