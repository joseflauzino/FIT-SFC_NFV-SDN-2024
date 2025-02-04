#!/bin/bash
#USAGE: source SFF.sh <int_ip_iface> <int_ip> 

curr_folder=$(pwd)
if [[ $curr_folder =~ (.+)"/CLI"(.*) ]];
then
	ifconfig $1 $2
	ip route add default dev $1
	cd ${BASH_REMATCH[1]}/FIT-SFC_NFV-SDN-2024/Components/
	python3 SFF.py $2 $1
else
	python3 SFF.py $2 $1
fi

