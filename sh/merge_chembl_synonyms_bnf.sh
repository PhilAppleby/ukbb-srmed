#!/bin/sh
source ${UKBPROJROOT}/env/common
# Merge bulk BNF data (ownership uncertain, possibly HIC) with 
# synonyms from the CHEMBL database
#
cat ${BNFDATADIR}/bnf_combined.csv | \
  python ${PYDIR}/merge_chembl_synonyms.py --synfile=${CDATADIR}/syn_dict_all.txt > \
  ${BNFDATADIR}/bnf_combined_synonyms.csv 
