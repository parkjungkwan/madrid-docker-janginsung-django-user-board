from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from user.model_data import DbUploader
from user.models import User
from user.serializers import UserSerializer



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@parser_classes([JSONParser])
def users(request):
    try:
        if request.method == 'GET':
            all_users = User.objects.all().values()
            serializer = UserSerializer(all_users, many=True)
            return JsonResponse(data=serializer.data, safe=False)
        elif request.method == 'POST':
            new_user = request.data
            serializer = UserSerializer(data=new_user)
            if serializer.is_valid():
                print(serializer)
                serializer.save()
                return JsonResponse({'join': 'SUCCESS'})
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PUT':
            modifyemail = request.data
            user = User.objects.get(id=modifyemail['id'])
            dbuser = User.objects.all().filter(id=modifyemail['id']).values()[0]
            for i in modifyemail:
                dbuser[i] = modifyemail[i]
            serializer = UserSerializer(data=dbuser)
            if serializer.is_valid():
                serializer.update(user, dbuser)
            return JsonResponse({'modify': 'SUCCESS'})
        elif request.method == 'DELETE':
            deluser = request.data
            dbuser = User.objects.get(user_email=deluser['user_email'])
            if deluser['user_email'] == dbuser.user_email:
                dbuser.delete()
                return JsonResponse({'remove': 'SUCCESS'})
            else:
                return JsonResponse({'remove': 'error'})

    except:
        return JsonResponse({'users': 'fail'})


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        loginuser = request.data
        print('************** data 확인 ************')
        print(loginuser)
        dbUser = User.objects.get(user_email=loginuser['email'])
        if loginuser['password'] == dbUser.password:
            userSerializer = UserSerializer(dbUser, many=False)
            return JsonResponse(data=userSerializer.data, safe=False,)
    except:
        return JsonResponse({'login':'fail'})


@api_view(['GET'])
def user(request):
    try:
        finduser = request.data
        dbUser = User.objects.all().filter(user_email=finduser['user_email']).values()[0]
        return JsonResponse(data=dbUser, safe=False)
    except:
        return JsonResponse({'find': 'fail'})


@api_view(['GET'])
def exist(request, email):
    try:
        if email is not None:
            joinuseremail = request.data
            existck = User.objects.all().filter(user_email=joinuseremail['user_email']).values()[0]
            if joinuseremail['user_email'] == existck['user_email']:
                return JsonResponse({'exist': '해당 이메일은 있습니다'})
    except:
        return JsonResponse({'exist':'사용 가능합니다.'})


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def upload(request):
#     print('######## 1 ########')
#     DbUploader().insert_data()
#     return JsonResponse({'Product Upload': 'SUCCEESS'})
