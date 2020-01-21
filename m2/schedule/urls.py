from django.urls import path, include
from schedule import views


#############################################################

from rest_framework import routers


############################################################

router = routers.DefaultRouter()
router.register('', views.scheduleView)

############################################################


urlpatterns = [

    path('schedule/', include(router.urls)),



]
