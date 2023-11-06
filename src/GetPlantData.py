import pandas as pd
from selenium import webdriver
import time

file_path = 'input\\USRIISv2_MasterList - All Invasive Plants - Filtered.xlsx'

df = pd.read_excel(file_path)
driver = webdriver.Chrome()
result = pd.DataFrame(columns=df.columns)

for index, row in df.iterrows():
    driver.get(row['WebLink'])
    time.sleep(10)
    page_source = driver.page_source
    if page_source.find("CharacteristicsTab") != -1:
        result.loc[len(result )] = row

result.to_excel("output\\result.xlsx", index=False)
driver.quit()
