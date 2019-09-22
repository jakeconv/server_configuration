# Web Server Project

## About
This repository contains files for connecting to an Amazon Lightsail instance running my Catalog Application project.
To access the application, please visit https://52.205.165.45

## Logging On to the Grader Account

To access the grader account, locate the private key submitted with the project.  The account name is grader, SSH is running on port 2200, and the IP address is 52.205.165.45.
On the server, this key is located in the grader's home folder as grader_rsa.
 
## Summary of Configurations Made

### Server Configuration
Upon creating the server, a selection of software packages were installed using apt-get, including Apache 2, the Apache 2 mod-wsgi module, Python, and Python Pip using the following:.

		sudo apt-get install apache2
		sudo apt-get install libapache2-mod-wsgi
		sudo apt-get install python
		sudo apt-get install python-pip

Also, the software on the server was updated by running:
		
		sudo apt-get upgrade

Remote logon to the root account was disabled, the default SSH port was changed to 2200, and key-based logon was configured to be a requirement.  This was accomplished by updating the sshd configuration located at /etc/ssh/sshd_config, then restarting the ssh service.

UFW was configured to allow communication on ports 80 (HTTP), 123 (NTP), 443 (HTTPS), and 2200 (SSH).  This was executed with the following commands:

		sudo ufw allow 80
		sudo ufw allow 123
		sudo ufw allow 443
		sudo ufw allow 2200
		sudo ufw enable

In addition, these ports needed to be opened on the Amazon Lightsail console.

The grader account was created, then added to the Sudoers group.  An RSA key pair was generated on my local machine with the ssh-keygen command.  The .ssh directory was created in the grader's home folder, then the public key was added to the grader's authorized_keys file.

With all of these steps complete, Apache 2 could be configured.

### Apache 2
Once Apache 2 and the WSGI module were installed on the server, they were configured to serve the Catalog application as a WSGI application.  A separate user account was created to run the application.  Per Facebook login requirements, this application needed to be configured to use HTTPS. This was accomplished by creating a security certificite, which I placed in /root/certs, and configuring Apache to redirect all requests to the server on port 80 to port 443.  A copy of the apache configuration can be found in this repository.

### Catalog Application
To run the catalog application on this server, the project files were cloned from GitHub into /var/www.  An app.wsgi file was created to call the application and run it.  The contents of app.wsgi can be found in this repository.  Any dependencies were installed using Pip including Flask and Sqlalchemy running the following commands:

		sudo pip install sqlalchemy
		sudo pip install flask

With this completed, the application is running at https://52.205.165.45

## References
The following resources were used to complete this project:
This guide was used to get the WSGI application up and running:
https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/#creating-a-wsgi-file

This guide was used to generate the self-signed security certificate and enable HTTPS on the application:
https://www.linode.com/docs/security/ssl/ssl-apache2-debian-ubuntu/

This guide was used to configure Apache to redirect all HTTP requests to HTTPS:
https://www.namecheap.com/support/knowledgebase/article.aspx/9821/38/apache-redirect-to-https
