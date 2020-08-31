from django.conf.urls import url
from . import views
namespace='contact'

urlpatterns =[
    url(r'^$', views.contact, name='contact'),
    
    ]
#handler404 = 'enquiry.views.handler404'