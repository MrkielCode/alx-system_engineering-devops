#!/usr/bin/env bash
#This script performs some loop functions

count=1;

while [ $count -le 20 ]
do
	echo "$count"
	case $count in
		4)
			echo "bad luck from China"
			;;
		9)
			echo "bad luck from Japan"
			;;
		17)
			echo "bad luck from Italy"
			;;
	esac
	((count++))
done
