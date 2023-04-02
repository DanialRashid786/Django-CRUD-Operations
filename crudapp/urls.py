from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

    path('', EmployeeRegistrationForm, name="registration"),
    path('registrations/', registration_list, name='registration_list'),
    path('delete/<empid>', delete, name='delete'),
    path('update/<id>', update_my_model, name='update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)