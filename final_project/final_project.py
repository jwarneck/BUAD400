# Sets URL on carbuzz.com to reflect the make the USER wants
# to search for.
def set_make_url(make):
	URL = "http://www.carbuzz.com/" + make +"/"
	return URL

def set_model(make):
	model = input("Please enter the model " + make + " you want to search:")
	return model

def set_make():
	make = input("Please enter the brand car you want to search: \n")
	return make