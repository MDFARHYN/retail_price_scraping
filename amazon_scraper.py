import requests 
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/Fitbit-Management-Intensity-Tracking-Midnight/dp/B0B5F9SZW7/?_encoding=UTF8&pd_rd_w=raGwi&content-id=amzn1.sym.9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_p=9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_r=A1B0XQ919M066QVE71VN&pd_rd_wg=Aw2vX&pd_rd_r=69a343dc-b5f2-4e2a-ae85-2ca4e3945a26&ref_=pd_hp_d_btf_crs_zg_bs_3375251&th=1"

downlaod_content = requests.get(url).text  #here we are downloading content

soup = BeautifulSoup(downlaod_content,'lxml')  #parse the content using BeautifulSoup

price = soup.find("span",class_="a-price-whole") 

price = price.text

price = price.replace('.','')

price = float(price)

print("price",price)




def send_email():

    email = "your email"

    receiver_email = "receiver_email " #You can also use your email as the receiver email.”

    subject = "price alert"

    message = f"Great news! The price has dropped. The new price is now {price}!"

    text = f"Subject:{subject}nn{message}"




    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login(email,"your app password")

    server.sendmail(email,receiver_email,text)

    print("email sent")

 

 

def check_and_notify():

    if price < 80:  #If the price is less than 80, an email notification will be sent.

        send_email()

        

check_and_notify()
