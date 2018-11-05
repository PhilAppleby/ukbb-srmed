#!/bin/sh
#source ${UKBPROJROOT}/env/common
# Take a multi column file extraced for a phenotype from 
# the main UKB csv file and output one record per participant
# per phenotype code
#
# must supply arg1, arg2 only (descriptive name and column prefix)
if [[ $# -ne 2 ]] ; then
    echo 'must supply arg1, arg2 only (descriptive name and column prefix)'
    exit 1
fi

cat  ${UKBPDIR}/ukb_${2}_${1}.csv | \
  python ${PYDIR}/pheno/transpose_pheno_data.py > ${UKBPDIR}/ukb_${2}_${1}_n.csv
