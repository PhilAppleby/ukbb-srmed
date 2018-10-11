# 
# Second step in the chembl synonym generation pipeline:
# python ${PYDIR}/chembl/dump_mysql_table_data.py --tablename=molecule_synonyms | \
#   sort -k1,1 -n | \
#   python ${PYDIR}/parse_chembl_synonyms.py | \
#   python ${PYDIR}/generate_syn_dictionary.py > ${CDATADIR}/syn_dict_all.txt
#
# 
import time
import datetime
import re
import os, sys
import random
import json
from datahelper import Datahelper

def main():
  """
  Requires the input to be sorted on the first field (the numeric molregno).
  One record per molregno is output.

  Calls a datahelper function to normalise each word or phrase (convert to 
  lower case and remove special characters)
  """
  count = 0
  last_molno = ""
  related_synonyms = []
  dh = Datahelper()

  for line in sys.stdin:
    data = line.strip().split('\t')
    if data[0] != last_molno and last_molno != "":
      print '|'.join(related_synonyms) + "|MOLREGNO:" + last_molno
      related_synonyms = []
    last_molno = data[0]
    text = dh.get_normalised_phrase(data[1])
    stype = data[2]
    syn = stype + ":" + text
    if syn not in related_synonyms:
      related_synonyms.append(syn)

  # output the last synonym group
  print '|'.join(related_synonyms) + "|MOLREGNO:" + last_molno

# execution flow starts here
#
start_time = time.time()

count = main()

