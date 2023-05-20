main_body = '''
Congratulations on becoming a member of Dehli Public School Ruby Park's Tech Club! Your passion for technology and dedication to exploring its vast possibilities have brought you here. We're excited to have you on board, and we can't wait to see the amazing contributions you'll bring to our community. Get ready to embark on an incredible journey of innovation and growth. Let's dive into coding, robotics, development, and much more. 

Click the adjoining link(s) to join us and begin your electrifying journey with the club.

*Your Deparments:*
'''

robo_message = "Join the Robotics Group: https://chat.whatsapp.com/CUJa9PLxB6AETNiQCYTLrT\n"
cp_message = "Join the Competetive Programming Group: https://chat.whatsapp.com/I0af6PO2uI0Jf806vfkVLm\n"     
dev_message = "Join the Development Group: https://chat.whatsapp.com/DKU5w4VwWVQ2xy3DCnqtQa\n" 


def message_builder(name:str,cat_set:set,grade:int) -> str:
    message = f"Greetings, {name}{main_body}"
    if 'Robotics' in cat_set:
        message += f"\n{robo_message}"

    if 'Web Development' in cat_set:
        message+=f"\n{dev_message}"
        
    if 'Competetive Programming' in cat_set:
        message += f"\n{cp_message}"
    
    message.format(name=name)
    # print(message)
    return message