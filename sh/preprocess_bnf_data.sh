#!/bin/sh
source ${UKBPROJROOT}/env/common
# Preprocess BNF files to cut the relevant columns, normalise
# coding and convert all text to lower case
#
# Local data Code + long description
cut -f 1,3 -d ',' ${BNFDATADIR}/bnf_data_formatted.csv  > ${BNFDATADIR}/bnf_data_1.csv
# Local data Code + approved_name
cut -f 1,4 -d ',' ${BNFDATADIR}/bnf_data_formatted.csv | sed '1d' > ${BNFDATADIR}/bnf_data_2.csv

# Cat the 2 result files from above, format the bnf code and convert all text to lower case
cat ${BNFDATADIR}/bnf_data_1.csv ${BNFDATADIR}/bnf_data_2.csv | python ${PYDIR}/bnf_parse.py > ${BNFDATADIR}/bnf_combined.csv 
