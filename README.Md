
## Create DATABASE
create database locally with name tenhourlab_workrequest

## Add Application Dependencies
`pip install -r requirements.txt`


## ENV File
1. Add a .env file to root directory of application
2. Add lines below to .env file
    ```
    DATABASE_URL=mysql+pymysql://<username>:<password>@localhost/tenhourlab_workrequest
    FLASK_ENV = development 
    ```

## RUN
```
flask db migrate
flask db upgrade
flask seed run  
flask run
```