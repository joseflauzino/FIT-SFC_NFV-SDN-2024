# Set up

## Prerequisites

- Ubuntu 16.04
- Python 3.7 +

## Preparation

> [!IMPORTANT] 
> **Before starting:** the following commands assume that you will clone the repositories into your user's home directory (`~`). If you choose to clone to another directory, just replace `~` in the commands with the proper path.

### Step 1: Clone the NIEP project
    git clone https://github.com/ViniGarcia/NIEP.git

### Step 2: Install NIEP
    cd ~/NIEP/INSTALLATION/
    sudo ./installer.sh

### Step 3: Clone the FIT-SFC repository
    git clone https://github.com/joseflauzino/FIT-SFC_NFV-SDN-2024.git

### Step 4: Move the FIT-SFC folder to the NIEP folder
    mv ~/FIT-SFC_NFV-SDN-2024/ ~/NIEP/

### Step 5: Install the required packages 
	cd ~/NIEP/FIT-SFC_NFV-SDN-2024/
	pip install -r requeriments.txt
	pip3 install -r requeriments.txt