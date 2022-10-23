from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_qr_codes, name='all_codes'),
    path('details/<int:id>/', views.img_detail_view, name='details'),
]