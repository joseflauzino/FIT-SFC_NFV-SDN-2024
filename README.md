[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

# Dependable Virtual Network Services: An Architecture for Fault- and Intrusion-tolerant SFCs

### Authors:
- Giovanni Venâncio (UFPR, Brazil) - giovanni@inf.ufpr.br
- Vinicius Fulber-Garcia (UFPR, Brazil) - vinicius@inf.ufpr.br
- José Flauzino (UFPR, Brazil) - jwvflauzino@inf.ufpr.br
- Eduardo A. P. Alchieri (UnB, Brazil) - alchieri@unb.br
- Elias P. Duarte Jr. (UFPR, Brazil) - elias@inf.ufpr.br

### Description

This repository contains the implementation of the FIT-SFC architecture and the instructions for reproducing the experiments presented in the paper submitted to [IEEE NFV-SDN 2024](https://nfvsdn2024.ieee-nfvsdn.org/).

# Abstract
A virtual network service can be implemented as a Service Function Chain (SFC) which is a composition of multiple Virtualized Network Functions (VNFs) forming the service topology. The IETF defines a standard architecture for SFCs, that includes traffic classification and forwarding elements. Considering that several network services implement functionalities that are critical for the correct operation of the network, the failure of an SFC can compromise the entire infrastructure, causing monetary losses or security issues. This work proposes the Fault- Intrusion Tolerant SFC (FIT-SFC): an architecture to support secure and highly available virtual services. While most of previous related work only assumes crash faults, FIT-SFC uses replication strategies to also tolerate intrusions on any component of the SFC architecture, while still being fully compliant with the IETF reference model. A prototype was implemented and experimental results show that FIT-SFC presents acceptable overhead and fast failover, tolerating faults/intrusions on both stateless and stateful services.

# Reproducing the Experiments

A prototype of the FIT-SFC architecture was implemented in Python 3 as a proof of concept. The experimental evaluation was conducted employing the [NFV Infrastructure Emulation Platform (NIEP)](https://ieeexplore.ieee.org/document/8432239).

The experiments presented in the paper can be reproduced by following the instructions listed below.

### 1. Set up

The first step before performing any of the experiments is to prepare the environment. **For this, please follow [these instructions](Set_up).**

### 2. Perform experiments

Once the environment has been properly prepared, **the experiments can be reproduced following the instructions below.** The experiments are independent, so they can be performed in any order.

#### [Experiment 1: DNS service latency when employing the FIT-SFC architecture](Experiment_1)
#### [Experiment 2: Authenticated DNS service latency when employing the FIT-SFC architecture](Experiment_2)
#### [Experiment 3: Load balancing when employing the FIT-SFC architecture](Experiment_3)
#### [Experiment 4: FIT-SFC architecture under crash failures](Experiment_4)
#### [Experiment 5: FIT-SFC architecture under intrusion](Experiment_5)
