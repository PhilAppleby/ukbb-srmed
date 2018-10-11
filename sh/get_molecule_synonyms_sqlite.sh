#!/bin/sh
source ${UKBPROJROOT}/env/common
# Extract synonyms from the chembl molecule_synonyms table and "flatten" them
# into one record prior to synonym dictionary generation, which expands
# to one record per synonym in the data file output by the pipeline
#
python ${PYDIR}/chembl/dump_sqlite_table_data.py --tablename=molecule_synonyms | \
	sort -k1,1 -n | \
	python ${PYDIR}/parse_chembl_synonyms.py | \
	python ${PYDIR}/generate_syn_dictionary.py > ${CDATADIR}/syn_dict_all.txt
