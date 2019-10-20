#import the required libraries
import requests
from bs4 import BeautifulSoup
import smtplib
#paste the link of a product
url='https://www.amazon.in/FX505GE-15-6-inch-Graphics-i7-8750H-FX505GE-BQ030T/dp/B07KPWK27P?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_Cj0KCQjw84XtBRDWARIsAAU1aM0_O3mak1crh1UUywT5iQW6waU88YF1bEWeAbGxgE43CuuBweQxTlQaAiZNEALw_wcB_k_&gclid=Cj0KCQjw84XtBRDWARIsAAU1aM0_O3mak1crh1UUywT5iQW6waU88YF1bEWeAbGxgE43CuuBweQxTlQaAiZNEALw_wcB'
#install gecko drivers
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

#initialize the variables
page=requests.get(url,headers=headers)
soup=BeautifulSoup(page.content,'html.parser')
#for getting the name of product
title=soup.find(id="productTitle").get_text()
#for getting price of product
price=soup.find(id="priceblock_ourprice").get_text()
pc=(price[0:10])
print(pc)
n=''
for i in pc:
    if i==".":
        break
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        n=n+i
pc=int(n)
#for sending email
if pc<20000:
    send_email()
def send_email():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('aditya28071999@gmail.com','imcadeejdrsvufmy')
    subject="Price fell down"
    body=" check price"
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail("aditya28071999@gmail.com","pandit28071999@gmail.com",msg)
    print("email sent")
    server.quit()

    
print(title.strip())

