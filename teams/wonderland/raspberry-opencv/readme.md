# Raspberry Pi OpenCV Server

## main.py

Run on PC.

Set the raspberry pi IP address in the script and get current objects in the webcam.

## server.py

Run on Raspberry Pi. Put the script in `/home/pi/workspace/ncappzoo/apps/street_cam` folder.

A simple HTTP server to provide the webcam data.

## vstreet_cam.py

Run on Raspberry Pi. Put the script in the `/home/pi/workspace/ncappzoo/apps/street_cam` folder.

Kernel script to identify the objects in the webcam.
