import requests
from bs4 import BeautifulSoup
import mail
import time

URL = "https://www.amazon.es/Hercules-DJControl-Inpulse-300-MK2/dp/B0B9LBVDVV/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1UEDN356HR344&keywords=dj+control+inpulse+300+mk2&qid=1706830231&sprefix=dj+control+inpulse+00+mk2%2Caps%2C118&sr=8-1&ufe=app_do%3Aamzn1.fos.5e544547-1f8e-4072-8c08-ed563e39fc7d"
HEADER = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}

def getprice():
    page = requests.get(URL, headers = HEADER)
    soup = BeautifulSoup(page.content, "lxml")
    price = soup.find(id="style_name_1_price").get_text()
    price = price.replace(",", ".")
    price = price[2:-4]
    return price

def readFile():
    f = open("price.txt", "r")
    if f.mode == "r":
        content = f.read()
    f.close()
    return content
    
def writeFile(number):
    f = open("price.txt", "w")
    if f.mode == "w":
        f.write(number)
    f.close()
    
def main():
    try:
        open("price.txt")
    except FileNotFoundError:
        writeFile(getprice())

    i = 0
    while(True):
        oldprice = readFile()
        newprice = getprice()
        if i == 2:
            newprice = 50
        if float(newprice) < float(oldprice):
            message = f"Su producto ha sido rebajado a {newprice} euros, cómpralo cabronazo \n URL: {URL}"
            mail.sendemail(message)
            writeFile(newprice)
            print("Mensaje mandado \n")
        
        i += 1
        time.sleep(5)

if __name__ == "__main__":
    main()
