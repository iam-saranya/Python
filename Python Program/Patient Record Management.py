class Patient:
    def __init__(self, id, name, age, gender, diagnosis):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

class PatientRecordSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def view_all_patients(self):
        if not self.patients:
            print("No patients in the record.")
            return

        print("Patient Records:")
        for patient in self.patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                print(f"Patient found - ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")
                return

        print(f"No patient found with ID {patient_id}.")

    def remove_patient(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                self.patients.remove(patient)
                print(f"Patient removed - ID: {patient.id}, Name: {patient.name}")
                return

        print(f"No patient found with ID {patient_id}.")

def main():
    patient_system = PatientRecordSystem()

    while True:
        print("\nPatient Record Management System")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Remove Patient")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            diagnosis = input("Enter patient diagnosis: ")
            new_patient = Patient(id, name, age, gender, diagnosis)
            patient_system.add_patient(new_patient)

        elif choice == '2':
            patient_system.view_all_patients()

        elif choice == '3':
            patient_id = input("Enter patient ID to search: ")
            patient_system.search_patient(patient_id)

        elif choice == '4':
            patient_id = input("Enter patient ID to remove: ")
            patient_system.remove_patient(patient_id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
