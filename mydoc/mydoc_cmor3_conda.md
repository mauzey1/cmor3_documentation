---
title: Anaconda installation
tags: [conda]
keywords: conda
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---

### All Platforms System Requirements

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
    binstar config --set verify_ssl False # it's not a typo ssl and verify are reversed
    ```

### Installing

  * Run the following command
   
    ```bash

    # install cmor, it will also install cdms2.
    # ------------------------------------------------
    conda install cmor -c pcmdi

    # Clone the CMIP6 table to your working directory.
    # ------------------------------------------------
    mkdir CMIP6_work
    cd  CMIP6_work

    # Disable SSL verifycation (firewall only).
    # -----------------------------------------
    export GIT_SSL_NO_VERIFY=true
    git clone https://github.com/PCMDI/cmip6-cmor-tables.git

    # Create a softlink of your tables in your working directory.
    # -----------------------------------------------------------
    ln -s cmip6-cmor-tables/Tables .

    # Set the UDUNITS2_XML_PATH to your anaconda installation.
    # -----------------------------------------------------------
    export UDUNITS2_XML_PATH=${HOME}/anaconda/share/udunits/udunits2.xml
    ```

## Conda environment

  * Create your CMOR environment with anaconda.

    ```
    conda create -n [YOUR_ENV_NAME_HERE] -c pcmdi cmor
    source activate [YOUR_ENV_NAME_HERE]
    conda env list 
    conda create -n [YOUR_ENV_NAME_HERE] --clone ENV 
    ```

  * [To learn more about conda environments](http://conda.pydata.org/docs/using/envs.html)




