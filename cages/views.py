from django.shortcuts import  render, get_object_or_404
from django.shortcuts import  render_to_response
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from .forms import UserForm, CustomerForm, AddressForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import formats
from reportlab.pdfgen import canvas

from .models import BbrCustomer, BbrAddress, BbrRentalagreement

# Create your views here.
def index(request):
	if request.method == 'POST':
		date = request.POST.get('date_to')
		request.session['date'] = date
		return render(request, 'cages/index.html', { 'obj': BbrRentalagreement.objects.filter(startdate__date = request.POST.get('date_to') ), 'selectedDate': date } )
	else:
		dt=datetime.today()
		fromdate = datetime.strftime(dt, '%Y-%m-%d')
		request.session['date'] = fromdate
		return render(request, 'cages/index.html', { 'obj': BbrRentalagreement.objects.filter(startdate__date = datetime.today()), 'currentDate': fromdate } )


def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			registered = True

		else:
			print user_form.errors

	else:
		user_form = UserForm()

	return render(request,
		'cages/register.html',
		{'user_form': user_form, 'registered': registered}, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/cages/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username,password)
			return HttpResponse("Invalid login details supplied")
	else:
		return render(request, 'cages/login.html', {}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/cages/')

@login_required
def customer(request):
	
	return render_to_response('cages/customer.html', { 'obj': BbrCustomer.objects.order_by('custid')})

def detail(request, custid):
	customer = get_object_or_404(BbrCustomer, pk=custid)
	return render(request, 'cages/detail.html', { 'customer': BbrCustomer })


@login_required
def add(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		customer_form = CustomerForm(data=request.POST)
		address_form = AddressForm(data=request.POST)

		if customer_form.is_valid() and address_form.is_valid():
			address = address_form.save()
			address.save()

			customer = customer_form.save(commit=False)
			customer.addressid = BbrAddress.objects.last()
			customer.save()

			registered = True

		else:
			print customer_form.errors, address_form.errors

	else:
		customer_form = CustomerForm()
		address_form = AddressForm()

	return render(request,
		'cages/add.html',
		{'customer_form': customer_form, 'address_form': address_form, 'registered': registered }, context)


@login_required
def report(request):
	date = request.session['date']
	return render(request, 'cages/report.html', {"date": date, 
	'obj': BbrRentalagreement.objects.filter(startdate__date = date ) } )
