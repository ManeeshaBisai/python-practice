# Add new key-value pair
# Add "grade" : "A" to the above dictionary and print the updated dictionary.
student = {
    "name" : "Maneesha",
    "age" : 22 ,
    "city" : "Vizag"
}
#new_dict = {"grade" : "A"}
#student.update(new_dict)

student["grade"] = "A" # Overwrite
print(student)

# Update Value
student.update({"city" : "Bangalore"})
print(student)