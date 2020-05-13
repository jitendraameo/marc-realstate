from django.shortcuts import render
from django.http import request
from .models import *
from django.db.models import Q

def home(request):
  
    return render(request, 'buyer/index.html', {'cities': City.objects.all(), 'areas':Area.objects.all()})   


def advance_search(request):
    return render(request, 'buyer/advance-search.html')  


def foreclosure_search(request):
    return render(request, 'buyer/foreclosure.html')  


def blog_search(request):
    return render(request, 'buyer/blog.html')  


def about_view(request):
    return render(request, 'buyer/aboutus.html')  
        

def contact_view(request):
    return render(request, 'buyer/contact.html')


def market_view(request):
    return render(request, 'buyer/advance-search.html')

def property_search_view(request):
    # try:
		city = request.GET['CityChoice']
		area = request.GET['AreaChoice']
		lowprice = request.GET['LimitFrom']
		upprice = request.GET['LimitTo']

		if city and area and lowprice and upprice:
			property_list = Property.objects.filter((Q(city__exact=city) and Q(area__exact=area))).filter(Q(price__range=(lowprice, upprice)))
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city and area and lowprice:
			property_list = Property.objects.filter((Q(city__exact=city) and Q(area__exact=area))).filter(Q(price__gte=lowprice))
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city and area and upprice:
			property_list = Property.objects.filter((Q(city__exact=city) and Q(area__exact=area))).filter(Q(price__lte=upprice))
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city and area:
			property_list = Property.objects.filter(Q(city__exact=city) and Q(area__exact=area))
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city and lowprice:
			property_list = Property.objects.filter(city__name__exact=city).filter(price__gte=lowprice)
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city and upprice:
			property_list = Property.objects.filter(city__name__exact=city).filter(price__lte=upprice)
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif city:
			property_list = Property.objects.filter(city__name__contains=city)
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif lowprice and upprice:
			property_list = Property.objects.filter(Q(price__range=(lowprice, upprice)))
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif lowprice:
			property_list = Property.objects.filter(price__gte=lowprice)
			return render(request, 'buyer/property2.html', {'properties': property_list})
		elif upprice:
			property_list = Property.objects.filter(price__lte=upprice)
			return render(request, 'buyer/property2.html', {'properties': property_list})
		else:
			return render(request, 'buyer/property2.html', {'properties': Property.objects.all()})

    


