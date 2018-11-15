---
title: Example Python
tags: [example]
keywords: example, python
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_python/
---
### CMOR user Input


[common_user_input.json](https://github.com/PCMDI/cmor/blob/master/Test/common_user_input.json)

```json
{
           "_control_vocabulary_file": "CMIP6_CV.json",
           "_AXIS_ENTRY_FILE":         "CMIP6_coordinate.json",
           "_FORMULA_VAR_FILE":        "CMIP6_formula_terms.json",
           "_cmip6_option":           "CMIP6",

           "tracking_prefix":        "hdl:21.14100",
           "activity_id":            "ISMIP6",


           "#output":                "Output Path where files are written",
           "outpath":                "CMIP6",

           "#experiment_id":         "CMIP6 valid experiment_ids are found in CMIP6_CV.json",
           "experiment_id":          "piControl-withism",
           "sub_experiment_id":      "none",
           "sub_experiment":         "none",

           "source_type":            "AOGCM ISM AER",
           "parent_mip_era":         "N/A",
           "mip_era":                "CMIP6",
           "calendar":               "360_day",

           "realization_index":      "11",
           "initialization_index":   "1",
           "physics_index":          "1",
           "forcing_index":          "1",

           "#contact ":              "Not required",
           "contact ":              "Python Coder (coder@a.b.c.com)",

           "#history":               "not required, supplemented by CMOR",
           "history":                "Output from archivcl_A1.nce/giccm_03_std_2xCO2_2256.",

           "#comment":               "Not required",
           "comment":                "",

           "#references":            "Not required",
           "references":             "Model described by Koder and Tolkien (J. Geophys. Res., 2001, 576-591).  Also see http://www.GICC.su/giccm/doc/index.html  2XCO2 simulation described in Dorkey et al. '(Clim. Dyn., 2003, 323-357.)'",

           "grid":                   "gs1x1",
           "grid_label":             "gr",
           "nominal_resolution":     "5 km",

           "institution_id":         "PCMDI",

           "parent_experiment_id":   "histALL",
           "parent_activity_id":     "ISMIP6",
           "parent_mip_era":         "CMIP6",

           "parent_source_id":       "PCMDI-test-1-0",
           "parent_time_units":      "days since 1970-01-01",
           "parent_variant_label":   "r123i1p33f5",

           "branch_method":          "Spin-up documentation",
           "branch_time_in_child":   2310.0,
           "branch_time_in_parent":  12345.0,


           "#run_variant":           "Description of run variant (Recommended).",
           "run_variant":            "forcing: black carbon aerosol only",

           "#source_id":              "Model Source",
           "source_id":               "PCMDI-test-1-0",

           "#source":                "source title, first part is source_id",
           "source":                 "PCMDI-test 1.0",


           "#output_path_template":   "Template for output path directory using tables keys or global attributes",
           "output_path_template":    "<mip_era><activity_id><institution_id><source_id><experiment_id><_member_id><table><variable_id><grid_label><version>",
           "output_file_template":    "<variable_id><table><source_id><experiment_id><_member_id><grid_label>",

           "license":                 "CMIP6 model data produced by Lawrence Livermore PCMDI is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and at https:///pcmdi.llnl.gov/. The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law."

}



```


### Example 1: Python source code

[test_doc.py](https://github.com/PCMDI/cmor/blob/master/Test/test_doc.py)
[CMIP6_Amon.json](https://github.com/PCMDI/cmor/blob/master/TestTables/CMIP6_Amon.json)

```python
import cmor

cmor.setup(inpath='Tables',netcdf_file_action=cmor.CMOR_REPLACE_4)

cmor.dataset_json("Test/common_user_input.json")
    
table='CMIP6_Amon.json'
cmor.load_table(table)

itime = cmor.axis(table_entry= 'time',
                  units= 'days since 2000-01-01 00:00:00',
                  coord_vals= [15,],
                  cell_bounds= [0, 30])
ilat = cmor.axis(table_entry= 'latitude',
                 units= 'degrees_north',
                 coord_vals= [0],
                 cell_bounds= [-1, 1])
ilon = cmor.axis(table_entry= 'longitude',
                 units= 'degrees_east',
                 coord_vals= [90],
                 cell_bounds= [89, 91])

axis_ids = [itime,ilat,ilon]
              
varid = cmor.variable('ts', 'K', axis_ids)
cmor.write(varid, [273])
outfile=cmor.close(varid, file_name=True)
print "File written: ",outfile
cmor.close()


```

### Example 2: Usual Treatment of a 2-D Field

```python
import cmor
import numpy


hfls = numpy.array([120, 116, 112, 108,
                    104, 100, 96, 92,
                    88, 84, 80, 76,
                    119, 115, 111, 107,
                    103, 99, 95, 91,
                    87, 83, 79, 75
                    ])
hfls.shape = (2, 3, 4)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])

lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])

time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])

ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/common_user_input.json")

cmor.load_table("Tables/CMIP6_Amon.json")

cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
axes = [cmorTime, cmorLat, cmorLon]

cmorHfls = cmor.variable("hfls", "W/m2", axes, positive="up")
cmor.write(cmorHfls, hfls)

cmor.close()

```

### Example 3: Usual Treatment of a 3-D Field on Pressure Levels

```python
import cmor
import numpy


ta = 10. * numpy.random.random_sample((2, 19, 3, 4)) + 250.
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])

lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])

time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])

lev = numpy.array([100000, 92500, 85000, 70000, 60000, 50000, 40000, 30000,
                   25000, 20000, 15000, 10000, 7000, 5000, 3000, 2000, 1000, 500, 100])

ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/common_user_input.json")

cmor.load_table("Tables/CMIP6_Amon.json")

cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")

cmorLev = cmor.axis("plev19", coord_vals=lev, units='Pa')
axes = [cmorTime, cmorLev, cmorLat, cmorLon]

cmorTa = cmor.variable("ta", "K", axes)
cmor.write(cmorTa, ta)

cmor.close()

```

### Example 4: Treatment of a Scalar Dimension (near-surface air temperature)

```python
import cmor
import numpy


tas = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])

lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])

time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])

ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/common_user_input.json")

cmor.load_table("Tables/CMIP6_Amon.json")

cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")

axes = [cmorTime, cmorLat, cmorLon]

cmorTas = cmor.variable("tas", "K", axes)
cmor.write(cmorTas, tas)

cmor.close()
```

### Example 5: Treatment of Auxiliary Coordinates (northward ocean heat transport; a function of latitude, ocean basin, month)

```python
import cmor
import numpy


data = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
data = numpy.array([-80, -84, -88,
                    -100, -104, -76,
                    -120, -92, -96,
                    -79, -83, -87,
                    -99, -103, -75,
                    -107, -111, -115
                    ])
data.shape = (2, 3, 3)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])

time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])

region = [
    "atlantic_arctic_ocean",
    "indian_pacific_ocean",
    "global_ocean"
]
ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/common_user_input.json")

cmor.load_table("Tables/CMIP6_Omon.json")

cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")
cmorBasin = cmor.axis("basin", coord_vals=region, units="")
axes = [cmorTime, cmorBasin, cmorLat]

cmorVar = cmor.variable("htovgyre", "W", axes)
cmor.write(cmorVar, data)

cmor.close()

```

### Example 6: Treatment of a 3-D Field on Model Levels (cloud fraction; a function of longitude, latitude, model level, month)


```python
import cmor
import numpy


data = 10. * numpy.random.random_sample((2, 3, 4)) + 250.
data = numpy.array([
    72.8, 73.2, 73.6, 74,
    71.6, 72, 72.4, 72.4,
    70.4, 70.8, 70.8, 71.2,
    67.6, 69.2, 69.6, 70,
    66, 66.4, 66.8, 67.2,
    64.8, 65.2, 65.6, 66,
    63.6, 64, 64.4, 64.4,
    60.8, 61.2, 62.8, 63.2,
    59.6, 59.6, 60, 60.4,
    58, 58.4, 58.8, 59.2,
    56.8, 57.2, 57.6, 58,
    54, 54.4, 54.8, 56.4,
    52.8, 53.2, 53.2, 53.6,
    51.6, 51.6, 52, 52.4,
    50, 50.4, 50.8, 51.2,
    72.9, 73.3, 73.7, 74.1,
    71.7, 72.1, 72.5, 72.5,
    70.5, 70.9, 70.9, 71.3,
    67.7, 69.3, 69.7, 70.1,
    66.1, 66.5, 66.9, 67.3,
    64.9, 65.3, 65.7, 66.1,
    63.7, 64.1, 64.5, 64.5,
    60.9, 61.3, 62.9, 63.3,
    59.7, 59.7, 60.1, 60.5,
    58.1, 58.5, 58.9, 59.3,
    56.9, 57.3, 57.7, 58.1,
    54.1, 54.5, 54.9, 56.5,
    52.9, 53.3, 53.3, 53.7,
    51.7, 51.7, 52.1, 52.5,
    50.1, 50.5, 50.9, 51.3])
data.shape = (2, 5, 3, 4)
lat = numpy.array([10, 20, 30])
lat_bnds = numpy.array([5, 15, 25, 35])

lon = numpy.array([0, 90, 180, 270])
lon_bnds = numpy.array([-45, 45,
                        135,
                        225,
                        315
                        ])

time = numpy.array([15.5, 45])
time_bnds = numpy.array([0, 31, 60])

lev = [0.92, 0.72, 0.5, 0.3, 0.1]
lev_bnds = [1, 0.83,
            0.61,
            0.4,
            0.2,
            0
            ]

p0 = 100000

a = [0.12, 0.22, 0.3, 0.2, 0.1]

b = [0.8, 0.5, 0.2, 0.1, 0]

ps = numpy.array([
    97000, 97400, 97800, 98200,
    98600, 99000, 99400, 99800,
    100200, 100600, 101000, 101400,
    97100, 97500, 97900, 98300,
    98700, 99100, 99500, 99900,
    100300, 100700, 101100, 101500])
ps.shape = (2, 3, 4)

a_bnds = [
    0.06, 0.18,
    0.26,
    0.25,
    0.15,
    0]

b_bnds = [
    0.94, 0.65,
    0.35,
    0.15,
    0.05,
    0]

ipth = opth = 'Test'
cmor.setup(inpath=ipth,
           set_verbosity=cmor.CMOR_NORMAL,
           netcdf_file_action=cmor.CMOR_REPLACE)

cmor.dataset_json("Test/common_user_input.json")

cmor.load_table("Tables/CMIP6_Amon.json")

cmorLat = cmor.axis("latitude",
                    coord_vals=lat,
                    cell_bounds=lat_bnds,
                    units="degrees_north")
cmorLon = cmor.axis("longitude",
                    coord_vals=lon,
                    cell_bounds=lon_bnds,
                    units="degrees_east")
cmorTime = cmor.axis("time",
                     coord_vals=time,
                     cell_bounds=time_bnds,
                     units="days since 2018")

cmorLev = cmor.axis("standard_hybrid_sigma",
                    units='1',
                    coord_vals=lev,
                    cell_bounds=lev_bnds)
axes = [cmorTime, cmorLev, cmorLat, cmorLon]

ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='a',
                    axis_ids=[cmorLev, ],
                    zfactor_values=a,
                    zfactor_bounds=a_bnds)

ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='b',
                    axis_ids=[cmorLev, ],
                    zfactor_values=b,
                    zfactor_bounds=b_bnds)
ierr = cmor.zfactor(zaxis_id=cmorLev,
                    zfactor_name='p0',
                    units='Pa',
                    zfactor_values=p0)

ips = cmor.zfactor(zaxis_id=cmorLev,
                   zfactor_name='ps',
                   axis_ids=[cmorTime, cmorLat, cmorLon],
                   units='Pa')


cmorVar = cmor.variable("cl", "%", axes)
cmor.write(cmorVar, data)
cmor.write(ips, ps, store_with=cmorVar)
cmor.close()

```
