#############################################
#  ___ __  __ ____   ___  ____ _____ ____   #
# |_ _|  \/  |  _ \ / _ \|  _ \_   _/ ___|  #
#  | || |\/| | |_) | | | | |_) || | \___ \  #
#  | || |  | |  __/| |_| |  _ < | |  ___) | #
# |___|_|  |_|_|    \___/|_| \_\|_| |____/  #
##############################################                                       

import csv
import whatsapp
import sys

# change to corresponding csv headers
phone_number_row_name = "WhatsApp Mobile Number"
class_row_name = "Class" 
department_row_name = "Department of Choice (you may choose more than one)"
name_row_name = "Name"

############################
#  _____ _____ ____ _____  #
# |_   _| ____/ ___|_   _| #
#   | | |  _| \___ \ | |   #
#   | | | |___ ___) || |   #
#   |_| |_____|____/ |_|   #
############################    

test_list = [
    # Add Tuples here
    # (Name:str, whatsapp.link_builder(PhoneNo:int), Class:int, Departments:str)
    ("Nandy",whatsapp.link_builder("9903737471"),11,"Competetive Programming, Web Development, Robotics"),
    ("Divyesha Singh",whatsapp.link_builder("9163966642"),12,"Competetive Programming, Web Development, Robotics"),
    ("Anjishnu",whatsapp.link_builder("9674533184"),8,"Competetive Programming, Web Development, Robotics")
     ]

########################
#   ____ ______     __ #
#  / ___/ ___\ \   / / #
# | |   \___ \\ \ / /  #
# | |___ ___) |\ V /   #
#  \____|____/  \_/    #
########################

filename = "form.csv"
csvlist = whatsapp.returnDictData(filename, name_row_name, class_row_name, phone_number_row_name, department_row_name)

#####################################
#  _____ ___ _   _____ _____ ____   #
# |  ___|_ _| | |_   _| ____|  _ \  #
# | |_   | || |   | | |  _| | |_) | #
# |  _|  | || |___| | | |___|  _ <  #
# |_|   |___|_____|_| |_____|_| \_\ #
#####################################

# Set active list here...
active_list = test_list 

filtered = []

for user in active_list:
    print(user[2])
    if user[2]>8:
        filtered.append(user)

#############################
#  ____  _____ _   _ ____   #
# / ___|| ____| \ | |  _ \  #
# \___ \|  _| |  \| | | | | #
#  ___) | |___| |\  | |_| | #
# |____/|_____|_| \_|____/  #
#############################

whatsapp.send_message(filtered, False)

