#
# Cuts columns of interest from the main UKB phenotype cvs file
#
# Takes account of multiple column version contained within the file by matching column prefixes
# in column headers
#
# Always outputs the eid field as the first one, followed by any column with the required prefix 
#
import time
import datetime
import os, sys
import csv
from optparse import OptionParser

start_time = time.time()
sys.stdout.flush()

def main(options):
  csvreader = None
  count=0

  try:
    csvfile =  open(options.csvfile, "r")
    csvreader = csv.reader(csvfile)
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    exit()
  except TypeError as e:
    print "Missing arguments ", e
    exit()
  except:
    print "Unexpected error:", sys.exc_info()
    sys.exit()

  colprefs = options.colprefs.split(',')
  #print colprefs
  cols = []
  outhdr = []

  try:
    hdr = csvreader.next()
    #print len(hdr)
    outhdr.append(hdr[0])
    cols.append(0)
    # Process the header record to capture column indices and build the output 
    # header record
    for colpref in colprefs:
      for i, col in enumerate(hdr):
        coldata=col.split('-')
        if coldata[0] == colpref:
          outhdr.append(col)
          #print i, coldata
          cols.append(i)
    print ",".join(outhdr)
    #print cols
    #print len(outhdr)

    for row in csvreader:
      outrec=[]
      count += 1
      # iterate over each row element
#      for i,elem in enumerate(row):
#        if i in cols:
#          outrec.append(elem)
      for idx in cols:
        outrec.append(row[idx])
      print ",".join(outrec)
  except:
    print "Unexpected error (2):", sys.exc_info()[0]
    print sys.exc_info()
    sys.exit()

  return count
#
# execution flow starts here
#
parser = OptionParser()
parser.add_option("-c", "--csvfile", dest="csvfile",
  help="csv file containing main UKB data", metavar="FILE")
# col prefixes are comma separated - no complaint is made if a prefix doesn't exist in the data
parser.add_option("-p", "--colprefs", dest="colprefs",
  help="UKB column prefixes", metavar="FILE")


(options, args) = parser.parse_args()
#
rec_count = main(options)
#print "END:", time.time() - start_time, "seconds", rec_count


