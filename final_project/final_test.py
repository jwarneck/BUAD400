from bs4 import BeautifulSoup
import requests
from final_project import *

n = 10

make = set_make()
model = set_model(make)

URL = set_make_url(make)

print("URL = " + URL)
print("Make: " + make +" Model: " + model)

