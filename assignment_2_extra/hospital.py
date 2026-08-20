class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = "Standard"

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.name} | Category: {self.category} | Cost: ${self.treatment_cost:.2f}")


class GeneralPatient(Patient):
    def __init__(self, patient_id, name, treatment_cost):
        super().__init__(patient_id, name, treatment_cost)
        self.category = "General"


class SpecialPatient(Patient):
    def __init__(self, patient_id, name, treatment_cost):
        super().__init__(patient_id, name, treatment_cost)
        self.category = "Special"
        self.treatment_cost *= 1.15 


class Hospital:
    def __init__(self):
        self.patients = []
        self._cost_cache = {}

    def add_patient(self, patient):
        self.patients.append(patient)
        self._cost_cache.clear()

    def display_all_records(self):
        if not self.patients:
            print("No patient records found.")
            return
        print("\n--- Hospital Patient Records ---")
        for patient in self.patients:
            patient.display_info()

    def get_total_revenue(self):
        if "total_revenue" in self._cost_cache:
            print("(Retrieved from cache)")
            return self._cost_cache["total_revenue"]

        total = sum(p.treatment_cost for p in self.patients)
        self._cost_cache["total_revenue"] = total
        return total


if __name__ == "__main__":
    hospital = Hospital()
    hospital.add_patient(GeneralPatient(101, "Alice Smith", 500))
    hospital.add_patient(SpecialPatient(102, "Bob Jones", 1200))
    hospital.add_patient(GeneralPatient(103, "Charlie Brown", 300))

    hospital.display_all_records()
    print(f"\nTotal Revenue: ${hospital.get_total_revenue():.2f}")
    print(f"Total Revenue (Second call): ${hospital.get_total_revenue():.2f}")