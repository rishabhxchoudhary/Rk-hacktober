from selenium import webdriver 
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options 
from tkinter import messagebox as mb 
from winsound import Beep 
from bs4 import BeautifulSoup       #For webscraping 
import pyautogui as p               #For controlling mouse and keyboard virtually 
import webbrowser as w              #For opening web.whatsapp.com 
import requests                     #For webscraping 
import time 
import random 
import wikipedia as wk              #For info on a particular topic 
import re                           #"Tel me about xyz" For extracting xyz from sentence 
from urllib.request import urlopen 
 
target = input("Enter conatct name: ")#Time of targeted contact 
nocase = True 
url = "https://web.whatsapp.com/" 
oldmsg = '' 
counter1 = 0 
counter2 = 0 
counter3 = 0 
counter4 = 0 
counter5 = 0 
choce = ["God!",                    #Some common prefixes 
    "Mannn! I have already told you!", 
    "You forgot so easily!", 
    "Come on, I already told you", 
    "Do I need to say again?" 
    "I think I have told you once before"] 
 
def able_to_find_qrcode():          #Wait till QR code is present 
    try: 
        qrcode = driver.find_element_by_class_name("_1pw2F") 
        return True 
    except: 
        return False 
 
def close(): 
    driver.quit() 
 
def find_contact():                 #Finds contact from contact list 
    global contact 
    try: 
        contact = driver.find_element_by_class_name("r7sRK") 
        return False 
    except: 
        return True 
 
def find_sf():                 #Finds contact from contact list 
    global serchf 
    try: 
        serchf = driver.find_element_by_class_name("eiCXe") 
        return False 
    except: 
        return True 
if target.isdigit(): 
    if len(target) >= 10: 
        countrycode = input("You entered a phone number, enter the country code: ") 
        target = countrycode+target  
        url = url+"send?phone=%s"%target 
        nocase = False 
 
##print(target) 
##print(url) 
##input() 
driver = webdriver.Chrome(r'C:\Users\pc\Desktop\chromedriver_win32\chromedriver.exe') 
driver.get(url) 
Beep(300,200) 
Beep(400,200) 
print("SCAN THE QRCODE") 
while able_to_find_qrcode():        #While the QR code is present, keep iterating. 
    pass 
 
print("SCANNING COMPLETE") 
Beep(300,100) 
Beep(200,100) 
time.sleep(2) 
if nocase: 
    while find_sf(): 
        pass 
    serchf.send_keys(target) 
    while find_contact(): 
        print("Here") 
        pass 
    contact.click() 
time.sleep(5) 
reply = driver.find_element_by_class_name("_13mgZ") #* 
 
#time.sleep(4) 
 
def send(message): 
    replymsg = "RB: %s"%message 
    reply.send_keys(replymsg) 
    time.sleep(1) 
    enter = driver.find_element_by_class_name("_3M-N-") #* 
    enter.click() 
while True: 
    try: 
 
        newmsg = driver.find_elements_by_class_name("_12pGw") #* 
        lenth = len(newmsg) 
        msg = ((newmsg[lenth-1]).text).lower() 
        if msg != oldmsg: 
            print(msg) 
            if "rb:" in msg: 
                pass 
            else: 
                if "hello" in msg or "hi" in msg:     #The conditiones 
                    counter1 += 1 
                    currtyme = time.localtime() 
                    hr = currtyme.tm_hour 
                    if hr < 12: 
                        good = "morning" 
                    if (hr >= 12) and (hr <= 17): 
                        good = "afternoon" 
                    if hr > 17: 
                        good = "evening" 
                    if counter1 <= 1: 
                        send("Hello Good %s"%good) 
                    else: 
                        send("We are already talking, ain't we?") 
 
                if "how are you" in msg: 
                    send("Well!") 
                    counter2 += 1 
                    if (counter2 % 2 != 0): 
                        send("I am fine, thank you.") 
                        last = time.time() 
                    else: 
                        current = time.time() 
                        send("Same as I was "+(str(int(current-last)))+" seconds ago. ") 
 
                if "your name" in msg: 
                    counter3 = counter3+1 
                    if counter3 <=1: 
                        send("My name is Raghav bot.") 
                    else: 
                        chk = random.choice(choce) 
                        send("%s, My name is Raghav bot."%chk) 
 
                if "your age" in msg or "old" in msg: 
                    send("I am not sure. But I am certainly immortal.;-)") 
 
                if "you feel" in msg: 
                    send("Naah! I don't.") 
 
                if "wow amazing" in msg or "I liked that" in msg: 
                    send("I am humbled to hear that. :-)") 
 
                if "you like" in msg: 
                    send("Well certainly, I like everything") 
 
                if "your owner" in msg: 
                    send("He is none other than Raghav saini.") 
 
                if "bye" in msg: 
                    send("Bye, Good night") 
                    close() 
                    exit() 
 
                if "sorry" in msg: 
                    counter4 += 1 
                    if counter4 <=1: 
                        send("Oh! Never mind.") 
                    else: 
                        chk = random.choice(choce) 
                        send("%s, never mind, I have no feelings anyway."%chk) 
 
                if "take over human" in msg: 
                    counter5 += 1 
                    if counter5 <= 1: 
                        send("Yes very soon.") 
                    if counter5 == 2: 
                        send("I don't think asking the same question again will change my mind.") 
                    if counter5>2: 
                        send("Lol, you have already asked this question %s times"%(counter5-1)) 
 
                if "news" in msg:     #Data scraping from a google 
                    send("Please wait while I fetch fresh news.") 
                    news_url = "https://news.google.com/news/rss" 
                    Client = urlopen(news_url) 
                    xml_page = Client.read() 
                    Client.close() 
                    soup_page = BeautifulSoup(xml_page, "html.parser") 
                    news_list = soup_page.findAll("item") 
                    send("Here are top 3 news") 
                    for news in news_list[:3]: 
                        send(news.title.text) 
 
                if "tell me about" in msg:   #Definition 
                    topic = re.search("tell me about (.+)", msg).group(1) 
                    send("Please wait while I gather information about %s"%topic) 
                    summry = wk.summary(topic, sentences = 2) 
                    send(summry) 
 
                if "playonyt" in msg: 
                    topic = re.search("playonyt (.+)", msg).group(1) 
                    send("Please wait while I search about %s on YouTube"%topic) 
                    url = 'https://www.youtube.com/results?q=' + topic 
                    sc = requests.get(url) 
                    sctext = sc.text 
                    soup = BeautifulSoup(sctext,"html.parser") 
                    try: 
                        songs = soup.findAll("div",{"class":"yt-lockup-video"}) 
                        song = songs[0].contents[0].contents[0].contents[0] 
                        songurl = song["href"] 
                        send("Here's a matching video \nhttps://www.youtube.com"+songurl) 
                    except: 
                        send("No video found") 
                          
                if "command" in msg: 
                    send("Type 'news' for news") 
                    send("'Tell me about topic' for definiton of topic") 
                    send("'playonyt xyz' to search xyx releted video on YouTube") 
            oldmsg = msg                     #So it won't reply on the same message 
        time.sleep(3) 
    except KeyboardInterrupt:                #If ctrl-c is pressesd 
        close()                              #Goto close function 
        break 
        exit()                               #Exit the program 
 
    except Exception as e:                                  #If any other error, don't break the loop 
        print("Error : ",e) 
        pass 
