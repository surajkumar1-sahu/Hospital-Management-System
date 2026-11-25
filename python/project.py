
patients = {}
next_id = 101

def add_patient():
    global next_id
    name = input("Enter Name: ")
    if name == "":
        print("Name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: "))
        if age < 0 or age > 120:
            print("Invalid age. Enter a number between 0 and 120.")
            print("Patient not added.")
            return
    except ValueError:
        print("Invalid age. Enter a number between 0 and 120.")
        print("Patient not added.")
        return

    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor: ")

    pid = "P" + str(next_id)
    patients[pid] = {
        "Name": name,
        "Age": age,
        "Disease": disease,
        "Doctor": doctor
    }

    print("Patient added. ID:", pid, "|", name, "|", age, "|", disease, "|", doctor)
    next_id += 1


def view_patients():
    if len(patients) == 0:
        print("No patient records found.")
    else:
        for pid, data in patients.items():
            print(pid, data)


def search_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        print(pid, patients[pid])
    else:
        print("Patient ID not found.")


def update_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        disease = input("Enter New Disease: ")
        patients[pid]["Disease"] = disease
        print("Patient", pid, "updated. Disease:", disease)
    else:
        print("Patient ID not found.")
        

def delete_patient():
    pid = input("Enter Patient ID: ")
    if pid in patients:
        del patients[pid]
        print("Patient", pid, "deleted. Total patients:", len(patients))
    else:
        print("Patient ID not found.")


while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        update_patient()
    elif choice == "5":
        delete_patient()
    elif choice == "6":
        print("Thank you for using Hospital Management System.")
        break
    else:
        print("Invalid choice. Please try again.")




# 1	ADD	    Add a new patient
# 2	VIEW	See all patients
# 3	SEARCH	Find a patient by ID
# 4	UPDATE	Change patient details
# 5	DELETE	Remove a patient
# 6	EXIT	Close the program
