# Overview
# Intro
This repository provides guides and scripts to fetch ipfs links, get cid and repin it to other places rather than pinata using Python. To do this, you will first need to obtain a ipfs_data csv file using script in fetch_arc69, and then repin cids through scripts in pin.

# Pre-Requirements
1) Install Python
If you do not already have Python installed, install python using Anaconda: https://www.anaconda.com/products/individual. Installing just Miniconda is fine as we will not need the other packages. Alternatively if you're going to use Visual Studio Code (see next step), downloading and installing python from https://www.python.org/downloads/ is also possible.

# 2) Install Python IDE
We will use a Python IDE to update and run the scripts. Although if you develop in multiple languages https://code.visualstudio.com/ is a great alternative. Spyder can be installed by opening the anaconda terminal and running the following:

conda install spyder

# 3) Install Python dependencies
This pipeline requires some dependencies which have to be installed prior to running.

They can be installed using PIP, by opening your terminal and running the following:

pip3 install -r requirements.txt

You will also need to install other dependencies depending on what kind of method you prefer to use to pin your NFT cid. If there is any missing dependencies, always google them and install accordingly.

# General Settings
In order to adjust the scripts to your needs, it's necessary to config the settings.yaml.

The output folder for all scripts will be per default included in this folder. If you wish for your output to be generated somewhere else you can adjust that settings accordingly:

default_output_folder: "c:/somewhere/here"

There are also some other files paths that requires you to config manually, such as your data files.
