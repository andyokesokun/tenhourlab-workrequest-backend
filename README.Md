
## Create Database
create database locally with name tenhourlab_workrequest

## Add Application Dependencies
`pip install -r requirements.txt`


## ENV File
1. create a filename named .env file to the root directory of the application
2. Add lines below to .env file
    ```
    DATABASE_URL=mysql+pymysql://<username>:<password>@localhost/tenhourlab_workrequest
    FLASK_ENV = development 
    ```
3. Replace values above with your env values 

## Run
```
flask db migrate
flask db upgrade
flask seed run  
flask run
```