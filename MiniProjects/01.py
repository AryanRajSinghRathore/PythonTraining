from bs4 import BeautifulSoup as bs
import requests
link ='https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-blue-tide-128-gb/product-reviews/itm7acae55b999e6?pid=MOBGHHXQCZQVEQDG&lid=LSTMOBGHHXQCZQVEQDGNPTZOJ&marketplace=FLIPKART'

page = requests.get(link)
#print(page)

#print(page.content)
soup = bs(page.content,'html.parser')
#print(soup)

#print(soup.prettify())
review = soup.find_all('div',class_ ='row')
#print(rating)


all_review =[]
for i in range(len(review)):
    all_review.append(review[i].get_text())
print(all_review)
