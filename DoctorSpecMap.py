from enum import Enum

# Enum for Doctor Specializations
class Specialization(Enum):
    CARDIOLOGY = "Cardiology"
    NEUROLOGY = "Neurology"
    ORTHOPEDICS = "Orthopedics"
    PEDIATRICS = "Pediatrics"
    DERMATOLOGY = "Dermatology"
    GYNECOLOGY = "Gynecology"
    GENERAL_MEDICINE = "General Medicine"

# Dictionary (Map) for Doctor Records
class DoctorSpecializationMap:
    def __init__(self):
        self.doctor_map = {}  # Map to store doctor name and their specialization
    
    # Add a doctor record (Name -> Specialization)
    def add_doctor(self, doctor_name, specialization):
        if doctor_name not in self.doctor_map:
            self.doctor_map[doctor_name] = specialization
            print(f"Doctor {doctor_name} added with specialization {specialization.value}.")
        else:
            print(f"Doctor {doctor_name} already exists.")
    
    # Update a doctor's specialization
    def update_specialization(self, doctor_name, new_specialization):
        if doctor_name in self.doctor_map:
            self.doctor_map[doctor_name] = new_specialization
            print(f"Doctor {doctor_name}'s specialization updated to {new_specialization.value}.")
        else:
            print(f"Doctor {doctor_name} not found.")
    
    # Delete a doctor record
    def delete_doctor(self, doctor_name):
        if doctor_name in self.doctor_map:
            del self.doctor_map[doctor_name]
            print(f"Doctor {doctor_name} has been deleted.")
        else:
            print(f"Doctor {doctor_name} not found.")
    
    # Retrieve a doctor's specialization
    def get_specialization(self, doctor_name):
        if doctor_name in self.doctor_map:
            return f"Doctor {doctor_name} specializes in {self.doctor_map[doctor_name].value}."
        else:
            return f"Doctor {doctor_name} not found."

    # Display all doctor records
    def display_all_doctors(self):
        if not self.doctor_map:
            print("No doctor records found.")
        else:
            for doctor, specialization in self.doctor_map.items():
                print(f"Doctor {doctor} specializes in {specialization.value}.")

# Test Case
def test_case():
    # Creating an instance of DoctorSpecializationMap
    doctor_map = DoctorSpecializationMap()
    
    # Adding some doctor records
    doctor_map.add_doctor("Dr. Smith", Specialization.CARDIOLOGY)
    doctor_map.add_doctor("Dr. Johnson", Specialization.NEUROLOGY)
    doctor_map.add_doctor("Dr. Brown", Specialization.ORTHOPEDICS)
    
    # Retrieving and displaying doctor specialization
    print(doctor_map.get_specialization("Dr. Smith"))
    print(doctor_map.get_specialization("Dr. Johnson"))
    
    # Updating a doctor's specialization
    doctor_map.update_specialization("Dr. Brown", Specialization.DERMATOLOGY)
    print(doctor_map.get_specialization("Dr. Brown"))
    
    # Deleting a doctor record
    doctor_map.delete_doctor("Dr. Johnson")
    print(doctor_map.get_specialization("Dr. Johnson"))
    
    # Displaying all doctors
    print("\nAll Doctors in the system:")
    doctor_map.display_all_doctors()

# Running the test case
test_case()
