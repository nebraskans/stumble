# stumble

A web application for finding hidden locations.

# Setup

For smoothest installation and running use a python virtual environment.
 I used https://www.continuum.io/downloads. Command line installer
 should work fine.

1. install mySQL server here:
    - https://dev.mysql.com/downloads/mysql/
    - Save the password given during installation
    - https://dev.mysql.com/downloads/workbench/
    - Start mySQL server
    - Open mySQL workbench, enter password and keep new password blank
2. In the command line run `mysql -u root`
3. Then `Create DATABASE stumble;` and `control + D` to exit
4. Install mysql
    - `brew install mysql`
5. Move into django app
    - `cd stumble`
6. Install Python requirements
    - `pip install -r requirements.txt`
7. Now create a super user with
    - `python manage.py createsuperuser`


# Run
1. On macOS go to settings>>mysql and start server. Windows: IDK
2. To start Django app run:
    - `python manage.py runserver`
3. If prompted to apply migration run:
    - `python manage.py migrate`
4. Go to http://127.0.0.1:8000/ to visit the app
    - Admin page http://127.0.0.1:8000/admin

Leo Grande
