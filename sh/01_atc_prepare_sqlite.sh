#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Data preparation- get ATC classification data and generate synonyms
#
echo "Step 1 - Get ATC classification data from the CHEMBL Db"
time ${SHDIR}/chembl/get_chembl_atc_classification_data_sqlite.sh
echo "Step 2 - Preprocess ATC classification data"
time ${SHDIR}/preprocess_atc_data.sh
echo "Step 3 - Get and reorganise CHEMBL molecule synonyms"
time ${SHDIR}/get_molecule_synonyms_sqlite.sh

# Main file artefacts at the end of each step of this group of steps:

# 1) ${CDATADIR}/atc_classification_molregno.tsv
#
# 2) ${ATCDATADIR}/atc_who_desc.csv
#
# 3) ${CDATADIR}/syn_dict_all.txt
