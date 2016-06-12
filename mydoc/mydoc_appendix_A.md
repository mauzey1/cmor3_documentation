---
title: Appendix A 
keywords: documentation
last_updated: June 12, 2016
tags: [appendix]
sidebar: mydoc_sidebar
permalink: /mydoc_appendix_A/
---

### Critical Errors

The following errors are considered as CRITICAL and will cause a CMOR code to stop.


  1. Calling a CMOR function before running cmor_setup
  1. NetCDF version is neither 3.6.3 or 4.1 or greater
  1. Udunits could not parse units
  1. Incompatible units
  1. Udunits could not create a converter
  1. Logfile could not be open for writing
  1. Output directory does not exist
  1. Output directory is not a directory
  1. User does not have read/write privileges on the output directory
  1. Wrong value for error_mode
  1. wrong value for netCDF mode
  1. error reading udunits system
  1. NetCDF could not set variable attribute
  1. Dataset does not have one of the required attributes (required attributes can be defined in the MIP table)
  1. Required global attribute is missing
  1. If CMIP5 project: source attributes does not start with model_id attribute.
  1. Forcing dataset attribute is not valid
  1. Leap_year defined with invalid leap_month
  1. Invalid leap month (<1 or >12)
  1. Leap month defined but no leap year
  1. Negative realization number
  1. Zfactor variable not defined when needed
  1. Zfactor defined w/o values and NOT time dependent.
  1. Variable has axis defined with formula terms depending on axis that are not part of the variable
  1. NetCDF error when creating zfactor variable
  1. NetCDF Error defining compression parameters
  1. Calling cmor_write with an invalid variable id
  1. Could not create path structure
  1. “variable id” contains a “_” or a ‘-‘ this means bad MIP table.
  1. “file_suffix” contains a “_”
  1. Could not rename the file you’re trying to append to.
  1. Trying to write an “Associated variable” before the variable itself
  1. Output file exists and you’re not in append/replace mode
  1. NetCDF Error opening file for appending
  1. NetCDF could not find time dimension in a file onto which you want to append
  1. NetCDF could not figure out the length time dimension in a file onto which you want to append
  1. NetCDF could not find your variable while appending to a file
  1. NetCDF could not find time dimension in the variable onto which you’re trying to append
  1. NetCDF could not find time bounds in the variable onto which you’re trying to append
  1. NetCDF mode got corrupted.
  1. NetCDF error creating file
  1. NetCDF error putting file in definition mode
  1. NetCDF error writing file global attribute
  1. NetCDF error creating dimension in file
  1. NetCDF error creating variable
  1. NetCDF error writing variable attribute
  1. NetCDF error setting chunking parameters
  1. NetCDF error leaving definition mode
  1. Hybrid coordinate, could not find “a” coefficient
  1. Hybrid coordinate, could not find “b” coefficient
  1. Hybrid coordinate, could not find “a_bnds” coefficient
  1. Hybrid coordinate, could not find “b_bnds” coefficient
  1. Hybrid coordinate, could not find “p0” coefficient
  1. Hybrid coordinate, could not find “ap” coefficient
  1. Hybrid coordinate, could not find “ap_bnds” coefficient
  1. Hybrid coordinate, could not find “sigma” coefficient
  1. Hybrid coordinate, could not find “sigma_bnds” coefficient
  1. NetCDF writing error
  1. NetCDF error closing file
  1. Could not rename temporary file to its final name.
  1. Cdms could not convert time values for calendar.
  1. Variable does not have all required attributes (cmor_variable)
  1. Reference variable is defined with “positive”, user did not pass it to cmor_variable
  1. Could not allocate memory for zfactor elements
  1. Udunits error freeing units
  1. Udunits error freeing converter
  1. Could not allocate memory for zfactor_bounds
  1. Calling cmor_variable before reading in a MIP table
  1. Too many variable defined (see appendix on CMOR limits)
  1. Could not find variable in MIP table
  1. Wrong parameter “positive” passed
  1. No “positive” parameter passed to cmor_variable and it is required for this variable
  1. Variable defined with too many (not enough) dimensions
  1. Variable defined with axis that should not be on this variable
  1. Variable defined within existing axis (wrong axis_id)
  1. Defining variable with axes defined in a MIP table that is not the current one.
  1. Defining a variable with too many axes (see annex on CMOR limits)
  1. Defining variable with axes ids that are not valid.
  1. Defining variable with grid id that is not valid.
  1. Defining a variable with dimensions that are not part of the MIP table (except for var named “latitude” and “longitude”, since they could have grid axes defined in another MIP table)
  1. Trying to retrieve length of time for a variable defined w/o time length
  1. Trying to retrieve variable shape into an array of wrong rank (Fortran only really)
  1. Calling cmor_write with time values for a timeless variable
  1. Cannot allocate memory for temporary array to write
  1. Invalid absolute mean for data written (lower or greater by one order of magintudethan what the MIP table allows)
  1. Calling cmor_write with time values when they have already been defined with cmor_axis when creating time axis
  1. Cannot allocate memory to store time values
  1. Cannot allocate memory to store time bounds values
  1. Time values are not monotonic
  1. Calling cmor_write w/o time values when no values were defined via cmor_axis when creating time axis
  1. Time values already written in file
  1. Time axis units do not contain “since” word (cmor_axis)
  1. Invalid data type for time values (ok are ‘f’,’l’,’i’,’d’)
  1. Time values are not within time bounds
  1. Non monotonic time bounds
  1. Longitude axis spread over 360 degrees.
  1. Overlapping bound values (except for climatological data)
  1. bounds and axis values are not stored in the same order
  1. requested value for axis not present
  1. approximate time axis interval much greater (>20%) than the one defined in your MIP table
  1. calling cmor_axis before loading a MIP table
  1. too many axes defined (see appendix on CMOR limits)
  1. could not find reference axis name in current MIP table
  1. output axis needs to be standard_hybrid_sigma and input axis is not one of : “standard_hybrid_sigma”, “alternate_hybrid_sigma”, “standard_sigma”
  1. MIP table requires to convert axis to unknown type
  1. requested “region” not present on axis
  1. axis (with bounds) values are in invalid type (valid are: ‘f’,’d’,’l’,’i’)
  1. requested values already checked but stored internally, could be bad user cleanup
  1. MIP table defined for version of CMOR greater than the library you’re using
  1. too many experiments defined in MIP table (see appendix on CMOR limits)
  1. cmor_set_table used with invalid table_id
  1. MIP table has too many axes defined in it (see appendix on CMOR limits)
  1. MIP table has too many variables defined in it (see appendix on CMOR limits)
  1. MIP table has too many mappings defined in it (see appendix on CMOR limits)
  1. MIP table defines the same mapping twice
  1. grid mapping has too many parameters (see appendix on CMOR limits)
  1. grid has different number of axes than what grid_mapping prescribes.
  1. Could not find all the axes required by grid_mapping
  1. Call to cmor_grid with axis that are not created yet via cmor_axis
  1. Too many grids defined (see appendix on cmor_limits)
  1. Call to cmor_grid w/o latitude array
  1. Call to cmor_grid w/o longitude array




