from django.shortcuts import render, HttpResponse
from . models import Contact
from django.http import JsonResponse

def contact(request):
    if request.method == 'POST':
    	name=request.POST.get('name')
    	email=request.POST.get('email')
    	subject=request.POST.get('subject')
    	newcontact = Contact(name=name,email=email,subject=subject)
    	newcontact.save()
    	data = {'name':name, 'email':email, 'subject':subject }
    	print(data)
    	return JsonResponse(data, safe=False)
        
        #return render(request, 'success.html', {})
        
    else:
        #return render(request, 'workingcontat.html', {})
        return render(request, 'contact/contactform.html', {})
#data = {'name':name, 'email':email, 'subject':subject }