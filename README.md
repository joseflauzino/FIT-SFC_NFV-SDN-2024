# FIT-SFC

### Step 1: Initialize NIEP, set up the desired topology, and bring it up
    sudo ./pox.py openflow.of_01 --port=10001 --address=127.0.0.1 forwarding.l2_learning
    sudo ./pox.py openflow.of_01 --port=10002 --address=127.0.0.1 forwarding.l2_learning

### Step 2: Initialize NIEP, set up the desired topology, and bring it up
    sudo python2 CLI.py
    define /home/research/Desktop/NIEP/SBRC-2022/SFC-FT_Confs/DNSExample4.json
    topoup
	
### Step 3: Open the mininet command line from NIEP
    mininet

### Step 4: Configure the routes and initialize the services in each element of the topology

#### Step 4.1: PARA CADA UM DOS N NÓS DE CLASSIFICADORES
    xterm SC0#
    source SFC-FT_Scripts/SC.sh SC0#-eth0 173.100.100.# 192.168.123.#

#### Step 4.2: PARA CADA UM DOS N NÓS DE ENCAMINHADORES
    xterm SFF0#
    source SFC-FT_Scripts/SFF.sh SFF0#-eth0 192.168.123.#

#### Step 4.3: PARA CADA UM DOS N NÓS DE NF (DNS)
    xterm DNS0#
    source SFC-FT_Scripts/DNS_NF.sh DNS0#-eth0 192.168.123.#

#### Step 4.4: ABRA UM NOVO TERMINAL DE QUALUER UM DOS CLASSIFICADORES E CONFIGURE OS SCs E SFFs
    xterm SC01
    python3 3-Manager.py 192.168.123.1 /home/research/Desktop/NIEP/SBRC-2022/SFC-FT_Confs/DNSExampleSFP4.yaml 1
    test

### Step 5: FINALMENTE, PODEMOS INICIAR O NOSSO CLIENTE
    xterm CLIENT01
    source SFC-FT_Scripts/Client.sh CLIENT01-eth0 1 192.168.122.1 173.100.100.1 173.100.100.2 173.100.100.3 173.100.100.4
