#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Generate UKB medication data phenotypes
#
echo "Step 11 - Generate BNF phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_bnf.sh
echo "Step 12 - Generate BNF phenotypes, version 2"
time ${SHDIR}/pheno/normalise_bnf_codes.sh
