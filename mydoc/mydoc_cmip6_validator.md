---
title: CMIP6 Validator
tags: [cmip6]
keywords: cmip6, table, validator
sidebar: mydoc_sidebar
permalink: /mydoc_cmip6_validator/
---

### Usage
```
CMIP6Validator [-h] cmip6_table infile [outfile]
```
where:

  * -h display sysnopsis of the program
  * __cmip6_table__ correspond to a CMIP6 JSON table.  
    * [CMIP6 Amon tables](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_Amon.json)

  * __infile__  netCDF CMIP6 file to be published by ESGF.

  * __outfile__ write output into a log file

### Validation

The validator will verify that all attributes in the input file are present and conform to CMIP6 for publication into ESGF.  We also recommand running the python program [cfchecker](https://pypi.python.org/pypi/cfchecker) created by the University of Reading in the UK to confirm that your file is CF-1 compliant.

  * In order to validate all CMIP6 required attributes by the CMIP6 Validator,  a [Control Vocabulary file](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json) is read by the program where a JSON dictionnary called  ["required_global_attributes"](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json#L3) point to a list of strings.  Each element of that list corresponds to a global attribute.  

  * The CMIP6 Validator can also use regular expressions to validate the value of the some global attributes.  Here is an [example](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json#L43) used for variant_label.

  * Institutions and institution_ids need to be registered into a list.   The CMIP6 validator will only accept institutions which have been pre-registered for CMIP6 publication into ESGF.   Click [here](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json#L123) for the list of institutions.  If you wish to register your institution write to the [cmor mailing list](mailto:cmor@listserv.llnl.gov).

  * Source and Source ID also need to be registered for CMIP6 publication.  Here is the [list](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json#L88) of registered sources.

  * Only experiments found in the Control Vocabulary files are accepted for CMIP6 publication. A list of [experiment_ids](https://github.com/PCMDI/cmip6-cmor-tables/blob/master/Tables/CMIP6_CV.json#L177) have been pre-defined including mandatory attributes.  A warning will be displayed if one experiment attribute is missing or is not properly set by your program.

  * grid and grid_resolution are mandatory global attributes in CMIP6.  The validator will make sure that these attributes are conformed to one of the following syntax:

     |  grid              |  grid_resolution |
     |--------------------|------------------|
     | gs1x1              |  1x1 degree  |
     | gs1x1 or gn0 to gn9|  1x1 degree  |
     | gs1x1 or gr0 to gr9|  1x1 degree  |
     |  gn0 to gn9        |  "5 km" or   "10 km" or   "25 km" or   "50 km" or  "100 km" or "250 km" or "500 km" or "1000 km" or "2500 km" or "5000 km" or "10000 km" |
     |  gr0 to gr9        |  "5 km" or   "10 km" or   "25 km" or   "50 km" or   "100 km" or "250 km" or "500 km" or "1000 km" or "2500 km" or "5000 km" or "10000 km" |

  
  * The CMIP6 Validator verifies that the creation date found in the netCDF file is conform to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard.

  * The Further Info URL attribute has to be set according to a very specific template.  The CMIP6 Validator will use global attribute names found in the netCDF input file and replace the corresponding tag found in a template to rebuild proper CMIP6 link.  If the reconstructed URL does not correspond to the value found in the input file, the validator will display an critical error on the screen.
    * Below is the defaul template used for the __furtherinfourl__ attribute.  Each string found between the "<>" characters correspond to a global attribute.  The program will replace these strings with the corresponding global attribute values and add the __"."__ character between each tag.

```
http://furtherinfo.es-doc.org/<mip_era><institution_id><source_id><experiment_id><sub_experiment_id><variant_label>

becomes

http://furtherinfo.es-doc.org/CMIP6.CSIRO-BOM.NICAM.piControl.none.r1i1p1f1" 
```

  * The CMIP6 Validator will also verify variable attributes necessary for CMIP6 publication.   It validates: long_name, standard_name, units and missing value according the CMIP6 tables information. 




