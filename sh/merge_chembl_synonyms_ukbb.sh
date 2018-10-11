#!/bin/sh
source ${UKBPROJROOT}/env/common
# 
# Merge chembl synonyms with UKBB medication coding data: chembl synoyms 
# from the CHEMBL database, UKBB coding data from the UK Biobank data showcase
# 

cat ${UDATADIR}/medication_coding.csv | \
	python ${PYDIR}/merge_chembl_synonyms.py --synfile=${CDATADIR}/syn_dict_all.txt > \
	${UDATADIR}/medication_coding_synonyms.csv 
