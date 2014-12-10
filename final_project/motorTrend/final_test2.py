from bs4 import BeautifulSoup
import requests
from final_project2 import *

n = 10

make = set_make()
model = set_model(make)

URL = set_model_url(make)

text = requests.get(URL).text
soup = BeautifulSoup(text)

print("Make:  " + make)
print("Model: " + model)
print(" ")
print("URL = " + URL)
print(" ")


'''
for link in soup.find_all('brand_list')
	href = link.get('href')
	print(link.get('href'))
	if href.has_key("make)


# print model link
model_URL = get_model_URL(soup, model)
print("MODEL_URL = " + model_URL)
'''
model_list = []
model_list = get_model_URL(soup,model) 


x = 0
print("x = " + str(x))
print("MODEL_LIST_LENGTH = " + str(len(model_list)))
while (x < len(model_list)):
	print(model_list[x])
	x += 1

'''
for x in range(0, len(model_list)):
	y = 1
	print(model_list[y])
	y +=1
'''

# get_all_news_link(model_URL)