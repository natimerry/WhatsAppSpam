# main_body = '''
# Congratulations on becoming a member of Delhi Public School Ruby Park's Tech Club! Your passion for technology and dedication to exploring its vast possibilities have brought you here. We're excited to have you on board, and we can't wait to see the amazing contributions you'll bring to our community. Get ready to embark on an incredible journey of innovation and growth. Let's dive into coding, robotics, development, and much more. 

# Click the adjoining link(s) to join us and begin your electrifying journey with the club.

# *Your Department:*
# '''

# robo_message = "*Robotics*\nJoin the Robotics Group: https://chat.whatsapp.com/CUJa9PLxB6AETNiQCYTLrT\n"
# cp_message = "*Competitive Programming*\nJoin the Competitive Programming Group: https://chat.whatsapp.com/I0af6PO2uI0Jf806vfkVLm\n"     
# dev_message = "*Development*\nJoin the Development Group: https://chat.whatsapp.com/DKU5w4VwWVQ2xy3DCnqtQa\n" 

def message_builder(name:str,grade:int,link:str) -> str:
    message = f"""Attention, tech enthusiasts of classes 9 and above! We're thrilled to invite you to our exclusive Discord server to engage in fascinating discussions about technology and beyond. This  is not compulsory at all and only aims to build peer relations within the Club 

Before you hop on board, we'd like to emphasise the importance of maintaining a respectful environment. Inappropriate conduct will not be tolerated (spamming included). Strict actions shall be taken in event of violation of the same. 

Join us on Discord, learn, share and collaborate to take your passion to new heights! 
{link}

*Please note*
While important announcements will be shared both on our Discord server and WhatsApp, a majority of the same shall be shared on our WhatsApp group only.
"""

    message.format(name=name)
    # print(message)
    return message