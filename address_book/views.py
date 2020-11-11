from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages 
# Create your views here.


def home(request):
	address = Address.objects.all()



	return render (request, 'home.html',{'address':address})



def add_address(request):
	if request.method == "POST":
		form = AddressForm(request.POST or none)
		if form.is_valid():
			form.save()
			messages.success(request,("itme has been added to the list "))
			return redirect('home')

		else:
			context = {'form':form}
			messages.success(request,("error form is not valid  "))
			return render (request , 'add_address.html', context)


	form = AddressForm()

	return render (request, 'add_address.html',{'form':form})





def delete(request,list_id):
	item = Address.objects.get(pk= list_id)
	item.delete()
	messages.success(request,("item has been deleted "))
	return redirect('home')



def edit_address(request,list_id):
	#item = Address.objects.get(pk= list_id)
	if request.method == "POST":
		item = Address.objects.get(pk= list_id)
		form = AddressForm(request.POST, instance = item)
		if form.is_valid():
			form.save()
			messages.success(request,("itme has been EDITEDDD  "))
			return redirect('home')
		else:
			item = Address.objects.get(pk= list_id)
			messages.success(request,("edit form is not valid "))
			return render (request , 'edit_address.html', {'item':item})

	else:
		item = Address.objects.get(pk= list_id)
		form = AddressForm(instance = item)
		return render (request, 'edit_address.html',{'item':item})