#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Wrap the pheno/cut_pheno_cols.sh script, supplying parameters
# for medication data - US only as that's where the main
# UKB csv file resides
#
echo "Step 8 - Extract medication phenotype from the main UKBB file"
time ${SHDIR}/pheno/cut_pheno_cols.sh reported_medication 20003
