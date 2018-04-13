from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import businessCard as bizcard
from .forms import businessCardForm
from django.shortcuts import render




def home(request):
    template_name = 'homepage/porfolio.html'
    print("test")
    if request.method == 'POST':
        form = businessCardForm(data=request.POST)
        if form.is_valid():
            email= request.POST.get("email")
            print("test3")
            name = form.cleaned_data['contact_name']
            biz_name = form.cleaned_data['company']
            phone_number = form.cleaned_data['phone_number']
            message  = form.cleaned_data['message']

            biz = bizcard(email= email ,contact_name = name, company = biz_name,phone_number = phone_number,message = message )

            biz.save()

    return render(request,template_name)

