# Access Dictionary Values
# Given student = {"name":"Maneesha", "age":22, "city":"Vizag"}, print the value of "age".
student = {
    "name" : "Maneesha",
    "age" : 22 ,
    "city" : "Vizag"
}
print("age :",student["age"])

# Check Key Existence
# Check if "name" exists in the dictionary and print Yes or No.
if "name" in student:
    print("yes")
else:
    print("no")