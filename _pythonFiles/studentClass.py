class Student:

    onboardingPaths = {"Marketing": "Inside Sales On-boarding",
                       "Sales": "Sales On-boarding",
                       "Solutions Consultants": "Client Services On-boarding",
                       "Success": "Client Delight On-boarding"
                      }
    num_of_students = 0

    def __init__(self, studentID, department, onboardingDate):
        self.studentID = studentID
        self.department = department
        self.onboardingDate = onboardingDate

        Student.num_of_students += 1

    def getOnboardingPath(self):
        return self.onboardingPaths[self.department]

print(Student.num_of_students)
student1 = Student("12345", "Sales", "2016-02-15")
student2 = Student("67890", "Marketing", "2019-01-01")
print(Student.num_of_students)

print(student1.studentID)
print(student1.getOnboardingPath())
