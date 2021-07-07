import os
try:
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY'] #CHANGE THIS!
    APP_EMAIL = ""
    DB_URI = os.environ['DB_URI']
    CURRENT_DB = "todo_database"
    USERS_COLLECTION = "users"
except KeyError as key:
    print(f'{key} does not exist in this env.')
    os.abort()