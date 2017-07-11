# stumble

A web application for finding hidden locations.

# Dependencies

mysql-server

mysql-workbench

python-pip

**more in requirements.txt**

# Setup

For smoothest installation and running use a python virtual environment.Command line installer
 should work fine.

**On Linux/Ubuntu**

(Optional: work in a virtual environment)
1. Install dependencies
2. Set your SQL password to ''
3. Running MySQL

**On Linux/Ubuntu VERBOSE**

0. Pip
	- `sudo apt-get install python-pip`
	
(Optional: work in a virtual environment

	- `pip install virtualenv`
	- `pip install virtualenvwrapper`
	- `export WORKON_HOME=~/Envs`
	- `source /usr/local/bin/virtualenvwrapper.sh)`
	
1. In a terminal install the dependencies
	- `sudo apt-get install mysql-server`
	- `sudo apt-get install mysql-workbench`
2. Start the SQL server
	- `sudo /etc/init.d/mysql start`
3. Running MySQL
	- `mysql -u root -p`
	- input your password

**MacOS**

1. install mySQL server here:
    - https://dev.mysql.com/downloads/mysql/
    - `brew install mysql`
    - Save the password given during installation
    - https://dev.mysql.com/downloads/workbench/
    - Start mySQL server
    - Open mySQL workbench, enter password and keep new password blank
2. In the command line run `mysql -u root`

**ALL**

1. Create a Database in MySQL
	- `Create DATABASE stumble;` CTRL+D
2. Install requirements.txt
	- `pip install -r requirements.txt`
3. Create your superuser
	- `python manage.py createsuperuser`
4. Visit 127.0.0.1:800 to see the app
	- /admin is admin page


# Run

1. On macOS go to settings>>mysql and start server. Windows: IDK
2. To start Django app run:
    - `python manage.py runserver`
3. If prompted to apply migration run:
    - `python manage.py migrate`
4. Go to http://127.0.0.1:8000/ to visit the app
    - Admin page http://127.0.0.1:8000/admin

# Cheatsheets

MySQL

MySQL Workbench
https://dev.mysql.com/doc/workbench/en/wb-launching-linux.html

Git
https://www.git-tower.com/blog/git-cheat-sheet/

Virtual Environments
http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
