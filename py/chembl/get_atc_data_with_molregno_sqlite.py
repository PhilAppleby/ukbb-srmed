import time
import sqlite3
import os, sys
from optparse import OptionParser
#
# Access the publicly available CHEMBL database (local copy) to
# obtain ATC (WHO) classification data
#
#
def main():
  """
  Get atc data for use in classifying UKBB coded medication data
  Requires a join of the CHEMBL atc_classification and molecule_atc_classification tables
  """
  try:
    chembl = sqlite3.connect(os.environ["CHFILE"])
    chembl.text_factory = str
  except:
    print("Unexpected error:", sys.exc_info())
    exit()

  query = """select atc.who_name, atc.level5, matc.molregno, atc.level4_description 
             from atc_classification atc 
             LEFT JOIN molecule_atc_classification matc 
             ON atc.level5 = matc.level5"""
  
  cursor = chembl.cursor()
  cursor.execute(query)
  for row in cursor:
    print('\t'.join([str(elem) for elem in row]))

  chembl.close()
  # main() ends


# execution flow starts here
#
start_time = time.time()

main()
