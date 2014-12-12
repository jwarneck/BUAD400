from bs4 import BeautifulSoup
import requests
import sys
from final_project2 import *
from sentiment import *
codes = get_sentiment_codes("/Users/Administrator/Documents/GitHub/BUAD400/final_project/motorTrend/AFINN-111.txt")

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

choice = -1
# iterate through links and pull text to score
print(" ")
list = get_choices(model_list, model)
print(" ")
print("Please choose an option to calculate: ")
choice = input()

print(" ")
#print("You chose: " + model_list[choice - 1])
#print(" ")
link = model_list[choice - 1] 
analyze = base_url + link

text = get_review(analyze)
#text = str(text)
#print(text)

#calculate a sentiment score for the review
score = get_score(codes, text)
	#print("SCORE = " + str(score))
score_list = []
score_list.append(score)
print("SCORES = ")
r = 0
while (r < len(score_list)):
	print(score_list[r])
	r += 1
score_list.append(1.2)
#get MSRP
price = get_msrp(make, model, base_url)
#print("PRICE URL= " + price)
print(" ")
print("Price = " + price)
#price_list = [32000, 25000]
price_list = []
price_list.append(price)
price_list.append(25000)

print(score_list)
print(price_list)

'''
#plot price and sent. score on graph
print(" ")
print("Plotting")
PLOT = plot_points(price_list, score_list)
print(PLOT)
'''