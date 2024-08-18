import functions
import medicalRecord as mR
class Patient():


    def __init__(self,id):
        self.id = id
        self.medicalRecords = []

    def addPatientRecord(self):
        medicalRecord = functions.addNewMedicalRecords()
        self.medicalRecords.append(medicalRecord)

    def updatePatientRecord(self, testName, updateData):
        for record in self.medicalRecords:
            if record.testName == testName:
                record.updateRecord(**updateData)
            else:
                print("record not found")
    def deleteTest(self, testName):
        self.medicalRecords = [record for record in self.medicalRecords if record.testName != testName]

    def getTest(self, testName):
        for record in self.medicalRecords:
            if record.testName == testName:
                return record
        print("test Not found")
        return None

