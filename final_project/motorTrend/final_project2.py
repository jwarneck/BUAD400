from bs4 import BeautifulSoup
import requests

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
	make = raw_input("Please enter the brand car you want to search: ")
	return make

def set_model_link(soup, model):
	model = model.lower()
	for link in soup.find_all('a')[:1000]:
		#print("FOR SET MODEL")
		href = link.get('href')
		#print("GET HREF")
		#print(link.get('href'))
		
		
		if (href == None):
			#
			print("BREAK")
			break
		
		elif (href.find(model)!= -1):
			print("THING = href")
			thing = []
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

def get_model_URL(soup, model):
	model_link = set_model_link(soup, model)
	#print("MODEL_LINK")
	#print(model_link)
	return model_link
'''
def get_all_news_link(model_URL):
	model_text = requests.get(model_URL).text
	model_soup = BeautifulSoup(model_text)
	thing_URL = model_URL[:-1] + "_news/"
	print("THING URL = " +thing_URL)
	#for link in model_soup.find_all('a')[:500]:
'''	