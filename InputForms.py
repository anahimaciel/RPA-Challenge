import pandas as pd
from playwright.sync_api import sync_playwright 

df=pd.DataFrame(pd.read_excel("challenge.xlsx"))

cols=df.columns

names={cols[0]:"labelFirstName",cols[1]:"labelLastName",cols[2]:"labelCompanyName",
       cols[3]:"labelRole",cols[4]:"labelAddress",cols[5]:"labelEmail",cols[6]:"labelPhone"}

with sync_playwright() as p:
    browser= p.chromium.launch()
    p.selectors.set_test_id_attribute("ng-reflect-name")

    page=browser.new_page()
    page.goto("https://rpachallenge.com/")
    
    page.get_by_role('button',name='Start').click()
    for i in range(len(df)):
        for col in cols:
            page.get_by_test_id(names[col]).fill(str(df[col][i]))   
        #page.screenshot(path=f"{i}.png")
        page.get_by_role('button',name='Submit').click()
    page.screenshot(path="f.png")
    browser.close()