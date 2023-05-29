# main_body = '''
# Congratulations on becoming a member of Delhi Public School Ruby Park's Tech Club! Your passion for technology and dedication to exploring its vast possibilities have brought you here. We're excited to have you on board, and we can't wait to see the amazing contributions you'll bring to our community. Get ready to embark on an incredible journey of innovation and growth. Let's dive into coding, robotics, development, and much more. 

# Click the adjoining link(s) to join us and begin your electrifying journey with the club.

# *Your Department:*
# '''

# robo_message = "*Robotics*\nJoin the Robotics Group: https://chat.whatsapp.com/CUJa9PLxB6AETNiQCYTLrT\n"
# cp_message = "*Competitive Programming*\nJoin the Competitive Programming Group: https://chat.whatsapp.com/I0af6PO2uI0Jf806vfkVLm\n"     
# dev_message = "*Development*\nJoin the Development Group: https://chat.whatsapp.com/DKU5w4VwWVQ2xy3DCnqtQa\n" 

def message_builder(name:str,grade:int,link:str) -> str:
    message = f"""Attention, tech enthusiasts in classes 9 and above! We're thrilled to invite you to join our exclusive Discord server and engage in fascinating discussions about technology and beyond.

Before you hop on board, we'd like to emphasize the importance of maintaining a respectful and positive environment. Inappropriate behavior will not be tolerated, including spamming or disruptive conduct. Remember, actions have consequences, and we strive to cultivate a space that fosters meaningful interactions.

While important announcements will be shared both on our Discord server and through WhatsApp, please note that certain updates, session polls, etc. may be shared only on our WhatsApp group. 

Join us on Discord and be part of a vibrant community of tech enthusiasts, where you can share your knowledge, learn from others, and engage in stimulating conversations: 

{link}"""

    message.format(name=name)
    # print(message)
    return message