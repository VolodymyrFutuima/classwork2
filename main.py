import requests
import lxml
from bs4 import BeautifulSoup


session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
for j in range(1, 6):
    url = f"https://cash-backer.club/shops?page={j}"
response = session.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.text,"lxml")

all_cashback = soup.find('div', class_="row mt-4")

cashback = all_cashback.find_all('div',class_="col-lg-3 col-md-3 col-12 menu")
for elem in cashback:
    price = elem.find("p", class_="card-text").text
    price = price[price.find(":")+1:price.find("₽")]
    title = elem.find("h3", class_="card-title").text.strip()
    with open("cash-backer.txt", "a", encoding="utf-8") as file:
        file.write(f"{title} ------>>>>\n")
        print(price)







