import requests
import lxml
from bs4 import BeautifulSoup

url = "https://kups.club/"

session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

response = session.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.text,"lxml")

all_product = soup.find('div', class_="row mt-4")
print(len(all_product))
print(all_product.text)

products = all_product.find_all('div',class_="col-lg-4 col-md-4 col-sm-6 portfolio-item ")


