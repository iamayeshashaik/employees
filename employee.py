import json


file = open("D:\\One Drive Storage\\OneDrive\\Documents\\Python Class(VS Code)\\Ayesha Python\\Edyoda\\employee.json")
data = json.load(file)
for i in data["employees"]:
    print(i)

dic = {
    "Telangana" : "Hyderabad",
    "Tamilnadu" : "Chennai",
    "Karnataka" : "Banglore",
    "Maharastra" : "Mumbai",
    "Assam" : "Dispur",
    "Bihar" : "Patna",
    "Goa" : "Panaji"
}