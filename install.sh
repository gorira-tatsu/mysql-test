#!/bin/sh

sudo apt -y update
sudo apt -y install mysql-server=8.0.28-0ubuntu0.20.04.3
sudo apt -y install python3
sudo apt -y install python3-pip
pip3 install mysql-connector-python==8.0.28


sudo mysql -e "CREATE USER 'tester'@'localhost'
  IDENTIFIED BY 'getwild';
GRANT ALL
  ON *.*
  TO 'tester'@'localhost'
  WITH GRANT OPTION;"


mysql -u tester -pgetwild < schema.sql

python3 makedata.py
