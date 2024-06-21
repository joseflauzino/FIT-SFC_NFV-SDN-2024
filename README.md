

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

    cd ~/NIEP/CLI/
    sudo python2 CLI.py
    define ~/FIT-SFC/SFC-FT_Confs/DNSExample4.json
    topoup

### Step 3: Open the Mininet command line from NIEP

At this point, all the components will have been deployed.

We can access the Mininet CLI from within NIEP:

	mininet
 
Then we can see all the components deployed:

	nodes

### Step 4: Configure the routes and initialize the services in each component of the topology

#### Step 4.1: Configure the classifiers

In Mininet, we can use the syntax `<node-name> <command>`  to send commands to nodes.

Therefore, we can configure the classifiers (i.e., each SC component) as follows:

	SC01 source SFC-FT_Scripts/SC.sh SC01-eth0 173.100.100.1 192.168.123.1 &
	SC02 source SFC-FT_Scripts/SC.sh SC02-eth0 173.100.100.2 192.168.123.2 &
	SC03 source SFC-FT_Scripts/SC.sh SC03-eth0 173.100.100.3 192.168.123.3 &
	SC04 source SFC-FT_Scripts/SC.sh SC04-eth0 173.100.100.4 192.168.123.4 &
	
> [!TIP] 
> 1. This will make the commands run in background on each node.
> 2. If you want to see the output of each command, open the terminal of each node and run the command:
    xterm SC0#
    source SFC-FT_Scripts/SC.sh SC0#-eth0 173.100.100.# 192.168.123.#

#### Step 4.2: Configure the forwarders

Similarly to the classifiers, configure the forwarders:

	SFF01 source SFC-FT_Scripts/SFF.sh SFF01-eth0 192.168.123.5 &
	SFF02 source SFC-FT_Scripts/SFF.sh SFF02-eth0 192.168.123.6 &
	SFF03 source SFC-FT_Scripts/SFF.sh SFF03-eth0 192.168.123.7 &
	SFF04 source SFC-FT_Scripts/SFF.sh SFF04-eth0 192.168.123.8 &

#### Step 4.3: Configure the network functions

Now, we need to configure each NF (which are DNS servers in this case).

	DNS01 source SFC-FT_Scripts/DNS_NF.sh DNS01-eth0 192.168.123.9 &
	DNS02 source SFC-FT_Scripts/DNS_NF.sh DNS02-eth0 192.168.123.10 &
	DNS03 source SFC-FT_Scripts/DNS_NF.sh DNS03-eth0 192.168.123.11 &
	DNS04 source SFC-FT_Scripts/DNS_NF.sh DNS04-eth0 192.168.123.12 &

#### Step 4.4: Finalize the configuration of SCs and SFFs

Open the terminal of any SC node (e.g., `xterm SC01`). Now, execute the following commands:

    python3 3-Manager.py 192.168.123.1 /home/research/Desktop/NIEP/SBRC-2022/SFC-FT_Confs/DNSExampleSFP4.yaml 1
    test

### Step 5: Initialize the client

    xterm CLIENT01
    source SFC-FT_Scripts/Client.sh CLIENT01-eth0 1 192.168.122.1 173.100.100.1 173.100.100.2 173.100.100.3 173.100.100.4

### Phase 3: Perform the experiment

### Step 1: Perform the experiment

	measure 100
