import mysql.connector as c

def connect_to_db():
    return c.connect(
        host="localhost",       
        user="root",
        passwd="Mysql@.11",    
        database="Covid_Vaccination_System"  
    )

db = connect_to_db()
if db.is_connected():
    print("True")


def add_patient():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender (Male/Female/Other): ")
    contact = input("Enter Patient Contact: ")
    address = input("Enter Patient Address: ")

    db = connect_to_db()
    cursor = db.cursor()

    query = "INSERT INTO Patients (name, age, gender, contact, address) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, gender, contact, address)
    cursor.execute(query, values)

    db.commit()
    print("Patient added successfully!")
    db.close()


def view_patients():
    db = connect_to_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Patients")
    result = cursor.fetchall()

    for row in result:
        print(row)

    db.close()


def add_vaccine():
    vaccine_name = input("Enter Vaccine Name: ")
    doses_required = int(input("Enter Doses Required: "))

    db = connect_to_db()
    cursor = db.cursor()

    query = "INSERT INTO Vaccines (vaccine_name, doses_required) VALUES (%s, %s)"
    values = (vaccine_name, doses_required)
    cursor.execute(query, values)

    db.commit()
    print("Vaccine added successfully!")
    db.close()


def schedule_appointment():
    patient_id = int(input("Enter Patient ID: "))
    center_id = int(input("Enter Center ID: "))
    vaccine_id = int(input("Enter Vaccine ID: "))
    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
    dose_number = int(input("Enter Dose Number: "))

    db = connect_to_db()
    cursor = db.cursor()

    query = "INSERT INTO Appointments (patient_id, center_id, vaccine_id, appointment_date, dose_number, status) VALUES (%s, %s, %s, %s, %s, 'Pending')"
    values = (patient_id, center_id, vaccine_id, appointment_date, dose_number)
    cursor.execute(query, values)

    db.commit()
    print("Appointment scheduled successfully!")
    db.close()


def main():
    while True:
        print("\n--- COVID Vaccination Management System ---")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Vaccine")
        print("4. Schedule Appointment")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_patient()
        elif choice == 2:
            view_patients()
        elif choice == 3:
            add_vaccine()
        elif choice == 4:
            schedule_appointment()
        elif choice == 5:
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if _name_ == "_main_":
    main()