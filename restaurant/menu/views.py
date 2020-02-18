from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import json
from .models import menu_item

def index(request):
	data=menu_item.objects.all()
	return render(request,'menu/index.html',{'menu_items':data})
	# return render(request,'menu/index.html')

def storeDetails(request):
	if request.method == 'POST':
		data=json.loads(request.body.decode("utf-8"))
		for item in data['menu_items']:
			menu_item.objects.create(	description=item['description'],	
										image_present=item['image_present'],	
										large_portion_name=item['large_portion_name'],	
										name=item['name'],	
										price_large=item['price_large'],	
										price_small=item['price_small'],	
										short_name=item['short_name'],	
										small_portion_name=item['small_portion_name'])

	return render(request,'menu/index.html',{'menu_items':data})