---
title: Anaconda installation
tags: [conda]
keywords: conda
sidebar: mydoc_sidebar
permalink: /mydoc_cmor3_conda/
---
# Anaconda Installation

## All Platforms System Requirements

  * [Anaconda](https://www.continuum.io/)
  * Make sure anaconda is in your PATH (assuming ananconda is installed in ${HOME}/anaconda)

    ```sh
    export PATH=${HOME}/anaconda/bin:${PATH} # for [ba]sh
    setenv PATH ${HOME}/anaconda/bin:${PATH} # for [t]csh
    ``` 

## Bypassing firewalls

  * If your institution has a firewall

    ```
    conda config --set ssl_verify False
    binstar config --set verify_ssl False # it's not a typo ssl and verify are reversed
    ```

## Installing

  * Run the following command
   
    ```
    conda install cmor -c pcmdi
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


