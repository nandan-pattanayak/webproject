from django.shortcuts import render
from django.http import HttpResponse
from .import models
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup
BASE_URL='https://delhi.craigslist.org/search/bbb?query={}'
BASE_IMAGE_URL="https://images.craigslist.org/{}_300x300.jpg"


# Create your views here.
def home(request):
	return render(request,"home.html")
def new_search(request):
	search=request.POST['text1']
	models.Record.objects.create(search=search)
	final_url=BASE_URL.format(quote_plus(search))
	respose=requests.get(final_url)
	data=respose.text
	soup=BeautifulSoup(data,features='html.parser')
	post_listings=soup.find_all('li',{'class':'result-row'})
	final_postings=[]
	for post in post_listings:
		post_title=post.find(class_='result-title').text
		print(post_title)
		post_url=post.find('a').get('href')
		print(post_url)
		if post.find(class_='result-image').get('data-ids'):
			post_image_url=post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
			post_image_url=BASE_IMAGE_URL.format(post_image_url)
			print(post_image_url)
		else:
			post_image_url="https://images.unsplash.com/photo-1516541196182-6bdb0516ed27?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"
		if post.find(class_='result-price'):
			post_price=post.find(class_='result-price').text
		else:
			post_price='N-A'
		final_postings.append((post_title,post_url,post_image_url,post_price))


	records={'data':search,'final_postings':final_postings}
	return render(request,'result.html',records)

