# UK Biobank Self Reported Medication Data parsing and matching
## Overview
Code to match UK biobank (UKBB) Self-Reported Medication (SRMed) descriptions with descriptions from a classification system. Data from the Anatomical Therapeutic Chemical (ATC) classification system defined by the WHO and code data from the British National Formulary (BNF) have been tested against during development.

The objective is to provide the means to classify UKBB Self-Reported medication data into related therapy groups for the purpose of enabling additional evidence from UKBB phenotype data to be collected when deriving both individual clinical phenotypes (for example, Asthma, Neuropathic Pain, T2 Diabetes) and when generating a range of phenotypes for Phenome Wide Association Studies (PhewAS). 

## Description
Matching code is written in Python 2 (2.7 was used for development). Extensive use of Bash shell wrappers is made to supply context:- Data directory locations, data file names and database access parameters. All code is intended to be run from a Linix / Unix command line.

### Subdirectories:

> *env/* Environment variables used are shown in a single file 'common_tplt', users should complete these and copy to a file named 'common', users must also pre-define **PROJDATA** and **PROJROOT**. Parameters for local chembl database access are also required for drug synonym extraction. The example supplied is for the sqlite version 23 of the chembl database which can be found at: 

> ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_23/chembl_23_sqlite.tar.gz this is no longer the latest version at the time of writing.

> *py/* Python scripts, including the module 'datahelper.py' which is where the text matching code is to be found.

> *sh* Bash shell scripts, wrappers for the python code split into several main functions and provided for coding against the ATC and BNF classification systems.

> Top-level scripts are prefixed '01_', '02_' and '03_' for each classification system and call several lower level bash scripts. The '03_' scripts are for code assignment to data for individual medication reports in UKBB, the path and filename for UKBB phenotype data for a project must be supplied vis the sourced 'common' environment parameter file.

> *data/* Generated match data for both ATC and BNF coding, this does not include manually assigned coding.
