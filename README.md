## Install Server

1. Create virtualenv

2. `pip install -t requirements.txt`

3. Add parameter to the `settings.py`
    
    `IS_SSO_SERVER = True`
    
    (by default this parameter equal true if environment variable IS_SSO_SERVER is exists)

3. Init database `./init.sh`

4. Start `./manage.py runserver 0.0.0.0:8000`


## Install Client

2. `pip install requirements.txt`

3. Init database `./init.sh`

4. Start `./manage.py runserver 0.0.0.0:8001`


#### Test login

1. Go to http://0.0.0.0:8001/login/

2. use login: `admin` and password: `123`

## Deploy

Use this project as template. Don't try inherit both apps from single project!