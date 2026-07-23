class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def priority(self):
        if self.treatment_cost > 50000:
            return "Special Priority"
        else:
            return "General Priority"

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients(self):
        print(f"Hospital: {self.name}")
        for patient in self.patients:
            print(f"Patient ID: {patient.patient_id}, Name: {patient.name}, Treatment Cost: ${patient.treatment_cost}, Priority: {patient.priority()}")
            print("-" * 30)

hospital = Hospital("City Hospital")
patient1 = Patient(1, "John Doe", 60000)
patient2 = Patient(2, "Jane Smith", 30000)
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.display_patients()