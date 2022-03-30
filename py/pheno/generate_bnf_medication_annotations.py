import time
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def load_code_list(fh):
  lookup = {}
  for line in fh:
    codedata = line.strip().split("|")
    lookup[codedata[0]] = codedata[1]
 
  return lookup

def main(options):
  """
  """

  dh = Datahelper()
  try:
    fh = open(options.bnfcodes, "r")
    code_lookup = load_code_list(fh)
  except:
    print("Unexpected error:", sys.exc_info())
    exit()

  print "pheno,PHENOTYPE,Category,type"

  count = 0
  for line in sys.stdin:
    data = line.strip().split(',')
    count = 0
  
    if data[0] in code_lookup:
      count += 1
      pheno_string = dh.get_normalised_phrase(code_lookup[data[0]])
      pheno_string = dh.make_pheno_string(pheno_string)
      #data.append(data[0] + "_" + pheno_string)
      data.append(data[0])
      data.append(pheno_string)
      data.append("BINARY")
      print(','.join(data))

  return count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
parser.add_option("-b", "--bnfcodes", dest="bnfcodes",
  help="bnfcodes", metavar="FILE")

(options, args) = parser.parse_args()

rcount = main(options)
#print "END:", time.time() - start_time, "seconds", rcount
