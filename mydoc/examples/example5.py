import cmor
import numpy
import os

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
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Omon.json")
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
filename = cmor.close(cmorVar, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))

