# 0 is for 1st name,
# 1 is for last name
# student = ["Ana", "Henderson", "Chemistry", 92]

# dictionaries
student = {
    "first_name": "Ana",
    "last_name": "Henderson",
    "subject": "Chemistry",
    "grade": 92, 
    "contact_details": {
        "phone": "+447759779252",
        "email": "ewoyidan@gmail.com"
    }
}
# print(student)

#print(student["date_of_birth"])

# student["date-of_birth"] = "1990-01-01"
# print("first_name" in student)

# student["grade"] = 95 # to alter the dict
# print(student)

# print(student.keys()) # brings out all information in a dict

# how to use nested dicts
# get only Ana's phone number
print(student["contact_details"]["phone"]) 