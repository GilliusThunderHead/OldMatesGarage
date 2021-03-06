from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.
def home (request):
	return render (request, 'products/home.html')
	
	


@login_required	
def create (request):
	if request.method=='POST':
		if request.POST['title'] and request.FILES['video']:#request.POST['body'] or request.POST['url'] or request.FILES['icon'] or request.FILES['image'] 
			product=Product()
			product.title=request.POST['title']
			#product.body=request.POST['body']
			#product.url=request.POST['url']
			#if	request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
			#	product.url=request.POST['url']
			#else:
			#	product.url='http://' + request.POST['url']
			#product.icon=request.FILES['icon']
			#odbyproduct.image=request.FILES['image']
			product.video=request.FILES['video']
			product.pub_date=timezone.datetime.now()	
			product.hunter=request.user
			product.save()
			return redirect('/products/' + str(product.id))
		
		else:
			return render (request, 'products/create.html')
	else:
		return render (request, 'products/create.html')
		

@login_required	(login_url="/accounts/signup")
def detail (request,product_id):
	product=get_object_or_404(Product,pk=product_id)
	return render(request, 'products/detail.html',{'product':product})

@login_required(login_url="/accounts/signup")	
def upvote(request, product_id):
	product=get_object_or_404(Product, pk=product_id)
	product.votes_total+=1
	product.save()
	return redirect('/products/' + str(product.id))
	
def videos(request):
	products=Product.objects
	return render (request, 'products/videos.html',{'products': products})
	
	
	
	
	
	
	
	
	
	