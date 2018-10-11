#!/bin/sh
source ${UKBPROJROOT}/env/common
# The Match steps:
# BNF and UKBB data synonym merging,
#
# All BNF codes and descriptions:
# UKBB side - has synonyms
# BNF side - has synonyms
#
#
echo "Step 4 - Merge CHEMBL molecule synonyms and BNF classification data"
time ${SHDIR}/merge_chembl_synonyms_bnf.sh
echo "Step 5 - Merge CHEMBL molecule synonyms and UKB self-reported medication data"
time ${SHDIR}/merge_chembl_synonyms_ukbb.sh
echo "Step 6 - The main matching step - attempt to assign BNF codes to UKBB data"
time ${SHDIR}/bnf_words_synonyms.sh
echo "Step 7 - Post process match / mismatch data to format for manual intervention and phenotype generation"
time ${SHDIR}/bnf_post_process_match_data.sh

# Main output files at the end of each step:

# 4) ${BNFDATADIR}/bnf_combined_synonyms.csv

# 5) ${UDATADIR}/medication_coding_synonyms.csv

# 6) ${BNFDATADIR}/results/bnf_res.csv

# 7) ${BNFDATADIR}/results/bnf_matched.csv and ${BNFDATADIR}/results/bnf_missing.csv (which is then used to assign manual matches) 
