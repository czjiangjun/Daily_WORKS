#! /bin/bash
sudo sed -i 's/bionic/focal/g' /etc/apt/sources.list
sudo apt update && sudo apt -y dist-upgrade
