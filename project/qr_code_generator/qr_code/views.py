from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from .models import QrGenerator
from .serializers import QrGeneratorSerializer
from qr_code import serializers


@api_view(['GET', 'POST'])
def all_qr_codes(request):
    if request.method == "GET":
        img = QrGenerator.objects.all()
        serializer = QrGeneratorSerializer(img, many=True)
        context ={
            "img":img
            }
        # return Response(serializer.data)

        
    
    
    elif request.method == "POST":
        data = request.data
        serializer = QrGeneratorSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    return render(request, 'home.html', context)



@api_view(['GET', 'PUT', 'DELETE'])
def img_detail_view(request, id):
    try:
        img = QrGenerator.objects.get(id=id)
    except img.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = QrGeneratorSerializer(img)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    elif request.method == "PUT":
        serializer = QrGeneratorSerializer(img, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
        img.delete()
        return Response(status=status.HTTP_410_GONE)