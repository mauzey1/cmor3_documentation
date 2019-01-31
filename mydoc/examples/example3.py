import cmor
import numpy
import os

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
cmorLev = cmor.axis("plev19", coord_vals=lev, units='Pa')
axes = [cmorTime, cmorLev, cmorLat, cmorLon]
cmorTa = cmor.variable("ta", "K", axes)
cmor.write(cmorTa, ta)
filename = cmor.close(cmorTa, file_name=True)
print("Stored in:", filename)
cmor.close()
os.system("ncdump {}".format(filename))

