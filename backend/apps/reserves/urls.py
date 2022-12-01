from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

urlpatterns = [
    path('reserves/', views.reserve_list_create, name='reserves'),
    path('reserves/<int:pk>/', views.reserve_detail_update_delete, name='reserve_detail'),
    path('reserve-pagination/', views.ReservePagination.as_view(), name='reserve_pagination'),
    path('reserve-period/', views.reserve_period_list_create, name='reserve_period'),
    path('reserve-period/<int:pk>/', views.RerservePeriodDetailUpdateDelete.as_view(), name='reserve_period_detail'),
    path('reserve-period-pagination/', views.ReservePeriodPagination.as_view(), name='reserve_period_pagination'),
    path('checkout/', views.checkout, name='checkout'),
    path('payments/', views.payment, name='payments'),
    path('payments-pagination/', views.payment_pagination, name='payments_pagination'),
]

router = SimpleRouter()

router.register("lots", views.LotModelViewSet, basename="lots") 
router.register("fares", views.FareModelViewSet, basename="fares") 
router.register("fares-pagination", views.FareModelPaginationViewSet, basename="fares_pagination") 
router.register("fares-period", views.FarePeriodModelViewSet, basename="fares_period") 
router.register("fares-period-pagination", views.FarePeriodModelPaginationViewSet, basename="fares_period_pagination") 
router.register("clients", views.ClientModelViewSet, basename="clients") 
router.register("clients-pagination", views.ClientModelPaginationViewSet, basename="clients_pagination") 

urlpatterns += router.urls

