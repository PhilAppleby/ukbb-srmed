import time
import pymysql
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main(options):
  """
  Access the CHEMBL db for each input line and use the description
  from the appropriate level
  """

  level = int(options.level)

  dh = Datahelper()
  try:
    chembl = pymysql.connect(host=os.environ["CHHOST"], user=os.environ["CHUSER"],  passwd=os.environ["CHPWD"],
             port=int(os.environ["CHPORT"]), db=os.environ["CHDB"])
  except:
    #print "Unexpected error:", sys.exc_info()[0]
    print("Unexpected error:", sys.exc_info())
    exit()

  print("pheno,PHENOTYPE,Category,type")

  count = 0
  for line in sys.stdin:
    data = line.strip().split(',')
    atc_code = data[0]
    query = "select level{0}_description from atc_classification where level{1} = '{2}' limit 1".format(level, level, atc_code)
    count = 0
  
    cursor = chembl.cursor()
    cursor.execute(query)
    for row in cursor:
      count += 1
      pheno_string = dh.get_normalised_phrase(row[0])
      pheno_string = dh.make_pheno_string(pheno_string)
      data.append(data[0] + "_" + pheno_string)
      data.append(pheno_string)
      data.append("BINARY")
      print(','.join(data))

  chembl.close()
  return count

# execution flow starts here
#
start_time = time.time()
parser = OptionParser()
parser.add_option("-l", "--level", dest="level",
  help="ATC level", metavar="INT")
(options, args) = parser.parse_args()

rcount = main(options)
#print "END:", time.time() - start_time, "seconds", rcount
