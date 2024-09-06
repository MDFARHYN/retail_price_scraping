mport requests 
from bs4 import BeautifulSoup
import smtplib
proxies = {
  "https": f"http://PROXY_USERNAME:PROXY_PASS@PROXY_SERVER:PROXY_PORT/"
}
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'content-encoding': 'gzip'
}
url =  "https://www.walmart.com/ip/Men-s-G-Shock-GA100L-8A-Tan-Silicone-Japanese-Quartz-Sport-Watch/166515367?classType=REGULAR"
downlaod_content = requests.get(url, headers=headers, proxies=proxies).text
soup = BeautifulSoup(downlaod_content,'lxml')
price = soup.find("span",{"":"price"}) 
price =  price.text
price = price.replace("Now $","")
price = float(price)
print("price",price)
def send_email():
    email = "your email"
    receiver_email = "receiver_email"
    subject = "Walmart  price alert"
    message = f"Great news! The price has dropped. The new price is now {price}!"
    text = f"Subject:{subject}nn{message}"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,"your app password")
    server.sendmail(email,receiver_email,text)
    print("email sent")
def check_and_notify():
    if price < 80:
        send_email()
        
check_and_notify()
