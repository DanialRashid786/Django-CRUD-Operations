from django.urls import path

from .views import *


urlpatterns = [

    path('', EmployeeRegistrationForm, name="registration"),
    path('registrationlist/', registration_list, name='registration_list'),
    path('delete/<empid>', delete, name='delete'),
    path('update/<id>', update_my_model, name='update'),

]

