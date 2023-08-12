from rest_framework import generics
# Create your views here.
from .models import *

from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class WorkersApiView(APIView):
    def get_object(self, phone):
        try:
            return Workers.objects.get(phone=phone)
        except Workers.DoesNotExist:
            raise Http404
        
    def get(self, request, phone, format=None):
        worker = self.get_object(phone)
        units = Unit.objects.filter(worker=worker)
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
    


# Request format
# {
# "unit" : "1",
# "latitude": "8",
# "longitude" : "9"
# }

class VisitApiView(APIView):
    def post(self, request, phone, format=None):
        unitId = self.request.data["unit"]
        workerPhone = Unit.objects.get(pk=unitId).worker.phone

        serializer = VisitSerializer(data=request.data)
        if workerPhone == phone:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"bad": "bad request, you are not in this unit"})  


class WorkersUnit(generics.ListCreateAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        queryset = Unit.objects.all()
        phone = self.request.query_params.get('phone')
        if phone is not None:
            worker= Workers.objects.get(pbone=phone)
            queryset = queryset.filter(worker=worker)


        return queryset


class WorkerList(generics.ListCreateAPIView):
    serializer_class = WorkersSerializer

    def get_queryset(self):
        queryset = Workers.objects.all()
        return queryset
    


class MakeVisit(generics.ListCreateAPIView):
    serializer_class = VisitSerializer

    def get_queryset(self):
        queryset = Visit.objects.all()
        return queryset
    
class WorkersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= WorkersSerializer
    queryset = Workers.objects.all()

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VisitSerializer
    queryset = Visit.objects.all()