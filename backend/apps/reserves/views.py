import json
from rest_framework import viewsets, views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Lot, Fare, Reserve, Payment, FarePeriod, ReservePeriod, Client
from .serializers import LotSerializer, FareSerializer, ReserveSerializer, PaymentSerializer, CheckOutSerializer, FarePeriodSerializer, ReservePeriodSerializer, ClientSerializer

class LotModelViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer

class FareModelViewSet(viewsets.ModelViewSet):
    queryset = Fare.objects.all()
    serializer_class = FareSerializer

class FarePeriodModelViewSet(viewsets.ModelViewSet):
    queryset = FarePeriod.objects.all()
    serializer_class = FarePeriodSerializer

class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'Metodo no permitido'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
        serializer =  ReserveSerializer(reserve, data=request.data, partial=True)
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

@api_view(['GET', 'POST', 'PATCH'])
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
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

