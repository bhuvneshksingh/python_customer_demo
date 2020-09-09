from django.urls import path
from . import views


urlpatterns = [
    
    # ------------------Customer API Urls-----------------------
	path('customers/list/', views.CustomerListView, name="CustomerListView"),
	path('customer/detail/<str:id>', views.CustomerDetailView, name="CustomerDetailView"),
	path('customer/create/', views.CustomerCreateView, name="CustomerCreateView"),
	path('customer/update/<str:id>', views.CustomerUpdateView, name="CustomerUpdateView"),
	path('customer/delete/<str:id>', views.CustomerDeleteView, name="CustomerDeleteView"),
	
]