from django.urls import path, include

from . import views

urlpatterns = [
    # English language paths
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    
    # Spanish language paths
    path("es", views.index_es, name="index-es"),
    path("contact/es", views.contact_es, name="contact-es"),
]