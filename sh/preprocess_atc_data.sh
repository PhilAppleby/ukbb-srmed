#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Preprocess the ATC classification data to cut the relevant columns
# Executed twice to capture both molregno and description
# Then to trim the ATC code to the required length (level3)
#
awk -F '\t' '{print $2 "\t" $3}' ${CDATADIR}/atc_classification_molregno.tsv | \
	grep -v None > ${CDATADIR}/atc_who_desc_fullcode.tsv
awk -F '\t' '{print $2 "\t" $1}' ${CDATADIR}/atc_classification_molregno.tsv >> \
	${CDATADIR}/atc_who_desc_fullcode.tsv
cat ${CDATADIR}/atc_who_desc_fullcode.tsv | \
	python ${PYDIR}/atc_parse.py --codelen=4 > ${ATCDATADIR}/atc_who_desc.csv
