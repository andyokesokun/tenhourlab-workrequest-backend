
# Create DATABASE
create database locally with name tenhourlab_workrequest

# Run Application Locally on cmd
pip install -r requirements.txt

Add a .env file to root directory of application

# PLACE INSIDE ENV

DATABASE_URL=mysql+pymysql://<username>:<password>@localhost/tenhourlab_workrequest
FLASK_ENV = development 

# RUN
flask db migrate
flask db upgrade
flask seed run  
flask run