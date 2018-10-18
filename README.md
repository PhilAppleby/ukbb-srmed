# UK Biobank Self Reported Medication Data parsing and matching
## Background
UK Biobank self reported medications are represented in UK Biobank as a list of codes per participant captured at the time of the Baseline Assessment Interview. 

For example participant id '000001' may have reported medications with UKBB codes 1140922174, 1140879424, 1140879616, 1197 and 2038460150.

These are described in the UKBB medication codes table as:

| Code     | Description                | Report Count |
| -------- | -------------------------- | -----------: |
|1140922174|alendronate sodium          |6380          |
|1140879424|alverine                    |308           |
|1140879616|amitriptyline               |10119         |
|1197      |evening primrose oil product|1132          |
|2038460150|paracetamol                 |100036        |

There is no structure in the data and no means of grouping medication into categories such as "Drugs for Diabetes" or "Drugs to control Asthma", for example.

## Aims
Write and test software to match terms in the UK Biobank Self Reported Medication data coding table with terms in both the Anatomical Therapeutic Chemical (ATC) classification system and in the British National Formulary (BNF) coding system. The overall aim being to assign higher level coded to allow grouping of the data. The resulting matched data can then be used in conjuction with the UKBB codes assigned at assessment time to generate evidence for use in both individual clinical phenotypes and in ranges of clincal phenotypes for use in PheWAS.

## Description
Matching code is written in Python 2 (2.7 was used for development). Extensive use of Bash shell wrappers is made to supply context:- Data directory locations, data file names and database access parameters. All code is intended to be run from a Linix / Unix command line. The following subdirectories can be found in the repository:

- *env/* Environment variables used are shown in a single file 'common_tplt', users should complete these and copy to a file named 'common', users must also pre-define **PROJDATA** and **PROJROOT**. Parameters for local chembl database access are also required for drug synonym extraction. The example supplied is for the sqlite version 23 of the chembl database which can be found at: 

ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_sqlite.tar.gz this is no longer the latest version at the time of writing.

- *py/* Python scripts, scripts to match synonyms prior to matching across coding systems. Also included is the module 'datahelper.py' which is where the text matching code is to be found.

- *sh* Bash shell scripts, wrappers for the python code split into several main functions and provided for coding against the ATC and BNF classification systems.

Top-level scripts are prefixed '01_', '02_' and '03_' for each classification system and call several lower level bash scripts. The '03_' scripts are for code assignment to data for individual medication reports in UKBB, the path and filename for UKBB phenotype data for a project must be supplied vis the sourced 'common' environment parameter file.

- *data/* Generated match data for both ATC and BNF coding, this does not include manually assigned coding.

## Running
Once the environment has been set up (see *env* above), three scripts are run wihout parameters.

For ATC-based matching run:
- 01_atc_prepare_sqlite.sh
- 02_atc_match.sh
- 03_get_ukbb_srmed_data_atc.sh

For ATC-based matching run:
- 01_bnf_prepare_sqlite.sh
- 02_bnf_match.sh
- 03_get_ukbb_srmed_data_bnf.sh
