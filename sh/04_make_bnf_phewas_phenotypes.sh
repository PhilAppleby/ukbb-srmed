#!/bin/sh
source ${UKBPROJROOT}/env/common
#
# Generate UKB medication data phenotypes
#
echo "Step 11 - Generate BNF phenotypes"
time ${SHDIR}/pheno/make_ukb_phenotypes_bnf.sh
