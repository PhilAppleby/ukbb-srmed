# 
import time
import datetime
import re
import string
import os, sys
from optparse import OptionParser
from datahelper import Datahelper

def main():

  try:
    dh = Datahelper()
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

  ewords = dh.get_excluded_words()

  count = 0
  outarray = []
  for wd in ewords:
    count += 1
    outarray.append(wd)
    if count % 4 == 0:
      print ",".join(outarray)
      outarray = []
  if len(outarray) > 0:
    print ",".join(outarray)
  print count

  return 


# execution flow starts here
#
main()
#print "END:", time.time() - start_time, "seconds", count, match_count, miss_count

