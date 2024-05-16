from selenium import webdriver
import time
import pandas as pd
import os
import streamlit as st

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

st.set_page_config(layout="wide")
st.title('LinkedIn Job Scraper')
url1=st.text_input('Enter url')

if url1:
    driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(url1)
    title =driver.title
    print(title)
    y=driver.find_elements(By.CLASS_NAME, 'results-context-header__job-count')[0].text
    y= ''.join(filter(str.isdigit, y))
    n=int(y)
    st.write(f"Page Title: {title}")

    companyname= []
    titlename= []

    try:
        for i in range(n):
            company=driver.find_elements(By.CLASS_NAME, 'base-search-card__subtitle')[i].text
            companyname.append(company)
        
    except IndexError:
        print("no")

    len(companyname)
    try:
        for i in range(n):
            title=driver.find_elements(By.CLASS_NAME, 'base-search-card__title')[i].text
            titlename.append(title)
            
    except IndexError:
        print("no")

    companyfinal=pd.DataFrame(companyname,columns=["company name"])
    titlefinal=pd.DataFrame(titlename,columns=["title"])

    x = companyfinal.join(titlefinal)
    df = pd.DataFrame(x)

    # Display the DataFrame with a specific width
    st.dataframe(df, width=1000)
    # Close the browser
    driver.quit()














# i = 2
# while i <= int((n+200)/25)+1: 
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     i = i + 1
    
#     try:
#         send=driver.find_element_by_xpath("//button[@aria-label='Load more results']")
#         driver.execute_script("arguments[0].click();", send)   
#         time.sleep(3)
                                                
            
#     except:
#         pass
#         time.sleep(5)
