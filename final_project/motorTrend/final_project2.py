from sentiment import *
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from twitter_util import *

# Sets URL on motortrend.com to reflect the make and model the 
# USER wants to search for.
def set_model_url(make):
	if " " not in make:
		comp = make.lower()
		URL = "http://www.motortrend.com/roadtests/01/" + comp +"/"
		return URL
	else:
		comp = make.replace(" ", "_").lower()
		URL = "http://www.motortrend.com/roadtests/01/" + comp +"/"
		return URL
		

# sets the model the USER wants to search
# input is make, returns model
def set_model(make):
	model = raw_input("Please enter the model " + make + " you want to search: ")
	print(" ")
	return model

# sets the make the USER wants to search
# returns make of car USER inputs
def set_make():
	print(" ")
	make = raw_input("Please enter the brand car you want to search: ")
	return make

def set_model_link(soup, model, URL):
	model = model.lower().replace(" " or "-", "_")
	thing = []
	for link in soup.find_all('a')[:1000]:
		#print("FOR SET MODEL")
		href = link.get('href')
		#print("GET HREF")
		#print(link.get('href'))
		
		
		if (href == None):
			
			x = 2
			while (x <= 5):
				model_URL = (URL + "page" + str(x) +".html")
				model_text = requests.get(model_URL).text
				model_soup = BeautifulSoup(model_text)
				x += 1
				#print("MODEL SOUP")
				#print(model_soup)
				#print(" ")
				#print("MODEL_URL = " + model_URL)
				#print(" ")
				#Go to next page...
				#set_model_link(model_soup, model, URL)
				for link in model_soup.find_all('a')[:1000]:
					href = link.get('href')
					if (href == None):
						#print("BREAK")
						break
					elif (href.find(model)!= -1):
						#print("THING = href")
						#print(href)
						#thing.append(href)
			
						if (href.find("photo_01")!= -1):
							continue
						elif (href.find("video")!= -1):
							continue
						elif (href.find("gallery")!= -1):
							continue
						else:
							thing.append(href)
					elif model not in href:
						#print("IF MODEL NOT IN")
						continue
			#print("BREAK")
			break
		
		elif (href.find(model)!= -1):
			#print("THING = href")
			#print(href)
			
			#thing.append(href)
			
			if (href.find("photo_01")!= -1):
				continue
			elif (href.find("video")!= -1):
				continue
			elif (href.find("gallery")!= -1):
				continue
			else:
				thing.append(href)
			
		
		elif model not in href:
			#print("IF MODEL NOT IN")
			continue
		'''
		elif (href == None):
			#
			print("BREAK")
			break
		'''
	return thing

def get_model_URL(soup, model, URL):
	model_link = set_model_link(soup, model, URL)
	#print("MODEL_LINK")
	#print(model_link)
	return model_link

def get_choices(model_list, model):
	car = model.lower()
	#print("CAR = " + car)
	length = len(model_list)
	#print(length)
	x = 0
	while (x < length):
		choice = model_list[x]
		spot = choice.index(car)
		title = choice[spot:]
		x += 1
		print(str(x) + ": " + title.replace("_", " ").replace("/", ""))

def get_review(analyze):
	#print(analyze)
	review = []
	review_url = analyze
	review_soup = BeautifulSoup(requests.get(review_url).text)
	#for pars in review_soup.find_all('span',  {'class': 'paragraph'}):
	stuff = review_soup.find_all('span',  {'class': 'paragraph'})
		#p = pars.get('text')
	p = '\n'.join([t.text for t in stuff])
	#print(p)
	#review.append(p)
	return p


def get_score(codes, text):
	score_list = []
	if (text != None):
		#print("CHECKING SCORE")
		score = sentiment_score(codes, text, avg_total_words = True, punct = ['.', '?', '!', ',', '-', "'", ';', ':', '/', "\n", "\t", '"'])
		#if (score > 0):
		score = ("{0:.5f}".format(score))
		#score_list.append(score)
		return score
		#else:
			#return score - 1
	else:
		#print("BROKEN")
		return None

def get_msrp(make, model, base_url):
	make = make.replace(" ", "_").lower()
	model = model.lower().replace(" " or "-", "_")
	#price_url = "http://www.truecar.com/prices-new/" + make + "/" + model + "-pricing/"
	price_url = "http://www.kbb.com/cars-for-sale/cars/new-cars/" + make + "/" + model + "/"
	#return price_url
	price_soup = BeautifulSoup(requests.get(price_url).text)
	#stuff = price_soup.find_all('span', {'class': 'amount'})
	stuff = price_soup.find_all('div', {'class': ' section-subtitle'})
	#for p in stuff:
	#	price = p.get('vehicle-price section-subtitle')
	price = '\n'.join([t.float for t in stuff])
	#print("PRICE = " + price)
	return price
	#print(URL)

def plot_points(price_list, score_list):
	scores_prices = []
	scores = score_list
	prices = price_list
	x = 0
	x_axis = []
	y = 0
	y_axis = []
	L = 0
	Z = 0
	while (x < len(scores)):
		x_axis.append(scores[x])
		x += 1
	while (y < len(prices)):
		y_axis.append(prices[y])
		y += 1
	while ( L < len(y_axis)):
		#scores_prices.append([x_axis[L]], [y_axis[L]])
		plt.plot([x_axis[L]], [y_axis[L]], 'ro')
		L += 1
		plt.axis([0, .1, 0, 150000])
		plt.savefig("scores_price_plot.png")
	plt.show()
	return plt