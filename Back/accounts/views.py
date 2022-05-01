from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserSerializer
from deliveries.models import Alarm

# jwt 토큰 - 헤더에 Authorization: "JWT <Token>"
# 회원가입
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password = request.data.get('password')
    passwordConfirm = request.data.get('passwordConfirm')
    username = request.data.get('username')
    email = request.data.get('email')
    # 데이터 확인
    try:
        if password != passwordConfirm:
            print(password, passwordConfirm)
            return Response({ 'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        UserModel = get_user_model()
        if  email != '@' not in email or not (email[-4:] == '.com') :
            return Response({ 'error': '잘못된 이메일 형식입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        # 데이터 직렬화
        if UserModel.objects.filter(username=username).exists():
            return Response({ 'error': '중복된 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
    

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.is_active = 0
            if username == 'manager':
                user.is_active = 1
                user.is_staff = 1
                user.save()
            else:
                user.save()
                userModel = get_user_model()
                alarm = Alarm()
                alarm.user = 'manager'
                alarm.check = False
                alarm.title = '신규 가입 요청'
                alarm.content = f'다음 유저로부터 신규 가입 요청이 있습니다. \n \n \n 유저명: {user.username} \n \n 이메일: {user.email}'
                alarm.type = 'new'
                alarm.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error":"test"}, status=status.HTTP_401_UNAUTHORIZED)
    except TypeError:
        return Response({ "error": 'test'}, status=status.HTTP_400_UNAUTHORIZED)

# 계정 활성화
@api_view(['POST'])
def user_active(request):
    userModel = get_user_model()
    user = get_object_or_404(userModel, username=request.data.get('username'))
    user.is_active = 1
    user.save()
    alarm = get_object_or_404(Alarm, pk=request.data.get('id'))
    alarm.delete()
    return Response(status=status.HTTP_200_OK)

    
# 개인정보 수정
@api_view(['PUT'])
def profile_edit(request):
    users = get_user_model()
    me = request.user
    email = request.data.get('email')
    username = request.data.get('username')
    person = get_object_or_404(users, pk=me.pk)

    if me.username != username:
        person.username = username

    if me.email != email:
        if '@' not in email or not (email[-4:] == '.com'):
            return Response({ 'error': '잘못된 이메일 형식입니다.'})
        person.email = email
    person.save()
    return Response(status=status.HTTP_200_OK)

# 유저 권한 확인
@api_view(['POST'])
def user_check(request):
    check = False
    if request.user.is_staff:
        check = True
    res = {
        'username': request.user.username,
        'staff': check,
    }
    return Response(res, status=status.HTTP_200_OK)
