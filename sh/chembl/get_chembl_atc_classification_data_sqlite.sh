#!/bin/sh
source ${UKBPROJROOT}/env/common
# Join atc_classification and atc_molecule_classication
#
python ${PYDIR}/chembl/get_atc_data_with_molregno_sqlite.py > \
	${CDATADIR}/atc_classification_molregno.tsv 
