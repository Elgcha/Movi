import json
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
import socketio
from deliveries.models import Address, Category, Delivery
from robots.models import Robot



sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*', cors_credentials=True)
thread = None
status = False
pickup = ''
unload = ''


def robot_status(v, a, state,  qr=''):
    print('----------------------')
    print(v, a, state, qr)
    robot = get_object_or_404(Robot, id=1)
    robot.state = '운송' if abs(v) > 0.1 or a else '대기' 
    robot.save()
    if qr:
        address = qr.get('address')
        address = list(address.split())
        print(address)
        address = get_object_or_404(Address, sido=address[0], sigungu=address[1], dong=address[2], doro=address[3])
        userM = get_user_model()
        user = get_object_or_404(userM, username=qr.get('user'))
        category =get_object_or_404(Category, name=qr.get('category'))

        delivery = get_object_or_404(Delivery, category=category, address=address, user=user)
        delivery.state = state
        delivery.save()


@sio.event # 테스트용
def my_broadcast_event(sid, message):
    # sio.emit('my_response', {'data': message['data']})
    pass

@sio.event
def SocketNode(sid):
    global status
    status = False

@sio.event
def SocketNode2Server(sid, message):
    global status, pickup, unload
    print(message)
    velocity = message.get('robot').get('velocity', 0)
    angular = message.get('robot').get('angular', 0)
    robot_state = message.get('robot').get('status')
    print(f'v: {velocity}, a: {angular}, status: {robot_state}')
    qr = []
    try:
        qr = message.get('qr')[0]
        qr = str(qr).strip("'<>() ").replace('\'', '\"')
        qr = json.loads(qr)
    except Exception  as E:
        print(E)
    print(qr)
    try:
        box_data = message.get('boxinfo', {})[0]
        print(box_data)
        box_data = json.loads(box_data)
        box_status = box_data.get('box_status', '')
        box_pickup = box_data.get('pickup_time', '')
        box_unload = box_data.get('unloading_time', '')
    except Exception  as E:
        print(E)
    # print(box_status, box_pickup, box_unload)
    try:
        if status != robot_state and qr and box_data:
            if pickup != box_pickup:
                status = robot_state
                pickup = box_pickup
                robot_status(velocity, angular, '배송', qr)
            elif unload != box_unload:
                status = robot_state
                unload = box_unload
                robot_status(velocity, angular, '완료', qr)
        else:
            robot_status(velocity, angular, '')

    except:
        pass
    
@sio.event
def disconnect_request(sid):
    sio.disconnect(sid)


@sio.event
def connect(sid, environ):
    sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)


@sio.event
def disconnect(sid):
    print('Client disconnected')