# Import necessary modules
from django.shortcuts import render
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# Define your view function
def run_google_form(request):
    # Your Selenium script
    web = webdriver.Chrome()
    web.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")

    sname = 'Sumeet Hareshlal Khatri'
    mynumber = '9511228208'
    memail = 'khatrisumeet400@gmail.com'
    myaddress = 'opp bk. no. 997, nr. Dasera maidan, section -23, Ulhasnagar'
    npincode = '421003'
    mydob = '02-04-2000'
    mygender = 'male'
    mtext = 'GNFPYC'

    # Find elements and fill the form
    name = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    number = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    mail = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    pincode = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    dob = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    gender = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    mtext_field = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')

    name.send_keys(sname)
    number.send_keys(mynumber)
    mail.send_keys(memail)
    address.send_keys(myaddress)
    pincode.send_keys(npincode)
    dob.send_keys(mydob)
    gender.send_keys(mygender)
    mtext_field.send_keys(mtext)

    # Submit the form
    submit_button = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    time.sleep(10)

    # Optionally, take a screenshot
    web.save_screenshot("image.png")
    web.quit()

    # Return a response or render a template as needed
    return render(request, 'result_template.html')
