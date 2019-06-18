#!/bin/sh
source ${UKBPROJROOT}/env/common
# Post process the BNF results files
#
egrep -w "NA" ${BNFDATADIR}/results/bnf_res.csv > ${BNFDATADIR}/results/bnf_res_NA.csv
egrep -vw "AMB|NA" ${BNFDATADIR}/results/bnf_res.csv > ${BNFDATADIR}/results/bnf_res_NONA.csv
# add UKBB counts to matches and unmatches
cat ${BNFDATADIR}/results/bnf_res_NA.csv | python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > ${BNFDATADIR}/results/bnf_missing.csv
cat ${BNFDATADIR}/results/bnf_res_NONA.csv | python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > ${BNFDATADIR}/results/bnf_matched.csv
# one_word matches are the most risky
grep ":1," ${BNFDATADIR}/results/bnf_matched.csv > ${BNFDATADIR}/results/bnf_one_word_match_full.csv
cut -f 1,2,3,5,6 -d ',' ${BNFDATADIR}/results/bnf_one_word_match_full.csv > ${BNFDATADIR}/results/one_word_match_list.csv

# all matched data
cut -f 1,2,6 -d ',' ${BNFDATADIR}/results/bnf_matched.csv > ${BNFDATADIR}/results/bnf_matched_list.csv
sort ${BNFDATADIR}/results/bnf_matched_list.csv > ${BNFDATADIR}/results/bnf_matched_list_sorted.csv
# looking at missing data 
cut -f 1,2,8 -d ',' ${BNFDATADIR}/results/bnf_missing.csv > ${BNFDATADIR}/results/bnf_unmatched_list.csv
sort ${BNFDATADIR}/results/bnf_unmatched_list.csv > ${BNFDATADIR}/results/bnf_unmatched_list_sorted.csv
# unique matched UKBB ids
cut -f 1,2 -d ',' ${BNFDATADIR}/results/bnf_matched.csv | sort -u > ${BNFDATADIR}/results/bnf_matched_unique.csv
cut -f 1,2 -d ',' ${BNFDATADIR}/results/bnf_matched.csv | sort | uniq -c | sort -nr > ${BNFDATADIR}/results/bnf_match_counts.csv

