from django.urls import path, include

from . import views

urlpatterns = [
    # English language paths
    path("", views.index, name="index"),
    path("pricing", views.pricing, name="pricing"),
    
    # Spanish language paths
    path("es", views.index_es, name="index-es"),
]