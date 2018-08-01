#!/bin/bash

# Install 4kstogram
wget https://dl.4kdownload.com/app/4kstogram_2.6.15-1_amd64.deb

# Install necessary package
apt install libglu1-mesa libharfbuzz-bin qt5-default xvfb sqlite3

# Run 4kstogram and it would make *Picture/4k\ Stogram* at home path
