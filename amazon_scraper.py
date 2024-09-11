import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import os
from datetime import datetime

# Proxy and headers configuration for avoid blocking
proxies = {
    "https": "http://PROXY_USERNAME:PROXY_PASS@PROXY_SERVER:PROXY_PORT/"
}

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'content-encoding': 'gzip'
}

url = "https://www.amazon.com/Fitbit-Management-Intensity-Tracking-Midnight/dp/B0B5F9SZW7/?_encoding=UTF8&pd_rd_w=raGwi&content-id=amzn1.sym.9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_p=9929d3ab-edb7-4ef5-a232-26d90f828fa5&pf_rd_r=A1B0XQ919M066QVE71VN&pd_rd_wg=Aw2vX&pd_rd_r=69a343dc-b5f2-4e2a-ae85-2ca4e3945a26&ref_=pd_hp_d_btf_crs_zg_bs_3375251&th=1"

# Scraping the price from the webpage
download_content = requests.get(url,proxies=proxies,headers=headers).text #downloading the html using python request and also using proxy for avoid blocking
soup = BeautifulSoup(download_content, 'lxml') #parsing the HTML content using BeautifulSoup
price = soup.find("span", class_="a-price-whole")  #using soup.find method for target price


# Cleaning and converting the price
price = price.text.strip().replace('.', '')
price = float(price)

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# File name for the CSV file
file_name = 'price_data.csv'

# Function to save price data to CSV
def save_to_csv(url, price):
    file_exists = os.path.isfile(file_name)
    
    with open(file_name, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'URL', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if the file does not exist
        if not file_exists:
            writer.writeheader()

        # Write data row
        writer.writerow({'Date': current_date, 'URL': url, 'Price': price})

    print(f"Data saved to {file_name}")

# Function to send an email alert
def send_email():
    email = "your email"
    receiver_email = "receiver_email"
    subject = "Amazon Price Alert"
    message = f"Great news! The price has dropped. The new price is now {price}!"
    text = f"Subject:{subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "your app password")
    server.sendmail(email, receiver_email, text)
    server.quit()
    print("Email sent!")

# Function to check price and notify if needed
def check_and_notify():
    if price < 80:  # Threshold price for notification
        send_email()

# Save the scraped data to CSV
save_to_csv(url, price)

 
