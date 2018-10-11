# The main text match process
#
# Dictionaries:
# 
# Classification system code file data fields:
# 1 the code
# 2 the description
# 3 synonyms added from CHEMBL (separated by '|')
# 
import time
import datetime
import re
import string
import os, sys
from optparse import OptionParser
from datahelper import Datahelper

def main(options):
  """
  The main match process - look up descriptions and 
  synonyms in the coding data dictionary (loaded
  on initialisation
  SEE ALSO: datahelper.py
  """
  dcount = 0
  count = 0
  match_count = 0
  miss_count = 0

  # try to load the classification system codes file
  try:
    fh = open(options.clsfile, "r")
    dh = Datahelper()
    dcount = dh.load_cls_phrases(fh)
    #print "Dictionary size = %d" % (dcount)
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

  # stdin used to read in medications coding data
  hdr = sys.stdin.readline()
  for line in sys.stdin:
    count += 1
    matched = False
    data = line.strip().split(',')
    all_phrases = [data[1]]
    if len(data) == 3:
      all_phrases += data[2].split('|')

    match_string = ""
    code_array, match_data, last_match, selected_code = dh.match_all_phrases(all_phrases)
    if len(code_array) > 0:
      if (options.multioutput == True): 
        # Current policy: output one line per code match (can be multiple per input record
        for code_elem in code_array:
          code_data = code_elem.split("~")
          print "%s,%s,%s,%s,%s,%s,%d" % (data[0], data[1], last_match, '|'.join(match_data), code_data[1], code_data[0], len(code_array))
      else:
        print "%s,%s,%s,%s,%s,%s,%d" % (data[0], data[1], last_match, '|'.join(match_data), 0, selected_code, len(code_array))
      match_count += 1
    else:      
      print "%s,%s,%s,%s,%s,%s,0" % (data[0], data[1], last_match, '|'.join(match_data), "NA", "NA")
      miss_count += 1

  return count, match_count, miss_count 


# execution flow starts here
#
parser = OptionParser()
parser.add_option("-b", "--clsfile", dest="clsfile",
  help="file contains input classification system codes and descriptions", metavar="FILE")
parser.add_option("-m", "--multioutput", dest="multioutput",
  help="output multiple classification codes per source system line", metavar="STR")

start_time = time.time()
(options, args) = parser.parse_args()

if options.multioutput == "Y":
  options.multioutput = True
else:
  options.multioutput = False

count, match_count, miss_count = main(options)
#print "END:", time.time() - start_time, "seconds", count, match_count, miss_count

