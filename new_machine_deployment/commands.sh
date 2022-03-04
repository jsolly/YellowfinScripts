#!/bin/bash
sudo apt update -y        # Fetches the list of available updates
sudo apt upgrade -y       # Installs some updates; does not remove packages
sudo apt full-upgrade -y  # Installs updates; may also remove some packages, if needed
sudo apt autoremove -y    # Removes any old packages that are no longer needed
sudo apt-get install zip unzip -y
sudo apt install curl -y
sudo reboot
# See doc on installing SDK man for Java

# Postgres
# Apt-get install postgresql

# MySQL
#sudo apt install mysql-server