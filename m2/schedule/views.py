from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Schedule
from django.http.response import HttpResponseNotAllowed

############## Restful API ###################
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status


from rest_framework.response import Response
from schedule.serializers import ScheduleSerializer


from django.contrib.auth.models import User

###################################################

from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.permissions import AllowAny
##############################################


class scheduleView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

def scheduleResponse():
    return "this is the schedule"
