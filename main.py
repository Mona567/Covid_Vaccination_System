import mysql.connector as c

def connect_to_db():
    return c.connect(
        host="localhost",       
        user="root",
        passwd="Mysql@.11",    
        database="Covid_Vaccination_System"  
    )


if con.is_connected():
    print("True")
