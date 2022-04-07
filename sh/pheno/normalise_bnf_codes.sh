#!/bin/sh
source ${UKBPROJROOT}/env/common
echo '.1 cat BNF coded for conversion' ${UKBPDIR}
cat ${UKBPDIR}/ukb_20003_with_bnf_codes_matched_sorted.csv \
	| python ${PYDIR}/pheno/normalise_bnf_codes.py \
	> ${UKBPDIR}/bnf_chapter_section_subsection_counts.csv
#------------------------------------------------------------------------------------------------
echo 'END'
