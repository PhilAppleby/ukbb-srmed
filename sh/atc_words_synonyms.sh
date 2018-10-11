#!/bin/sh
source ${UKBPROJROOT}/env/common
#
#   CHEMBL synonyms have been attached to both ATC classification data
#   and UKB coding data 
#   This is the main match process - the result file contains code matches
# 
#
cat ${UDATADIR}/medication_coding_synonyms.csv | \
	python ${PYDIR}/code_data_match.py --clsfile=${ATCDATADIR}/atc_who_desc_synonyms.csv > \
	${ATCDATADIR}/results/atc_res.csv
