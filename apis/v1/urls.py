from django.urls import path
from apis.v1 import views

urlpatterns = [
    path("get_details", views.get_details),
    path("add_details", views.add_details),
    path("edit_details", views.edit_details),
    path("put_details", views.put_details),
    path('delete_details',views.delete_details)

]
