import mysql.connector as mysql
HOST = "localhost" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "PC_DB"
# this is the user you create
USER = "root"
# user password
PASSWORD = ""
# connect to MySQL server
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())