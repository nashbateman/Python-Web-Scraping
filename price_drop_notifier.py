import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Xiaomi-Electric-Long-range-Fold-n-Carry-Ultra-Lightweight/dp/B076KKX4BC/ref=sr_1_3?crid=13SMYVXZGOHGQ&dchild=1&keywords=electric+scooter+for+adults&qid=1588051328&sprefix=electric+scooter%2Caps%2C229&sr=8-3'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def check_price():
    
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    print(converted_price)
    print(title.strip())
    if(converted_price < 380):
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
  
    server.login('nashbateman@gmail.com', 'sgeixgqkdhtepmif')
    subject = 'Price drop notification'
    body = 'The electric scooter has dropped in price. Check the amazon link! https://www.amazon.com/Xiaomi-Electric-Long-range-Fold-n-Carry-Ultra-Lightweight/dp/B076KKX4BC/ref=sr_1_3?crid=13SMYVXZGOHGQ&dchild=1&keywords=electric+scooter+for+adults&qid=1588051328&sprefix=electric+scooter%2Caps%2C229&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'nashbateman@gmail.com',
        'nashbateman@gmail.com',
        msg
    )
    
    print('Email notification has been sent')

    server.quit()
    
check_price()
