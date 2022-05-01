from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import RobotSerializer
from .models import Robot
from socketio_app.views import sio


@api_view(['GET'])
def get_robot(request):
    robots = Robot.objects.all()
    serializer = RobotSerializer(robots, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def start(request):
    sio.emit('my_broadcast_event', {'message': 'hello'})
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def end(request):
    sio.emit('my_broadcast_event', {'message': 'hello'})
    return Response(status=status.HTTP_200_OK)




