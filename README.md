## Summary

Holiday lettings website

## Local development

### Prerequisites

- GitHub account with read and write access to this repository's code
- Access to the CircleCI project `lettings-site`
- Heroku account
- Git CLI
- SQLite3 CLI
- Python interpreter, version 3.6 or higher
- Sentry account
- Dockerhub account

In the rest of the local development documentation, it is assumed the command `python` in 
your OS shell runs the above Python interpreter (unless a virtual environment is activated)



### macOS / Linux

#### Clone the repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/grking8/lettings-site.git`

#### Create the virtual environment

- `cd /path/to/lettings-site`
- `python -m venv venv`
- `apt-get install python3-venv` (If previous step errors with package not found on Ubuntu)
- Activate the environment `source venv/bin/activate`
- Confirm the command `python` now runs the Python interpreter in the virtual environment,
`which python`
- Confirm the version of the Python interpreter is 3.6 or higher `python --version`
- Confirm the command `pip` runs the pip executable in the virtual environment, `which pip`
- To deactivate the environment, `deactivate`

#### Run the site

- `cd /path/to/lettings-site`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Go to `http://localhost:8000` in a browser
- Confirm the site is running and can be navigated (you should see several profiles and lettings)

#### Linting

- `cd /path/to/lettings-site`
- `source venv/bin/activate`
- `flake8`

#### Unit tests

- `cd /path/to/lettings-site`
- `source venv/bin/activate`
- `pytest`

#### Database

- `cd /path/to/lettings-site`
- Open a shell session `sqlite3`
- Connect to the database `.open lettings-site.sqlite3`
- Display tables in the database `.tables`
- Display columns in the profiles table, `pragma table_info(profiles_profile);`
- Run a query on the profiles table, `select user_id, favorite_city from profiles_profile where favorite_city like 'B%';`
- `.quit` to exit

#### Admin panel

- Go to `http://localhost:8000/admin`
- Login with user `admin`, password `Abc1234!`

### Windows

Using PowerShell, as above except

- To activate the virtual environment, `.\venv\Scripts\Activate.ps1` 
- Replace `which <my-command>` with `(Get-Command <my-command>).Path`

## Deployment

- In the Heroku dashboard
    - Copy the API key `<heroku-api-key>`
    - Create a new app `<heroku-app-name>` (if you leave the field blank, Heroku will create a
    name for you)
    - In Settings -> Config Vars, add the variables below with the appropriate values from Sentry
        - `LETTINGS_SITE_SENTRY_AUTH`
        - `LETTINGS_SITE_SENTRY_PROJECT_ID`
- In CircleCI, create environment variables
    - `HEROKU_API_KEY` with value `<heroku-api-key>`
    - `HEROKU_APP_NAME` with value `<heroku-app-name>`
    - Trigger a build via the CircleCI web console or by pushing a commit to `master`
- Navigate to `https://<heroku-app-name>.herokuapp.com` in a browser
- Confirm the site is running
- Navigate to `https://<heroku-app-name>.herokuapp.com/sentry-debug`, should see error appear
in Sentry
- Login to the admin panel using above credentials

## Containerisation

- `Dockerfile` in this repository can be run locally `docker run --rm --publish 8000:8000 guydocker/lettings-site:0d2608cffcac0a22412f7534391dc1b0e476f913 runserver 0.0.0.0:8000` after authentication / the registry being made public
- To test the above, navigate to `http://localhost:8000/admin`, you should see the site running
