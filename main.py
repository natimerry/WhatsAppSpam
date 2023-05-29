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
phone_number_row_name = "Phone No."
class_row_name = "Class" 
department_row_name = "Department of Choice (you may choose more than one)"
name_row_name = "Name"
links_row_name = "Links"

############################
#  _____ _____ ____ _____  #
# |_   _| ____/ ___|_   _| #
#   | | |  _| \___ \ | |   #
#   | | | |___ ___) || |   #
#   |_| |_____|____/ |_|   #
############################    

test_list = [
    # Add Tuples here
    # (Name:str, whatsapp.link_builder(PhoneNo:int), Class:int, Link:str)
    ("Pritish Dutta", whatsapp.link_builder("7596842100"), 10, "https://discord.gg/NCg8BPKArw"),
    ("Pritish Dutta", whatsapp.link_builder("9903737471"), 12, "https://discord.gg/NCg8BPKArw")
     ]

########################
#   ____ ______     __ #
#  / ___/ ___\ \   / / #
# | |   \___ \\ \ / /  #
# | |___ ___) |\ V /   #
#  \____|____/  \_/    #
########################

filename = "filtered.csv"
csvlist = whatsapp.returnDictData(filename, name_row_name, class_row_name, phone_number_row_name, links_row_name)

#####################################
#  _____ ___ _   _____ _____ ____   #
# |  ___|_ _| | |_   _| ____|  _ \  #
# | |_   | || |   | | |  _| | |_) | #
# |  _|  | || |___| | | |___|  _ <  #
# |_|   |___|_____|_| |_____|_| \_\ #
#####################################

# Set active list here...
active_list = test_list 


#############################
#  ____  _____ _   _ ____   #
# / ___|| ____| \ | |  _ \  #
# \___ \|  _| |  \| | | | | #
#  ___) | |___| |\  | |_| | #
# |____/|_____|_| \_|____/  #
#############################

# print(csvlist)
whatsapp.send_message(test_list, False)