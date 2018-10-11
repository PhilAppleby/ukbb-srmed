#
# Trim ATC code to formatted version
# Calls d function in the datahelper class
#
import time
import datetime
import os, sys
from datahelper import Datahelper
from optparse import OptionParser

def main(options):
  dh = Datahelper()

  for line in sys.stdin:
    data = line.strip().split('\t')
    data[0] = dh.format_atc_code(data[0], int(options.codelen))
    data[1] = dh.get_normalised_phrase(data[1]).lower()
    print ','.join(data)
# End main()

# execution flow starts here
#
start_time = time.time()

parser = OptionParser()
parser.add_option("-l", "--codelen", dest="codelen",
  help="ATC code length", metavar="INT")
(options, args) = parser.parse_args()

main(options)

