# Bitwarden Directory Connector deployment options

Welcome to this repo detailing useful configurations and methods for deploying Bitwarden Directory Connector on Linux.  This repo is referred to in the accompanying YouTube video located [here](https://www.youtube.com/watch?v=u9IUvH7j7bo).

The repo contains a few main components:

- an example ansible role that will 
  - deploy `bwdc` alongside the `bws` and `bw` binaries
  - use these to download a `data.json` file from a Bitwarden org
  - deploy a python script that will obtain the master password used to authorise the `bw` cli tool via a call to Bitwarden Secrets manager

- the aforementioned python script
  - that gives an exploratory introduction to obtaining secrets via Bitwarden Secrets Manager for use in your python scripting

- manual configuration steps
  - in order to manually run the shell commands necessary to allow `bwdc` to use the supplied `data.json` file via either encrypted or plaintext secrets

