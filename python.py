import mysql.connector as c

def connect_to_db():
    return c.connect(
        host="localhost",       # Your MySQL host
        user="root",            # Your MySQL username
        passwd="Mysql@.11",     # Your MySQL password
        database="Covid_Vaccination_System"  # Your database name
    )
