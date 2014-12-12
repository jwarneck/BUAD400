import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

'''
make = "audi"
model= "a3"

price_url = "http://www.kbb.com/cars-for-sale/cars/new-cars/" + make + "/" + model + "/"
print(price_url)
soup = BeautifulSoup(requests.get(price_url).text)
spans = soup.find_all('div', {'class': 'vehicle-price_section-subtitle'})
text = '\n'.join([t.text for t in spans])
print(text)
print(spans)
'''

plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()