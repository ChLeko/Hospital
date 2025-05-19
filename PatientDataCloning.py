import copy

# Patient class with attributes (Name, Age, Diagnosis, Address)
class Patient:
    def __init__(self, name, age, diagnosis, address):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.address = address  # Address can be a dictionary (to simulate nested data)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, Address: {self.address}"

# Test Case to demonstrate Shallow and Deep Copy
def test_case():
    # Original patient object
    patient1 = Patient("John Doe", 45, "Hypertension", {"street": "123 Main St", "city": "Springfield", "zip": "12345"})

    # Shallow copy of the patient object
    shallow_copy_patient = copy.copy(patient1)

    # Deep copy of the patient object
    deep_copy_patient = copy.deepcopy(patient1)

    # Modifying the shallow copy's address
    shallow_copy_patient.address["city"] = "Shelbyville"
    shallow_copy_patient.name = "John Smith"  # Modify name to show that it's a shallow copy

    # Modifying the deep copy's address
    deep_copy_patient.address["street"] = "456 Elm St"
    deep_copy_patient.name = "James Doe"  # Modify name to show that it's a deep copy

    # Printing original and copies to show the effects of modifications
    print("Original Patient:")
    print(patient1)

    print("\nShallow Copy Patient (after modification):")
    print(shallow_copy_patient)

    print("\nDeep Copy Patient (after modification):")
    print(deep_copy_patient)

# Running the test case
test_case()
