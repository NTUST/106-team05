from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Member


def index(request):
	return render(request, 'polls/index.html', {"alert":""})

def single(request):
	return render(request, 'polls/single.html', {"alert":""})

def about(request):
	return render(request, 'polls/about.html', {"alert":""})	

def contact(request):
	return render(request, 'polls/contact.html', {"alert":""})

def gallery(request):
	return render(request, 'polls/gallery.html', {"alert":""})

def icons(request):
	return render(request, 'polls/icons.html', {"alert":""})

def order(request):
	return render(request, 'polls/order.html', {"alert":""})

def membership(request):
	return render(request, 'polls/membership.html', {"alert":""})

def slot(request):
	return render(request, 'polls/slot.html', {"alert":""})	

def test(request):
	return render(request, 'polls/test.html', {"alert":""})

def typography(request):
	return render(request, 'polls/typography.html', {"alert":""})

def blog(request):
	return render(request, 'polls/blog.html', {"alert":""})

def registered(request):
	return render(request, 'polls/registered.html', {"alert":""})

def add_member(request):   #新增餐廳資料的函式
	c = ""

	account = request.POST['account']  #拿資料（是拿name）
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['password']
	phone = request.POST['phone']
	address = request.POST['address']

	for i in Member.objects.all():
		if account == i.Member_account or password == i.Member_password :
			c = "account or password already be used"

	if c == "":
		m = Member(Member_account = account, Member_name = name, Member_email = email, Member_password = password, Member_phone = phone, Member_address = address)  #新建Restaurant類別
		m.save()  #儲存

	return render(request, 'polls/registered.html', {"alert":c})

def login(request):
	return render(request, 'polls/blog.html', {"alert":""})

def login_check(request):

	c = "account or password have error"
	account = request.POST['account']
	password = request.POST['password']

	for i in Member.objects.all():
		if account == i.Member_account and password == i.Member_password :
			c = ""

	return render(request, 'polls/membership.html', {"alert":c})


