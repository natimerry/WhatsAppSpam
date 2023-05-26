from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from messages import message_builder
import os

def link_builder(number:str):
    if len(number) > 10:
        number=number[-10:]
    return f"https://web.whatsapp.com/send?phone=%2B91{number}&text&app_absent=0"

def load_dump():
    l = set()
    if os.path.exists("./dump.txt"):
        with open("./dump.txt") as dumpfile:
            for line in dumpfile.read().split():
                l.add(line)
    print(f"Names loaded from already sent: {l}")
    return l


def type_message(driver:any,message):
    action_chain = ActionChains(driver)
    sleep(1)
    for character in message:
        action_chain.send_keys(character)
    sleep(1)
    action_chain.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
    sleep(2)
    action_chain.reset_actions()
    action_chain.send_keys(Keys.RETURN).perform()
    sleep(3.5)

def message_builder(name:str,cat_set:set,grade:int) -> str:
    # from messages import cp_message,robo_message,dev_message
    from messages import   disc_message as   disc_message
    message = f"Greetings {name}, \n{ disc_message}"
    # if 'Robotics' in cat_set:
    #     message += f"\n{robo_message}"

    # if 'Web Development' in cat_set:
    #     message+=f"\n{dev_message}"
        
    # if 'Competetive Programming' in cat_set:
    #     message += f"\n{cp_message}"
        
    message.format(name=name)
    # print(message)
    return message

def send_message(links:list,dry_run:bool):
    dump = load_dump()
    #firefox profile goes here

    ff_profile:str = "/home/jay/.mozilla/firefox/9r1xcgqx.default-release"
    # Define ff_profile yourself

    driver = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(ff_profile)) 
    driver.get('https://web.whatsapp.com')
    wait = WebDriverWait(driver, 100)
    count = 0
    total = len(links)
    import time
    for link_tuple in links:
        start = time.time()
        count+=1
        name,link,grade,cat_set = link_tuple
        if name.count(' '):
            name = name.split()[0]
        if link in dump:
            continue
        print(f"{count} of {total} {link_tuple}")
        if name.count(' '):
            name = name.split()[0]
        
        message = message_builder(name,cat_set,grade)
        driver.get(link)
        textField = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fd365im1')))
        
        if not dry_run:
            type_message(driver=driver,message=message)
            with open("./dump.txt","a") as dumpfile:
                dumpfile.write(f"{link}\n")
                print(f"Dumped {name} to file")
        else:
            sleep(3)
        end = time.time()
        print(f"Elapsed time: {end - start}")
    driver.close()

def announce(message:str, class_cat:set = None, dept_set:set = None):
    pass