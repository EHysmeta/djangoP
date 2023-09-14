from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home_page"),
    path('about/',views.about, name="about_page"),
    path("itemdetail/<id>/", views.itemdetail, name="detail"),
    path("category/<id>/", views.Category, name="category"),
    path("contacts/", views.contact, name="contacts")
]