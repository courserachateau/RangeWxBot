#!/usr/bin/bash

today=$(date +"%Y-%m-%d")
fname="daily_log"
vladiate 2>&1| tee -a $fname".txt" | tee $fname"_$today.txt"

