from pydoc import classname
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())

# Item URL 
driver.get("https://www.urbanoutfitters.com/shop/fujifilm-instax-mini-11-instant-camera?category=SEARCHRESULTS&color=010&searchparams=q%3Dfujifilm%2520instax%26sayt%3Dtrue&type=REGULAR&size=ONE%20SIZE&quantity=1")

# Set up telegram
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


api_id = '17066558'
api_hash = '29c73df652abe6842ef793b79c0c6e68'
token = "5025038632:AAEFtLwtldy3-Dalx8pzcVVI7Jo8jEy7IvM"
phone = "+16174078162"

client = TelegramClient('session', api_id,api_hash)

client.connect()

if not client.is_user_authorized():
  
    client.send_code_request(phone)
     
    # signing in the client
    client.sign_in(phone, input('Enter the code: '))
import time

while True:
    driver.refresh()
    #check Available?
    elem = driver.find_element_by_css_selector(".c-pwa-message__text")
    available = elem.text
    
    if available.find("not available") != -1:
        pass
    else:
        try:
            receiver = InputPeerUser(1465890629, 0)
        
            client.send_message(receiver, available, parse_mode='html')
        except Exception as e:
            print(e)
    time.sleep(300)
  
# disconnecting the telegram session
client.disconnect()
