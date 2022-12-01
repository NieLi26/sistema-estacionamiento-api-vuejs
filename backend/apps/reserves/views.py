from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


from .models import Lot, Fare, Reserve, Payment, FarePeriod, ReservePeriod, Client
from .serializers import LotSerializer, FareSerializer, ReserveSerializer, PaymentSerializer, CheckOutSerializer, FarePeriodSerializer, ReservePeriodSerializer, ClientSerializer

class FarePagination(PageNumberPagination):
    page_size = 2

class FarePeriodPagination(PageNumberPagination):
    page_size = 2

class PaymentPagination(PageNumberPagination):
    page_size = 2

class ReservePeriodPagination(PageNumberPagination):
    page_size = 2

class ClientPagination(PageNumberPagination):
    page_size = 2

class LotModelViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer

class FareModelViewSet(viewsets.ModelViewSet):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer

class FareModelPaginationViewSet(viewsets.ModelViewSet):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer
    pagination_class = FarePagination

class FarePeriodModelViewSet(viewsets.ModelViewSet):
    queryset = FarePeriod.objects.all()
    serializer_class = FarePeriodSerializer

class FarePeriodModelPaginationViewSet(viewsets.ModelViewSet):
    queryset = FarePeriod.objects.all()
    serializer_class = FarePeriodSerializer
    pagination_class = FarePeriodPagination


class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
class ClientModelPaginationViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination

# class ReserveSerializerAPIView(views.APIView):

# @api_view(['GET', 'POST', 'PATCH'])
# def reserve(request, pk=None): 
#     if request.method == 'GET':
#         reserve_list = Reserve.objects.all()
#         serializer =  ReserveSerializer(reserve_list, many=True)
#         if serializer.data:
#             return Response(serializer.data)
#         return Response({'No hay reservas creadas'})
    
#     elif request.method == 'POST':   
#         serializer = ReserveSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PATCH':
#         reserve = Reserve.objects.get(id=pk)
#         serializer =  ReserveSerializer(reserve, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     else:
#         return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def reserve_list_create(request):
    if request.method == 'GET':
        reserve_list = Reserve.objects.all() 
        serializer =  CheckOutSerializer(reserve_list, many=True)

        if serializer.data:
            return Response(serializer.data)
        return Response({'detail': "Not content"}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':   
        serializer = ReserveSerializer(data=request.data, context=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ReservePagination(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params.get('q', '')
        reserve_list = Reserve.objects.filter(licence__icontains=q) 
        paginator = PaymentPagination()
        page_obj = paginator.paginate_queryset(reserve_list, request)
        serializer =  ReserveSerializer(page_obj, many=True)
        if serializer.data:
            return paginator.get_paginated_response(serializer.data)
        return Response({'detail': "Not content"}, status=status.HTTP_200_OK)

@api_view(['DELETE', 'PATCH', 'GET'])
def reserve_detail_update_delete(request, pk):
    if request.method == 'GET':
        try:
            reserve = Reserve.objects.get(id=pk)
            serializer =  ReserveSerializer(reserve)
            return Response(serializer.data)
        except:
            return Response({'detail': "Not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PATCH':
        reserve = Reserve.objects.get(id=pk)
        serializer =  ReserveSerializer(reserve, data=request.data, partial=True, context=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reserve = Reserve.objects.get(id=pk)
        reserve.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST'])
def reserve_period_list_create(request):
    if request.method == 'GET':
        reserve_list = ReservePeriod.objects.all() 
        serializer =  ReservePeriodSerializer(reserve_list, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response({'detail': "Not content"}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':   
        serializer = ReservePeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
class ReservePeriodPagination(APIView):
    def get(self, request, *args, **kwargs):
        q = request.query_params.get('q', '')
        reserve_list = ReservePeriod.objects.filter(licence__icontains=q) 
        paginator = PaymentPagination()
        page_obj = paginator.paginate_queryset(reserve_list, request)
        serializer =  ReservePeriodSerializer(page_obj, many=True)
        if serializer.data:
            return paginator.get_paginated_response(serializer.data)
        return Response({'detail': "Not content"}, status=status.HTTP_200_OK)


class RerservePeriodDetailUpdateDelete(APIView):
    def get(self, request, *args, **kwargs):
        try:
            reserve_period = ReservePeriod.objects.get(id=kwargs['pk'])
            serializer =  ReservePeriodSerializer(reserve_period)
            return Response(serializer.data)
        except:
            return Response({'detail': "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, *args, **kwargs):
        reserve_period = ReservePeriod.objects.get(id=kwargs['pk'])
        serializer =  ReservePeriodSerializer(reserve_period, data=request.data, partial=True, context=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        reserve_period = ReservePeriod.objects.get(id=kwargs['pk'])
        reserve_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def checkout(request):
    if request.method == 'GET':

        reserves = Reserve.objects.filter(status=Reserve.Status.BUSY)
        serializer = CheckOutSerializer(reserves, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':   
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def payment(request):
    if request.method == 'GET':
        payment_list = Payment.objects.all()
        serializer = PaymentSerializer(payment_list, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response({'detail': "Not content"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def payment_pagination(request):
    if request.method == 'GET':
        payment_list = Payment.objects.all()
        paginator = PaymentPagination()
        page_obj = paginator.paginate_queryset(payment_list, request)
        serializer = PaymentSerializer(page_obj, many=True)
        return paginator.get_paginated_response(serializer.data)

