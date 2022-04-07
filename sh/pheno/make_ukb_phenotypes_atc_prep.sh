#!/bin/sh
source ${UKBPROJROOT}/env/common
# 
# Assign ATC level3 codes to participant,medication data 
# Includes steps to cut only the relevant columns from matched data 
# and to combine automatically matched data with manually 
# assigned codes
#
# Just get the matches from the manually edited file
cp -f  ${ATCDATADIR}/results/atc_manual_matches.csv ${ATCDATADIR}/results/atc_manual_matches.csv.BAK
egrep -vw "UKBB_code|NA" ${ATCDATADIR}/results/atc_manual_matches.csv > \
  ${ATCDATADIR}/results/atc_manual_matches_detail.csv
# Cut relevant columns
cut -f 1,2,5 -d ',' ${ATCDATADIR}/results/atc_manual_matches_detail.csv > \
  ${ATCDATADIR}/results/atc_manual_matches_cut.csv
cut -f 1,2,6 -d ',' ${ATCDATADIR}/results/atc_matched.csv > \
  ${ATCDATADIR}/results/atc_auto_matches_cut.csv

# Combine auto and manually matched codes
cat ${ATCDATADIR}/results/atc_auto_matches_cut.csv \
  ${ATCDATADIR}/results/atc_manual_matches_cut.csv > \
  ${ATCDATADIR}/results/atc_all_matches.csv 

# Assign codes where possible to all items in the reported medication list
cat ${UKBPDIR}/ukb_20003_reported_medication_n.csv | \
  python ${PYDIR}/pheno/assign_codes_to_participant_data.py \
    --codefile=${ATCDATADIR}/results/atc_all_matches.csv > \
  ${UKBPDIR}/ukb_20003_with_atc_codes.csv

# Get list of unmatched participant medication data
grep -w NA ${UKBPDIR}/ukb_20003_with_atc_codes.csv > \
  ${UKBPDIR}/ukb_20003_with_atc_codes_unmatched.csv

# Get list of matched participant medication data (without a header) this
# will feed into phenotype generation
grep -wv NA ${UKBPDIR}/ukb_20003_with_atc_codes.csv | sed '1,1d' > \
  ${UKBPDIR}/ukb_20003_with_atc_codes_matched.csv

