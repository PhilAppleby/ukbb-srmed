import time
import sqlite3
import os, sys
from optparse import OptionParser

def main(options):
  """
  Dump out the data for any sqllite table in the chembl db as a tab-separated variable file 
  Accepts an optional (simple) where clause and an optional row limit.
  """
  try:
    chembl = sqlite3.connect(os.environ["CHFILE"])
    chembl.text_factory = str
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print("Unexpected error:", sys.exc_info())
    exit()
  
  query = "select * from {0}".format(options.tablename)

  if options.where_clause != None:
    query += " {0}".format(options.where_clause)
  
  if options.limit != None:
    query += " limit {0}".format(options.limit)

  count = 0
  
  cursor = chembl.cursor()
  cursor.execute(query)
  for row in cursor:
    count += 1
    print('\t'.join([str(elem) for elem in row]))

  chembl.close()

  return count

# execution flow starts here
#
parser = OptionParser()

parser.add_option("-t", "--tablename", dest="tablename",
  help="Table name", metavar="STR")

parser.add_option("-w", "--where_clause", dest="where_clause",
  help="Optional where clause", metavar="STR")

parser.add_option("-l", "--limit", dest="limit",
  help="Optional row limit (suggest 1 at test-time", metavar="STR")

start_time = time.time()
(options, args) = parser.parse_args()

rcount = main(options)
#print "END:", time.time() - start_time, "seconds", rcount
