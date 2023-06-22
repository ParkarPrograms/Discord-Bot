import requests
import json
import the_conversation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



url= "Discord Channel Here"

chrome_file_path = "C:\development\chromedriver.exe"

clyde= webdriver.Chrome(executable_path=chrome_file_path)





def get_nearest_message(channel_id):
    headers = {
        "authorization": "Discord Authorization"
    }
    r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers = headers)
    messages = json.loads(r.text)


    return (messages[0]['content'])


channel = "Channel ID"



clyde.get(url)

time.sleep(30)


actions = ActionChains(clyde)

response = ""
while True:
    words = get_nearest_message(channel)
    if words == response:
        pass
    else:
        response = the_conversation.get_response(words)
        actions.send_keys(response)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    time.sleep(10)

