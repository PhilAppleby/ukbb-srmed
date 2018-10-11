#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Wrap the pheno/transpose_pheno_data.sh script, supplying parameters
# for medication data
#
echo "Step 9 - Transpose medication phenotype data, eliminating empty cells"
time ${SHDIR}/pheno/transpose_pheno_data.sh reported_medication 20003
