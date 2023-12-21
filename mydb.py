import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd = "my-secret-pw"
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE django_crm")

print("All done!")