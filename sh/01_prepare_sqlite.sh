#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Data preparation- get BNF classification data and generate synonyms
#
# NOTE: No step 1 here, BNF files must be supplied - this depends
# on local ownership of BNF data
#
echo "Step 2 - Preprocess BNF classification data"
time ${SHDIR}/preprocess_bnf_data.sh
echo "Step 3 - Get and reorganise CHEMBL molecule synonyms"
time ${SHDIR}/get_molecule_synonyms_sqlite.sh

# Main file artefacts at the end of each step of this group of steps:

# 2) ${BNFDATADIR}/bnf_combined.csv
#
# 3) ${CDATADIR}/syn_dict_all.txt
