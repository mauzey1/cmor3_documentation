---
title: Github Installation
tags: [github]
keywords: github
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_github/
---
### Environment setup


```bash
# To get trough the firewall!!
export GIT_SSL_NO_VERIFY=true 
# Where do you want you installation?
export PREFIX=$HOME/build
mkdir build
cd build
```

### Compile Dependencies

#### Retrieve sources

* [http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.17.tar](http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.17.tar) or latest
* [ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.0.tar.gz](ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.0.tar.gz) or latest
* [ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.20.tar.gz](ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-2.2.20.tar.gz) or latest
* [http://www.mirrorservice.org/sites/ftp.ossp.org/pkg/lib/uuid/uuid-1.6.2.tar.gz](http://www.mirrorservice.org/sites/ftp.ossp.org/pkg/lib/uuid/uuid-1.6.2.tar.gz) or latest

```bash
tar xf hdf5-1.8.17.tar
tar xzf netcdf-4.4.0.tar.gz
tar xzf udunits-2.2.20.tar.gz
tar xzf uuid-1.6.2.tar.gz
```

#### build libuuid

```bash
cd uuid-1.6.2
./configure --prefix=$PREFIX
make 
make install
```

#### build udnits2

```bash
cd ../udunits-2.2.20
./configure --prefix=$PREFIX
make
make install
```

#### build hdf5

```bash
cd ../hdf5-1.8.17
./configure --prefix=$PREFIX
make  
make install
```

#### build netcdf4

```bash
export CFLAGS="-I${PREFIX}/include"
export LDFLAGS="-L${PREFIX}/lib"

cd ../netcdf-4.4.0
./configure --prefix=$PREFIX --enable-netcdf4
make 
make install
```

### Build cmor 

```bash
cd ..
git clone https://github.com/PCMDI/cmor.git
cd cmor
git checkout master

./configure --prefix=$PREFIX --with-python --with-uuid --with-udunits --with-netcdf=$PREFIX/ 
make 
make install
make python
```


