import requests
import schedule
import time
import json
from plyer import notification
from bs4 import BeautifulSoup


# Function for requesting data from url
def request_data(url):
    r=requests.get(url).text
    return r

# Function for getting notification
def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\Chittoria\\PycharmProjects\\Python Project\\cimg2.ico",        #The Icon which you want to appear on the notification
        timeout=10
    )
def notifier():
    while True:
        # notifyMe("COVID-19 UPDATES","Let's fight with this virus together.")
        myData = request_data("https://www.mohfw.gov.in/")          #This is the website link from where the data is being fetched.

        soup = BeautifulSoup(myData, 'html.parser')                 #Using Beautiful Soup, web scraping is being done.
        soup.prettify()
        myStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myStr += tr.get_text()

        myStr = myStr[1:]
        itemlist = myStr.split("\n\n")
        state_list = ["Rajasthan", "Delhi", "Punjab", "Maharashtra", "Uttar Pradesh"]           #You can select whatever cities you want
        for item in itemlist[0:35]:
            datalist = item.split('\n')
            # print(datalist)
            if datalist[1] in state_list:
                print(datalist)
                title = "Cases of COVID-19"
                message = f"STATE: {datalist[1]}\nActive Cases: {datalist[2]}\nCured: {datalist[3]}    Deaths: {datalist[4]}\nTotal Confirmed Cases: {datalist[5]}"
                notifyMe(title, message)
                time.sleep(12)

        time.sleep(15 * 60)                     #It will run after every 15 minutes.
if __name__ == '__main__':
    notifier()





