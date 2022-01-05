#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:07:16 2022

@author: izuchukwumatthew
"""

Steps

1 Set up and deploy EC2 using a PEM key and open ports 22 (SSH) and 3306 (MySQL)

2 Connect to the EC2 instance using the terminal -ssh

3 Change directory to downloads (This is where the PEM key is stored)

4 Open "Cam_AHI.pem" ubuntu@ec2-44-198-59-25.compute-1.amazonaws.com Run the following command after connecting to the machine: Sudo apt-get update

5 Create user (UBUNTU)

6 add user 'USERNAME' and passwd 'PASSWORD'

7 Edit the configuration: etc/ssh/sshd_config	  

8 Set Password Authentication and permit root login to yes 

9 Install MySQL :install mysql-client mysql-server

10 Update listings
###sudo apt-get update 
#To check Status
###sudo service mysql status
###will display 'actively running)

11 Change bin address to 0.0.0.0
#sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

12 Restart MySQL to make sure it was updated
#sudo service mysql restart
#Start MySQL
###Sudo MySQL

13 Create a MySQL user
###Create user 'DBA'@'%' IDENTIFIED BY 'PASSWORD';

14 Grant all privileges to SQL user

	GRANT ALL PRIVILEGES ON *.* TO 'DBA'@% WITH GRANT OPTION;

	Show grants 

15 Create a database
###CREATE DATABASE e2e

16 Write Python script to insert csv data

17 See Python Script Notebook attachment 

18 Create a dump (.sql) file
###mysqldump -u DBA -p e2e > e2e_dump.sql
###sudo mysqldump-apt e2e>e2e_dump.sql
(the command ls will show the dump file created)

19 Launch a second ec2 instance using AWS or Azure
### Open Ports 22 and 3306

22 Connect machine in the teminal 
#SCP to local Machine
###scp e2e_dump.sql client@52.170.46.178:/home/client

23 On second instanc, input the following command:
###sudo mysql e2e < e2e_dump.sql

24 Create Trigger
###See sql file attachment 