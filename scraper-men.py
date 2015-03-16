from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import os
import gevent

product_urls = []
img_urls = []
counter = 0
wd = webdriver.Chrome()
category_ids = {'Sneakers & Athletic Shoes': 0, 'Boots': 1, 'Oxfords': 2, 'Loafers': 3, 'Sandals': 4, 'Boat Shoes': 5, 'Slippers': 6, 'Clogs & Mules': 7, 'Insoles & Accessories': 8, 'Climbing': 9, 'Heels': 10, 'Flats': 11}

def main():
	os.chdir('./men')
	print "Getting product pages..."
	for i in range (0, 121):
		#url = "http://www.zappos.com/mens-shoes~ov?zfcTest=sis%3A0#!/men-shoes/CK_XAXoC0wSCAQKRFsABAuICAwEYDw.zso?p=" + str(i) + "&s=recentSalesStyle/desc/"
                url = "http://www.zappos.com/mens-shoes~ov#!/men-shoes/CK_XAXoC0wSCAQKRFsABAuICAwEYDw.zso?p=" + str(i) + "&s=recentSalesStyle/desc/"
		text = get_product_page(url)
		get_product_list(text)
	print "Parsing product pages..."
	for url in product_urls:
		product_page = get_page(url)
		parse_product_page(product_page)
	print "Saving images..."
	batch_save_images()

def get_product_page(url):
	global wd
	wd.get(url)
	time.sleep(1)
	return wd.page_source

def get_page(url):
	response = requests.get(url)
	return response.text

def get_product_list(text):
	BS = BeautifulSoup(text)
	for product in BS.find_all("a", class_="product"):
		product_urls.append("http://www.zappos.com" + product.get("href"))

def parse_product_page(text):
	global counter
	BS = BeautifulSoup(text)
	title = BS.title.string.split(' - ')[0].replace("/", "-")
	image_dir = BS.find("a", id="angle-3")
	if image_dir is None:
		return
	img_urls.append("http://www.zappos.com" + image_dir.get("href"))
	brand = BS.find('img', attrs={"itemprop" : "logo"})
	if brand is None:
		brand = BS.find('a', class_="to-brand").string.strip()
	else:
		brand = brand.get('alt')
	#print brand

	color = BS.find('option', selected=True)
	if color is None:
		return
	else:
		color = color.text.strip()
		color = color.replace("EXCLUSIVE! ", '')
	#print color
	price = BS.find('span', class_='price')
	if price is None:
		return
	else:
		price = price.string.strip()
	#print price
	sku = BS.find('span', id='sku')
	if sku is None:
		return
	else:
		sku = sku.string.strip()
	#print sku
	rating = BS.find('span', class_='rating')
	if rating is None:
		rating = '-1'
	else:
		rating = rating.string.strip()
	#print rating + " star(s)"
	category = ""
	breadcrumbs = BS.select("#breadcrumbs > a")
	if breadcrumbs is None:
		return
	for breadcrumb in breadcrumbs:
		category += (breadcrumb.string.strip() + " > ")
	category = category[:-3]
	#print category
	category_id = category_ids[breadcrumbs[1].string.strip()]
	#print category_id
	f = open(str(counter) + ".txt","wb")
	f.write(str(counter) + "\n")
	f.write(title.encode('utf-8') + "\n") # python will convert \n to os.linesep
	f.write(brand.encode('utf-8') + "\n")
	f.write(color.encode('utf-8') + "\n")
	f.write(category.encode('utf-8') + "\n")
	f.write(str(category_id) + "\n")
	f.write(price.encode('utf-8') + "\n")
	f.write(rating.encode('utf-8') + "\n")
	f.write(sku.encode('utf-8') + "\n")
	f.close() # you can omit in most cases as the destructor will call if
	counter += 1

def save_img(url, i):
   	resp = requests.get(url)
   	fout = open(str(i) + ".jpg", "wb")
   	fout.write(resp.content)
   	fout.close()

def batch_save_images():
	threads = [gevent.spawn(save_img, img_urls[i], i) for i in xrange(len(img_urls))]
	gevent.joinall(threads)

main()
