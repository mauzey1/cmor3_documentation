---
title: CMIP6 User Input
tags: [cmip6]
keywords: cmip6, cmor
sidebar: mydoc_sidebar
permalink: /mydoc_cmip6_user_input/
---

### Notes

1. Keys beginning with character **_** will not be written in netCDF file as attribute.  They can be use for template filename of template path.
1. Keys beginning with charachter **#** can be used as comment.

### CMIP6 CMOR User Input

[CMIP6_global_attributes_filenames_CVs.doc](https://docs.google.com/document/d/1h0r8RZr_f3-8egBMMh7aqLwy3snpD6_MrDz1q8n5XUk)

* *_control_vocabulary_file*:"Specify Control Vocabulary file name"

* *_cmip6_option*:           "used to trigger validation for CMIP6 only."

* *activity_id*:             "Specify an activity PMIP, GeoMIP"

* *output*:                  "Output Path where files are written -- must be created by the user."

* *experiment_id*:           "Correspond to id found in \"_control_vocabulary_file\""

* *source_type*:             "type of model used",

* *sub_experiment*:          "description of sub-experiment",

* *sub_experiment_id*:       "none",

* *parent_sub_experiment_id*:     

* *parent_mip_era*:              

* *mip_era*:                    

* *institution*:     
            
* *source*:         

* *calendar*:     

* *realization_index*:      

* *initialization_index*:  

* *physics_index*:       

* *forcing_index*:        

* *contact *:           

* *history*:          

* *comment*:        

* *references*:   

* *institution_id*:      

* *model_id*:          

* *forcing*:         

* *parent_variant_label*:  

* *parent_experiment_id*:

* *branch_time*:       


* *parent_activity_id*: 

* *parent_source_id*:   

* *branch_method*:        
* *branch_time_in_child*: 
* *branch_time_in_parent*:
* *branch_time_units_in_parent*:


* *further_info_url*:       "http://furtherinfo.es-doc.org/<mip_era>/<institution_id><source_id><experiment_id><sub_experiment_id><variant_label>",
* *grid*:                  
* *grid_label*:           
* *grid_resolution*:     
* *run_variant*:      
* *source_id*:       

* *output_path_template*:    "<activity_id><institution_id><source_id><experiment_id><variant_label><table><variable_id><grid_label><version>",

* *output_file_template*:    "<variable_id><table><experiment_id><source_id><variant_label><grid_label>",

* *license*:                "One of 2 licenses: ----- CMIP6 model data produced by <Your CentreName> is licensed under a Creative Commons Attribution 'NonCommercial Share Alike' 4.0 International License (http://creativecommons.org/licenses/by/4.0/). Use of the data should be acknowledged following guidelines found at <what URL???> The data is hosted via the Earth System Grid Federation. Permissions beyond the scope of this license may be available at http://pcmdi.org/cmip5/terms-of-use.   Individuals using this data should register at ??? to receive notice of selected categories of errata and updates. Further information about this data, including some limitations, can be found at ???. The data producers and data providers make no warranty, either express or implied, including but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law. "


