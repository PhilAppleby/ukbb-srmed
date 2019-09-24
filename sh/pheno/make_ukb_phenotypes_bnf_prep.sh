#!/bin/sh
source ${UKBPROJROOT}/env/common
# 
# Just get the matches from the manually edited file
#egrep -vw "UKBB_code|NA" ${BNFDATADIR}/results/bnf_all_manual_matches.csv > \
#  ${BNFDATADIR}/results/bnf_manual_matches.csv
# Cut relevant columns
#cut -f 1,2,5 -d ',' ${BNFDATADIR}/results/bnf_manual_matches.csv > \
#  ${BNFDATADIR}/results/bnf_manual_matches_cut.csv
#cut -f 1,2,6 -d ',' ${BNFDATADIR}/results/bnf_matched.csv > \
#  ${BNFDATADIR}/results/bnf_all_matches.csv

# Combine auto and manually matched codes
#cat ${BNFDATADIR}/results/bnf_auto_matches_cut.csv \
#  ${BNFDATADIR}/results/bnf_manual_matches_cut.csv > \
#  ${BNFDATADIR}/results/bnf_all_matches.csv 

# Assign codes where possible to all items in the reported medication list
cat ${UKBPDIR}/ukb_20003_reported_medication_n.csv | \
  python ${PYDIR}/pheno/assign_codes_to_participant_data.py \
    --codefile=${BNFDATADIR}/results/bnf_all_matches.csv > \
  ${UKBPDIR}/ukb_20003_with_bnf_codes.csv

# Get list of unmatched participant medication data
grep -w NA ${UKBPDIR}/ukb_20003_with_bnf_codes.csv > \
  ${UKBPDIR}/ukb_20003_with_bnf_codes_unmatched.csv

# Get list of matched participant medication data (without a header) this
# will feed into phenotype generation
grep -wv NA ${UKBPDIR}/ukb_20003_with_bnf_codes.csv | sed '1,1d' > \
  ${UKBPDIR}/ukb_20003_with_bnf_codes_matched.csv

