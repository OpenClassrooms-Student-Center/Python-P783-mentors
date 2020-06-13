## Summary

Holiday lettings website

## Local development

### Prerequisites

- A GitHub account with read access to this repository
- Git CLI
- SQLite3 CLI
- A Python interpreter, version 3.6 or higher. 
- In the rest of the local development documentation, it is assumed the command `python` in 
your OS shell runs the above Python interpreter (unless a virtual environment is activated)

### Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/grking8/lettings-site.git`

#### Create the virtual environment

- `cd /path/to/lettings-site`
- `python -m venv lettings-site`
- `apt-get install python3-venv` (If previous step errors with package not found on Ubuntu)
- Activate the environment `source lettings-site/bin/activate`
- Confirm the command `python` now runs the Python interpreter in the virtual environment,
`which python`
- Confirm the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm the command `pip` runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/lettings-site`
- `source lettings-site/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser
- Confirm the site is running and can be navigated (you should see several profiles and lettings)

#### Database

- `cd /path/to/lettings-site`
- Open a shell session `sqlite3`
- Connect to the database `.open lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(profiles_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `CTRL+D` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`