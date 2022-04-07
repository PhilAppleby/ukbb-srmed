# Load BNF codes and match them in the chapter.section count file
# 
import time
import datetime
import re
import os, sys

start_time = time.time()

def main():

  print("id,icd9,count")
  bnf_col = 2
  
  for line in sys.stdin:
    data = line.strip().split(",")
    bnf_code = ""
    bnf_array = data[bnf_col].split(".")
    if bnf_array[0] == "DU":
      continue
    if bnf_array[0] == "NULL":
      continue
    if len(bnf_array) == 1:
      bnf_code = "{0:02d}".format(int(bnf_array[0]))
    elif len(bnf_array) == 2:
      bnf_code = "{0:02d}{1:02d}".format(int(bnf_array[0]), int(bnf_array[1]))
    elif len(bnf_array) == 3:
      bnf_code = "{0:02d}{1:02d}{2:02d}".format(int(bnf_array[0]), int(bnf_array[1]), int(bnf_array[2]))
    print("{},{},{}".format(data[0], bnf_code, 10))
  return


# execution flow starts here
#
main()
#print "END:", time.time() - start_time, "seconds", rec_count

