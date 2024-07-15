#!/bin/bash


sudo git add .

current_date=$(date +"%Y/%m/%d-%H:%M:%S")

sudo git commit -m "Version-$current_date"

sudo git push origin main
