#!/usr/bin/env bash
#This displays file

for file in *;
do
	if [[ "$file" != .* ]]
	then
		list_file=$(echo "$file" | cut -d '-' -f 2-)
		echo "$list_file"
	fi
done	
