# Lnks API with Python


## Config
1. Create file `.env` in root project
2. Create your database MongoDB
3. Add your database url in `DATABASE_URL` variable
4. Add your database name in `DATABASE_NAME` variable
5. Add your secret key in `SECRET_KEY` variable

## Start development

1. Install dependencies `pip install -r requirements.txt`
2. Run `uvicorn main:app --reload`


## Database
Use MongoDB Atlas for database and PyMongo for connection.


## Todo

- [x] Basic App
- [x] Router Base
- [x] Config file (env file)
- [x] DB Config
- [x] Module Hashing - (Verify Password and Hasher password bcrypt)
- [x] Module Security - (create token, verify token)
- [x] Router SignUp (Model User)
- [x] Router Login
- [] Router Links (Model Link)
