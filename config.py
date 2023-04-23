from dotenv import dotenv_values

dotenv_file = dotenv_values(".env")

token = dotenv_file['TOKEN']
admin = [1274013505]

# DATABASE
host = dotenv_file['DB_HOST']
user = dotenv_file['DB_USER']
password = dotenv_file['DB_PASS']
db_name = dotenv_file['DB_DATABASE_NAME']