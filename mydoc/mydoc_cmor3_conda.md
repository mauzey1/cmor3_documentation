---
title: Anaconda installation
tags: [conda]
keywords: conda
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---

### All Platforms System Requirements

  * **CMOR 3.4.0 on conda-forge is only supported for Python 2.7.  For Python 3.6 and 3.7 support, use the latest [nightly build](#obtaining-nighlty-builds).  Future releases on conda-forge will support Python 3.**

  * [Anaconda](https://www.continuum.io/)

  * Make sure anaconda is in your PATH (assuming ananconda is installed in ${HOME}/anaconda)

    ```sh
    export PATH=${HOME}/anaconda/bin:${PATH} # for [ba]sh
    setenv PATH ${HOME}/anaconda/bin:${PATH} # for [t]csh
    ``` 

### Bypassing firewalls

  * If your institution has a firewall

    ```
    conda config --set ssl_verify False
    ```

### Installing

  * Run the following command
   
    ```bash
    # install cmor, it will also install cdms2.
    # ------------------------------------------------
    conda create -n CMOR -c conda-forge cmor
    source activate CMOR

    # Clone the CMIP6 table to your working directory.
    # ------------------------------------------------
    mkdir CMIP6_work
    cd  CMIP6_work

    # Disable SSL verification (firewall only).
    # -----------------------------------------
    export GIT_SSL_NO_VERIFY=true
    git clone https://github.com/PCMDI/cmip6-cmor-tables.git

    # Note:
    # -----------------------------------------------------------
    # UDUNITS2_XML_PATH is set automatically by activating CMOR. 
    # export UDUNITS2_XML_PATH=${CONDA_PREFIX}/share/udunits/udunits2.xml
    #
    ```

## Conda environment

  * Create your different CMOR environment with anaconda.

    ```
    conda create -n [YOUR_ENV_NAME_HERE] -c conda-forge cmor
    source activate [YOUR_ENV_NAME_HERE]
    ```

  * [To learn more about conda environments](http://conda.pydata.org/docs/using/envs.html)

## Obtaining Nighlty builds

  * Create a dedicated environment for nightly (in between releases code):
    ```
    conda create -n [YOUR_ENV_NAME_HERE] -c pcmdi/label/nightly -c conda-forge cmor
    source activate [YOUR_ENV_NAME_HERE]
    ```
