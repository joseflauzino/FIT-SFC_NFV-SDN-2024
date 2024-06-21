

# Experiment 1: FIT-SFC architecture under crash failures

This experiment aims to evaluate the behavior of the FIT-SFC architecture under crash failures of different components.

> [!IMPORTANT] 
> **Before starting:** the following commands assume that the repositories have been cloned into your user's home directory (`~`). If you choose to clone to another directory, just replace `~` in the commands with the proper path.

## Phase 1: Set up

### Step 1: Clone the FIT-SFC repository
    git clone https://github.com/joseflauzino/FIT-SFC_NFV-SDN-2024.git

### Step 2: Clone the NIEP project
    git clone https://github.com/ViniGarcia/NIEP.git

### Step 3: Move the FIT-SFC folder to the NIEP folder
    mv ~/FIT-SFC_NFV-SDN-2024/ ~/NIEP/

### Step 4: Install the required packages 
	cd ~/NIEP/FIT-SFC_NFV-SDN-2024/
	pip install -r requeriments.txt
	pip3 install -r requeriments.txt
 
## Phase 2: Deployment

### Step 1: Initialize the SDN controllers
Run each command below in a different terminal window.

Controller 1:

	cd ~/NIEP/OFCONTROLLERS/pox
	sudo ./pox.py openflow.of_01 --port=10001 --address=127.0.0.1 forwarding.l2_learning
	
Controller 2:

 	cd ~/NIEP/OFCONTROLLERS/pox
	sudo ./pox.py openflow.of_01 --port=10002 --address=127.0.0.1 forwarding.l2_learning

### Step 2: Initialize NIEP, set up the desired topology, and bring it up

In another terminal window, type the following commands.

> [!NOTE] 
> Replace `<path>` with the proper path to the NIEP folder.

    cd ~/NIEP/CLI/
    sudo python2 CLI.py
    define <path>/NIEP/FIT-SFC_NFV-SDN-2024/Confs/DNSExample.json
    topoup

### Step 3: Open the Mininet command line from NIEP

At this point, all the components will have been deployed.

We can access the Mininet CLI from within NIEP:

	mininet
 
Then we can see all the components deployed:

	nodes

### Step 4: Configure the routes and initialize the services in each component of the topology

#### Step 4.1: Configure the classifiers

For each SC node, do:

	xterm SC<id>
	source ../FIT-SFC_NFV-SDN-2024/Script/SC.sh SC<id>-eth0 173.100.100.<host-number> 192.168.123.<host-number>

> [!TIP] 
> 1. Replace `<id>` with the SC identifier (i.e., SC01, SC02, etc.).
> 2. Replace `<host-number>` according to the IP Address set in the DNSExample.json file (used in Step 2).
> **Example:**  `source ../FIT-SFC_NFV-SDN-2024/Scripts/SC.sh SC01-eth0 173.100.100.1 192.168.123.1`

#### Step 4.2: Configure the forwarders

For each SFF node, do:

	xterm SFF<id>
	source ../FIT-SFC_NFV-SDN-2024/Script/SFF.sh SFF<id>-eth0 192.168.123.<host-number>

> [!TIP] 
> 1. Replace `<id>` with the SFF identifier (i.e., SFF01, SFF02, etc.).
> 2. Replace `<host-number>` according to the IP Address set in the DNSExample.json file (used in Step 2).
> **Example:**  `source ../FIT-SFC_NFV-SDN-2024/Scripts/SFF.sh SFF01-eth0 192.168.123.5`

#### Step 4.3: Configure the network functions

For each NF node (which are DNS servers in this case), do:

	xterm DNS<id>
	source ../FIT-SFC_NFV-SDN-2024/Script/DNS_NF.sh DNS<id>-eth0 192.168.123.<host-number>

> [!TIP] 
> 1. Replace `<id>` with the SFF identifier (i.e., SFF01, SFF02, etc.).
> 2. Replace `<host-number>` according to the IP Address set in the DNSExample.json file (used in Step 2).
> **Example:**  `source ../FIT-SFC_NFV-SDN-2024/Scripts/DNS_NF.sh DNS01-eth0 192.168.123.9`

#### Step 4.4: Finalize the configuration of SCs and SFFs

Open another terminal of any SC node. For example:

	xterm SC01

Now, execute the following commands:

	cd ../FIT-SFC_NFV-SDN-2024/Basics
	python3 3-Manager.py 192.168.123.1 ~/NIEP/FIT-SFC_NFV-SDN-2024/Confs/DNSExampleSFP4.yaml 1
	test

### Step 5: Initialize the client

    xterm CLIENT01
    source ../FIT-SFC_NFV-SDN-2024/Scripts/Client_DNS.sh CLIENT01-eth0 1 192.168.122.1 173.100.100.1 173.100.100.2 173.100.100.3 173.100.100.4

### Phase 3: Perform the experiment

### Step 1: Perform the experiment

	measure 100
