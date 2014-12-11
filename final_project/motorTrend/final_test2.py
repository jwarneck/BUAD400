from bs4 import BeautifulSoup
import requests
from final_project2 import *

n = 10

make = set_make()
model = set_model(make)
base_url = "http://www.motortrend.com"
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

model_list = set(get_model_URL(soup,model, URL))
model_list = list(model_list)

#print(model_list)


#model_list = get_model_URL(soup, model)

#print("MODEL_LIST = ")
#print(model_list)
'''
x = 0
#print("x = " + str(x))
#print("MODEL_LIST_LENGTH = " + str(len(model_list)))
print(model +"_LINK_LIST")
while (x < len(model_list)):
	print(model_list[x])
	x += 1
'''

# iterate through links and pull text to score
print(" ")
print("Please choose an option to calculate: ")
get_choices(model_list)
choice = input()
print(" ")
print("You chose: " + model_list[choice - 1])
print(" ")
link = model_list[choice - 1] 
analyze = base_url + link

review = get_review(analyze)
print(review)