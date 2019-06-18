#!/bin/sh
source ${UKBPROJROOT}/env/common
echo '.1 sort BNF coded data to' ${UKBPDIR}
cat ${UKBPDIR}/ukb_20003_with_bnf_codes_matched.csv | \
  sort -u  > ${UKBPDIR}/ukb_20003_with_bnf_codes_matched_sorted.csv

# step 2 get the list of possible phenotypes
echo '.2 extract list of possible phenotype to' ${UKBPDIR}
cut -f 3 -d ',' ${UKBPDIR}/ukb_20003_with_bnf_codes_matched_sorted.csv | \
  sort -u > ${UKBPDIR}/ukb_possible_med_phenotypes_bnf.csv

# step 3 generate phenotype annotations, get data from the BNF description file
echo '.3 Get data from bnf desc file, write to' ${UKBPDIR}
cat ${UKBPDIR}/ukb_possible_med_phenotypes_bnf.csv | \
  python ${PYDIR}/pheno/generate_bnf_medication_annotations.py \
  --bnfcodes=${BNFCODEDIR}/bnf_listing.txt > \
  ${UKBPDIR}/Anno_medications_BIN_bnf.csv

# step 4 generate phenotypes
echo '.4 write PheWAS phenos to' ${UKBPDIR}
cat ${UKBPDIR}/ukb_20003_with_bnf_codes_matched_sorted.csv | \
  python ${PYDIR}/pheno/generate_medication_phenotypes.py \
  --pfile=${UKBPDIR}/Anno_medications_BIN_bnf.csv > \
  ${UKBPDIR}/med_phenotypes_bnf.tsv
#------------------------------------------------------------------------------------------------
echo 'END'
