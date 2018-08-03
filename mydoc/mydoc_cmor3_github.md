---
title: Source installation
tags: [github]
keywords: github
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_github/
---

### Obtaining the sources

  * Clone the repo from gituhb
    ```bash
    git clone git://github.com/pcmdi/cmor
    cd cmor
    ```

### Anaconda System Requirements (if building using anaconda compilers)


#### Getting Anaconda

  * [Anaconda](https://www.continuum.io/)
  * Make sure anaconda is in your PATH (assuming ananconda is installed in ${HOME}/anaconda)

    ```bash
    export PATH=${HOME}/anaconda/bin:${PATH} # for [ba]sh
    ``` 

#### Bypassing firewalls

  * If your institution has a firewall

    ```bash
    conda config --set ssl_verify False
    ```

#### Creating the conda environement with compilers and needed libraries

  * Depending on your os conda brings different compilers

    For Linux
    ```bash
    export CONDA_COMPILERS="gcc_linux-64 gfortran_linux-64"
    ```

    For Mac
    ```bash
    export CONDA_COMPILERS="clang_osx-64 gfortran_osx-64"
    ```

  * Run the following command
   
    ```bash
    conda create -q -n cmor_dev -c cdat/label/nightly -c conda-forge -c cdat ossuuid udunits2 hdf5 libnetcdf numpy openssl cdms2 python=2.7 $CONDA_COMPILERS testsrunner
    ```
  * Activate the conda environment

    ```bash
    source activate cmor_dev
    ```

### Configuring cmor

  * Depending on your OS linking environment variables are different

    For Linux
    ```bash
    export LDSHARED_FLAGS="-shared -pthread"
    ```

    For Mac
    ```bash
    export LDSHARED_FLAGS=" -bundle -undefined dynamic_lookup"
    ```
  * Set the PREFIX

  Since your environment can use a different name and its location is system dependent use:

  ```bash
  export PREFIX=$(python -c "import sys; print sys.prefix")
  ```

  * configure cmor:

  ```bash
  ./configure --prefix=$PREFIX --with-python --with-uuid=$PREFIX --with-udunits2=$PREFIX --with-netcdf=$PREFIX  --enable-verbose-test
  ```

### Building CMOR

  * Run

  ```bash
  make install
  ```

### Testing the installation

   * Two sets of test can be used
   
   ```bash
   make test
   ```

   ```bash
   python run_tests.py -v2 -H
   ```