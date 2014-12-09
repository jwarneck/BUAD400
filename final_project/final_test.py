from bs4 import BeautifulSoup
import requests
from final_project import *

n = 10

make = set_make()
model = set_model(make)

URL = set_model_url(make)

text = requests.get(URL).text
soup = BeautifulSoup(text)

print("URL = " + URL)
print("Make:  " + make)
print("Model: " + model)

print(" ")


'''
for link in soup.find_all('brand_list')
	href = link.get('href')
	print(link.get('href'))
	if href.has_key("make)
'''
# print model link
model_URL = get_model_URL(soup, model)
print("MODEL_URL = " + model_URL)