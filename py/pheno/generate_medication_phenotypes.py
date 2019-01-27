# 
# Generate binary phenotypes from the set of UKB
# participants reporting taking medications
# Load the column list as a code vs num array
#
# For each person, output a line which has 0's
# where the person has taken no medication in a category
# and 1's where they have
# HOW TO PROPERLY QC THIS?
import time
import datetime
import re
import os, sys
import random
import json
from optparse import OptionParser

def load_pheno_names(pfile):
  """
  Here the column order for the output file is set
  to the order of reading the file records
  """
  plookup = {}
  pcolnames = []
  col = 0

  hdr = pfile.readline()

  for line in pfile:
    data = line.strip().split(",")
    plookup[data[0]] = col
    pcolnames.append(data[1])
    col += 1

  return plookup, pcolnames

def main(options):
  count = 0
  synonyms = {}
  #codes = {}

  try:
    fh = open(options.pfile, "r")
    plookup, pcolnames = load_pheno_names(fh)
  except:
    print "Failed to open phenotype code file %s" % (options.pfile)
    sys.exit()

  #print "FID,IID,%s" % (",".join(pcolnames))
  print "FID\tIID\t%s" % ("\t".join(pcolnames))
  #print len(pcolnames) + 2

  last_eid = ""
  phen_array = ['0'] * len(pcolnames)

  for line in sys.stdin:
    data = line.strip().split(",")
    if data[0] != last_eid:
      if last_eid != "":
        #print "%s,%s,%s" % (last_eid, last_eid, ",".join(phen_array))
        print "%s\t%s\t%s" % (last_eid, last_eid, "\t".join(phen_array))
      phen_array = ['0'] * len(pcolnames)
      last_eid = data[0]
    if data[2] in plookup:
      phen_array[plookup[data[2]]] = '1'

  #print "%s,%s,%s" % (last_eid, last_eid, ",".join(phen_array))
  print "%s\t%s\t%s" % (last_eid, last_eid, "\t".join(phen_array))
  return count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
#
parser.add_option("-p", "--pfile", dest="pfile",
  help="phenotype code file", metavar="FILE")

(options, args) = parser.parse_args()

count = main(options)
#print "END:", time.time() - start_time, "seconds", count

