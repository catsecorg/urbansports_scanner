#!/bin/sh
gobuster dir -u https://urbansportsclub.com/de/ -w /home/catsec/Urbansportsclub/Firmen.txt > urbanscan.txt &
BACK_PID=$!

while kill -0 $BACK_PID ; do
    sleep 30
    # You can add a timeout here if you want
done

python3 urbansportsclub.py urban_price.txt &
BACK_PID=$!

while kill -0 $BACK_PID ; do
    sleep 30
    # You can add a timeout here if you want
done




