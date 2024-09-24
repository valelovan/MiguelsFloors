from django.urls import path, include

from . import views

urlpatterns = [
    # English language paths
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("gallery", views.gallery, name="gallery"),
    
    # Spanish language paths
    path("es", views.index_es, name="index-es"),
    path("contact/es", views.contact_es, name="contact-es"),
    path("gallery/es", views.gallery_es, name="gallery-es"),
]