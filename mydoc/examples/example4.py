import cmor
import numpy
import os

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
cmor.dataset_json("CMOR_input_example.json")
cmor.load_table("CMIP6_Amon.json")
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
filename = cmor.close(cmorTas, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))
