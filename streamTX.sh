#!/bin/bash

raspivid -n -w 1280 -h 720 -b 10000000 -fps 30 -t 0 -o - | \
gst-launch-1.0 -v fdsrc blocksize=4096 !  h264parse ! queue2 ! rtph264pay config-interval=10 pt=96 \
! udpsink host=31.46.124.65 port=5000

