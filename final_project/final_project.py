# Sets URL on carbuzz.com to reflect the make and model the 
# USER wants to search for.
def set_model_url(make):
	URL = "http://www.carbuzz.com/" + make +"/"
	return URL

# sets the model the USER wants to search
# input is make, returns model
def set_model(make):
	model = raw_input("Please enter the model " + make + " you want to search:")
	return model

# sets the make the USER wants to search
# returns make of car USER inputs
def set_make():
	make = raw_input("Please enter the brand car you want to search:")
	return make

def set_model_link(soup, model):
	for link in soup.find_all('a')[:500]:
		#print("FOR SET MODEL")
		href = link.get('href')
		#print("GET HREF")
		#print(link.get('href'))
		if model not in href:
			#print("IF MODEL NOT IN")
			continue
		else:
			#print("THING = href")
			thing = href
		return thing

def get_model_URL(soup, model):
	model_link = set_model_link(soup, model)
	#print("MODEL_LINK")
	#print(model_link)
	return model_link