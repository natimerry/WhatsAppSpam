import csv
import whatsapp
import sys

phone_list = []

# change to corresponding csv headers
phone_number_row_name = "WhatsApp Mobile Number"
class_row_name = "Class" 
department_row_name = "Department of Choice (you may choose more than one)"
name_row_name = "Name"


test_list = [
    # ("Maman","9830815568","Robotics, Competetive Programming, Web Development"),
    # ("Pritish",whatsapp.link_builder("7596842100"),2,"Competetive Programming, Web Development"),
    # ("Swapnil",whatsapp.link_builder("6291850508"),9,"Web Development"),
    # ("Aniruddha",whatsapp.link_builder("9830335689"),12,"Robotics, Competetive Programming, Web Development"),
    # ("Anjishnu",whatsapp.link_builder("9674533184"),2,"Competetive Programming, Web Development, Robotics"),
    # ("Arghya",whatsapp.link_builder("7439395427"),2,"Competetive Programming, Web Development, Robotics"),
    # ("Divyesha Singh",whatsapp.link_builder("9163966642"),2,"Competetive Programming, Web Development, Robotics"),
    ("Kakai",whatsapp.link_builder("9007226335"),2,"Competetive Programming, Web Development"),
            ]

with open('form.csv') as induction_form:
    reader = csv.DictReader(induction_form)
    for row in reader:
        name = row[name_row_name]
        category = row[department_row_name]
        if category.count(','):
            categories_set = set(category.split(", "))
        else:
            categories_set = {category}

        phone_list.append((
            name,
            whatsapp.link_builder(row[phone_number_row_name]),
            int(row[class_row_name]),
            categories_set            
        ))

whatsapp.send_message(test_list ,False)
#send messages to ppl with dupl names


    
