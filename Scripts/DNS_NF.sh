#!/bin/bash
#USAGE: source DNS_NF.sh <int_ip_iface> <int_ip> 

curr_folder=$(pwd)
if [[ $curr_folder =~ (.+)"/CLI"(.*) ]];
then
	ifconfig $1 $2
	ip route add default dev $1
	cd ${BASH_REMATCH[1]}/FIT-SFC_NFV-SDN-2024/DNS/
	python3 DNS_NF.py $2
else
	python3 DNS_NF.py $2
fi
