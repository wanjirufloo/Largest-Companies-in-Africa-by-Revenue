from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_Africa_by_revenue'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text,'html')

print(page.status_code)

print(soup)

table = soup.find_all('table')[1]

print(table)

 africa_titles = table.find_all('th')

africa_titles

africa_table_titles = [titles.text.strip() for titles in africa_titles]
print(africa_table_titles)

import pandas as pd

df = pd.DataFrame(columns =africa_table_titles)
df

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length]= individual_row_data
    

df

df.to_csv(r'C:\Users\Flo\Desktop\Webscraping\Companies.csv',index = False)

