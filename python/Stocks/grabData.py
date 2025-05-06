import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import re
import time
import os

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/76.0.3809.6261048 Safari/537.36'}

urls=["https://www.boerse.de/aktien/Allianz-Aktie/DE0008404005",
      "https://www.boerse.de/aktien/ASML-Holding-Aktie/NL0010273215",
      "https://www.boerse.de/aktien/Alphabet-C-Aktie/US02079K1079",
      "https://www.boerse.de/aktien/Amazon-Aktie/US0231351067",
      "https://www.boerse.de/aktien/Apple-Aktie/US0378331005",
      "https://www.boerse.de/aktien/CyberArk-Software-Aktie/IL0011334468"

      ]


# Use Beautiful Soup to parse the HTML

stockdata=[]

for url in urls:
    response = requests.get(url,headers=headers)
    try:

        print (url, response)
        soup = BeautifulSoup(response.content, "html.parser")
        price = soup.find('div', class_="nobr marginlessHeadline").get_text(separator="",strip=True)
        print(price)
        if soup.find('div', class_="name nameMittel"):
            company = soup.find('div', class_="name nameMittel").h1.text
        else:
            company = soup.find('div', class_="name nameGross").h1.text
        company_isin = soup.find_all('td', class_="tooldata2")[1].text
        current_dateTime = date.today().isoformat()
        change = soup.find_all('div', class_="nobr marginlessHeadline")[2].span.span.text
        # volume=soup.find('table', class_="tb10Table borderPrimary width100 usp100NoBorder usp100Table").find_all("td")[2].text
        #volume = soup.find_all('td', class_="col l3 bodyLargeHeavy")[2].text
        stockvalues = [current_dateTime,company,company_isin,price,change]
        stockdata.append(stockvalues)


    except AttributeError:
        print("Change the Element id")
        # Wait for a short time to avoid rate limiting
    time.sleep(5)

column_names = ["Date", "Company","ISIN","Price", "Change"]
df = pd.DataFrame(columns = column_names)
df['Change'] = df['Change'].str.replace('%', '').str.replace(',', '.').astype(float)
for i in stockdata:
  index=0
  df.loc[index] = i
  df.index = df.index + 1
df=df.reset_index(drop=True)
df.to_csv("StockInputData.csv", mode='a', header=not os.path.exists("StockInputData.csv"))
#print(df)
