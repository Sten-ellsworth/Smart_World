from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer


# Create your views here.
# List all stocks or create a new one
# Stocks/


# class StockList(APIView):
#
#     def get(self, request):
#         stocks = Stock.objects.all()
#         serializer = StockSerializer(stocks, many=True)
#         return Response(serializer.data)
#
#     def post(self):
#         pass

@api_view(['GET'])
def getList(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailList(request, pk):
    try:
        stocks = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stocks)
        return Response(serializer.data)


@api_view(['PUT'])
def putList(request, pk):
    try:
        stocks = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StockSerializer(stocks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def postList(request):

    if request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# @api_view(['GET', 'PUT', 'DELETE'])
# def stock_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         stocks = Stock.objects.get(pk=pk)
#     except Stock.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = StockSerializer(stocks)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = StockSerializer(stocks, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         stocks.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
