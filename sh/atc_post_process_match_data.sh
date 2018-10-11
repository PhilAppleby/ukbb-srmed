#!/bin/sh
source ${UKBPROJROOT}/env/common
# Post process the ATC results files
#
# differentiate between unmatched and matched data
egrep -w "NA" ${ATCDATADIR}/results/atc_res.csv > \
	${ATCDATADIR}/results/atc_res_NA.csv
egrep -vw "NA" ${ATCDATADIR}/results/atc_res.csv > \
	${ATCDATADIR}/results/atc_res_NONA.csv
# add UKBB counts to matches and unmatches
cat ${ATCDATADIR}/results/atc_res_NA.csv | \
	python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > \
	${ATCDATADIR}/results/atc_missing.csv
cat ${ATCDATADIR}/results/atc_res_NONA.csv | \
	python ${PYDIR}/append_ukb_counts.py --ukbcfile=${UDATADIR}/UKB_counts.csv > \
	${ATCDATADIR}/results/atc_matched.csv
# one_word matches are the most risky
grep ":1," ${ATCDATADIR}/results/atc_matched.csv > \
	${ATCDATADIR}/results/atc_one_word_match_full.csv
cut -f 1,2,3,5,6 -d ',' ${ATCDATADIR}/results/atc_one_word_match_full.csv > \
	${ATCDATADIR}/results/one_word_match_list.csv

# Following steps extract data for manual examination / intervention
# all matches
cut -f 1,2,8 -d ',' ${ATCDATADIR}/results/atc_matched.csv > \
	${ATCDATADIR}/results/atc_matched_list.csv
sort ${ATCDATADIR}/results/atc_matched_list.csv > \
	${ATCDATADIR}/results/atc_matched_list_sorted.csv
# looking at missing data
cut -f 1,2,8 -d ',' ${ATCDATADIR}/results/atc_missing.csv > \
	${ATCDATADIR}/results/atc_unmatched_list.csv
sort ${ATCDATADIR}/results/atc_unmatched_list.csv > \
	${ATCDATADIR}/results/atc_unmatched_list_sorted.csv
# unique matched UKBB ids
cut -f 1,2 -d ',' ${ATCDATADIR}/results/atc_matched.csv | \
	sort -u > ${ATCDATADIR}/results/atc_matched_unique.csv
cut -f 1,2 -d ',' ${ATCDATADIR}/results/atc_matched.csv | \
	sort | \
	uniq -c | \
	sort -nr > ${ATCDATADIR}/results/atc_match_counts.csv

