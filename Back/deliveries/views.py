from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Address, Alarm, Category, Delivery
from .serializers import DeliverySerializer, CountSerializer, AlarmSerializer
import datetime


@api_view(['POST'])
# @permission_classes([AllowAny]) # 테스트용
def create(request):
    data = request.data
    # 주소가 db에 없으면 추가
    address = list(request.data.get('address').split())
    sido = address[0]
    sigungu = address[1]
    dong = address[2]
    doro = address[3]
    try:
        address = get_object_or_404(Address, sido=sido, sigungu=sigungu, dong=dong, doro=doro)
    except:
        address = Address.objects.create(sido=sido, sigungu=sigungu, dong=dong, doro=doro)
        address.save()
    # 카테고리가 db에 없으면 추가
    try:
        category = get_object_or_404(Category, name=data.get('category'))
    except:
        category = Category.objects.create(name=data.get('category'))
        category.save()
    UserModel = get_user_model()
    user = get_object_or_404(UserModel, username=data.get('user'))
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        delivery = serializer.save(category=category, address=address, user=user)
        delivery.save()
        return Response(status=status.HTTP_201_CREATED)

# 메인페이지 데이터
@api_view(['GET'])
# @permission_classes([AllowAny]) # 테스트용
def get_deliveries(request):
    deliveries = Delivery.objects.all()
    res = deliveries.aggregate(all = Count('id'),
    move = Count('state', filter=Q(state="배송")),
    wait = Count('state', filter=Q(state="대기")),
    complete = Count('state', filter=Q(state="완료"))
    )
    return Response(res, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_deliveries_mine(request):
    deliveries = request.user.delivery_set.all()
    res = deliveries.aggregate(all = Count('id'),
    move = Count('state', filter=Q(state="배송")),
    wait = Count('state', filter=Q(state="대기")),
    complete = Count('state', filter=Q(state="완료"))
    )
    return Response(res, status=status.HTTP_200_OK)

# 상세 페이지 데이터
@api_view(['GET'])
# @permission_classes([AllowAny]) # 테스트용
def get_detail_deliveries(request):
    deliveries = Delivery.objects.all()
    # page = request.GET.get('page')
    # paginator = Paginator(deliveries, '20')
    # deliveryList = paginator.page(int(page))
    serializer = DeliverySerializer(deliveries, many=True)
    # res = {
    #     'page': {
    #         'countAll': deliveries.count(),
    #         'current': page,
    #         'pageSize': 20,
    #     },
    #     'data': serializer.data,
    # }
    return Response(serializer.data, status=status.HTTP_200_OK)

# 상태 변화 처리
@api_view(['POST'])
@permission_classes([AllowAny])
def move(request):
    try:
        delivery = get_object_or_404(Delivery, pk=request.POST.get('pk'))
        delivery.state = request.POST.get('state')
        delivery.moved_at = datetime.datetime()
        delivery.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
        

# 세부 페이지 검색
@api_view(['POST'])
# @permission_classes([AllowAny]) # 테스트용
def search_detail_location(request): # 지역 검색
    sido = request.POST.get('sido')
    sigungu = request.POST.get('sigungu')
    dong = request.POST.get('dong')
    # address = Address.objects.filter(sido=sido)
    if dong:
        address = Address.objects.filter(sido=sido, sigungu=sigungu, dong=dong).prefetch_related("delivery_set")
    elif sigungu:
        address = Address.objects.filter(sido=sido, sigungu=sigungu).prefetch_related("delivery_set")
    else:
        address = Address.objects.filter(sido=sido).prefetch_related("delivery_set")
    deliveries = address[0].delivery_set.all()
    for i in range(1, address.count()):
        deliveries = deliveries.union(address[i].delivery_set.all())
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

    

@api_view(['POST'])
# @permission_classes([AllowAny]) # 테스트용
def search_detail_user(request): # 배송기사별 검색
    deliveries = get_list_or_404(Delivery, userId=request.POST.get('userId'))
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([AllowAny]) # 테스트용
def search_detail_number(request): # 송장 번호 검색
    deliveries = get_list_or_404(Delivery, number=request.POST.get('number'))
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#메인 페이지 검색

@api_view(['GET'])
# @permission_classes([AllowAny]) # 테스트용
def search_location(request): # 지역 검색
    sido = request.GET.get('sido')
    sigungu = request.GET.get('sigungu')
    dong = request.GET.get('dong')
    if dong:
        address = Address.objects.filter(sido=sido, sigungu=sigungu, dong=dong).prefetch_related("delivery_set")
    elif sigungu:
        address = Address.objects.filter(sido=sido, sigungu=sigungu).prefetch_related("delivery_set")
    else:
        address = Address.objects.filter(sido=sido).prefetch_related("delivery_set")
    count = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    for i in address:

        count += i.delivery_set.count() 
        count_1 += i.delivery_set.filter(state="배송").count() 
        count_2 += i.delivery_set.filter(state="대기").count()
        count_3 += i.delivery_set.filter(state="완료").count()
    res = {
        'all': count,
        'move': count_1,
        'wait': count_2,
        'complete': count_3,
    }
    
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([AllowAny]) # 테스트용
def search_user(request): # 배송기사별 검색
    deliveries = Delivery.objects.filter(userId=request.POST.get('userId'))
    res = deliveries.aggregate(all = Count('id'),
    move = Count('state', filter=Q(state="배송")),
    wait = Count('state', filter=Q(state="대기")),
    complete = Count('state', filter=Q(state="완료"))
    )

    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_address(request):
    sido = request.GET.get('sido')
    sigungu = request.GET.get('sigungu')
    sidos = []
    sigungus = []
    dongs = []
    if sigungu:
        dongs = Address.objects.filter(sido=sido, sigungu=sigungu).order_by('dong')
        dongs = dongs.values_list('dong', flat=True).distinct()
    elif sido:
        sigungus = Address.objects.filter(sido=sido).order_by('sigungu')
        sigungus = sigungus.values_list('sigungu', flat=True).distinct()
    else:
        sidos = Address.objects.all().order_by('sido')
        sidos = sidos.values_list('sido', flat=True).distinct()
    res = {
        'sido': sidos,
        'sigungu': sigungus,
        'dong': dongs,
    }
    return Response(res, status=status.HTTP_200_OK)

@api_view(['POST']) # 알림 생성
@permission_classes([AllowAny])
def create_alarm(request):
    serializer = AlarmSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET']) # 알림 조회
@permission_classes([AllowAny])
def alarm(request):
    username = request.user.username
    try:
        alarms = get_list_or_404(Alarm, user=username)
        serializer = AlarmSerializer(alarms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def alarm_check(request):
    res=False
    if Alarm.objects.filter(user=request.user.username, check=False).exists():
        res=True
    return Response(res, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def alarm_delete(request):
    a_list = request.data
    print(1, a_list)
    for i in a_list:
        now = Alarm.objects.filter(id=i)
        now.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def alarm_view(request):
    alarm = Alarm.objects.filter(id=request.data.get('id'))
    alarm.check = True
    alarm.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_chart_data(request):
    sidos = Address.objects.prefetch_related('delivery_set').values('sido')
    sidos = sidos.annotate(count=Count('delivery'))
    labels = []
    data = []
    for i in sidos:
        labels.append(i['sido'])
        data.append(i['count'])
    res = {
        'labels': labels,
        'data': data,
    }
    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_chart_data_d(request):
    etcs = Delivery.objects.values('etc').exclude(etc__exact='').exclude(etc__isnull=True).annotate(count=Count('etc'))
    labels = []
    data = []
    for i in etcs:
        labels.append(i['etc'])
        data.append(i['count'])
    res = {
        'labels': labels,
        'data': data,
    }
    return Response(res, status=status.HTTP_200_OK)





