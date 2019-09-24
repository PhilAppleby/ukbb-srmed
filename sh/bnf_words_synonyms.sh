#!/bin/sh
source ${UKBPROJROOT}/env/common
# Match words in medication_coding.tsv (The UKBB site has tis as coding4.tsv - download link
# was http://biobank.ctsu.ox.ac.uk/showcase/coding.cgi?id=4 as at 20171019
#
# bnf_combined.csv is a mashup of words from both the chemical names file and from HIC's bnf file
# CAN WE USE THIS
# Advantages are that it has proprietary names and chem name
#
cat ${UDATADIR}/medication_coding_synonyms.csv | python ${PYDIR}/code_data_match.py \
	--clsfile=${BNFDATADIR}/bnf_combined_synonyms.csv \
	--multioutput=N \
	> ${BNFDATADIR}/results/bnf_res.csv
