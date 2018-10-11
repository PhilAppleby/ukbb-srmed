#!/bin/sh
source ${UKBPROJROOT}/env/common
# Extract UKBB SR medication data
#
echo "Step 8 - Extract phenotype information from the UKBB main phenotype file"
time ${SHDIR}/pheno/medication_pheno_extract.sh
echo "Step 9 - Transpose extracted phenotype data"
time ${SHDIR}/pheno/medication_pheno_transpose.sh
echo "Step 10 - Prepare ATC data for phenotype generation"
time ${SHDIR}/pheno/make_ukb_phenotypes_atc_prep.sh
