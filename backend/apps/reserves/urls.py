from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('reserves/', views.reserve_list_create, name='reserves'),
    path('reserves/<int:pk>/', views.reserve_detail_update_delete, name='reserve_detail'),
    path('reserve-period/', views.reserve_period_list_create, name='reserve_period'),
    path('checkout/', views.checkout, name='checkout'),
    path('payments/', views.payment, name='payments'),
]

router = SimpleRouter()

router.register("lots", views.LotModelViewSet, basename="lots") 
router.register("fares", views.FareModelViewSet, basename="fares") 
router.register("fares-period", views.FarePeriodModelViewSet, basename="fares_period") 
router.register("clients", views.ClientModelViewSet, basename="clients") 

urlpatterns += router.urls

