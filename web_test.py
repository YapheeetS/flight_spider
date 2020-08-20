import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from playsound import playsound

chrome_path = r'/usr/local/bin/chromedriver'  # path from 'which chromedriver'
search_dates = ["2020-08-19", "2020-08-22","2020-08-26", "2020-08-29", "2020-09-02", "2020-09-05"]
time_out_seconds = 10

url = 'https://www.google.com/flights?lite=0#flt=SFO.PVG.2020-08-19.SFOPVG0UA857;c:USD;e:1;so:7;sd:1;t:b;tt:o;sp:2.USD.153510'

flag = 1
while flag:
    for date in search_dates:
        my_url = url.replace("2020-08-19", date)
        print('date: ', date)
        print('url: ', my_url)

        driver = webdriver.Chrome(executable_path=chrome_path)
        driver.get(my_url)

        time.sleep(time_out_seconds)  # Let the user actually see something!
        error_message = driver.find_elements_by_class_name("gws-flights-results__error-message")
        if len(error_message) > 0:
            print("error")
            driver.quit()
            time.sleep(5)
            continue
        else:
            print("Find UA857!")
            flag = 0
            driver.quit()
            break

playsound('ring.mp3')


