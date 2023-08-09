from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.http import JsonResponse

from apps.home.models import *
from apps.home.serializers import *
from django.db.models import Max
from django.shortcuts import render, redirect
from django.contrib.auth import *

import json

# @login_required(login_url="/login/")
class LoginAPI(APIView):
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # CMM_LOGIN에 있는 아이디와 비밀번호 비교 로직 구현
            if self.is_valid_login(username, password): 
                return JsonResponse({'message': '로그인 성공'})
            else:
                return JsonResponse({'message': '로그인 실패'}, status=401)
        except Exception as e:
            return JsonResponse({'message': '에러 발생'}, status=500)
    
    def is_valid_login(self, username, password):
        # CMM_LOGIN에 있는 아이디와 비밀번호를 확인하는 로직을 구현합니다.
        # 예를 들어, 아래처럼 데이터베이스 조회나 다른 방식으로 확인할 수 있습니다.
        
        try:
            cmm_user = CmmLogin.objects.get(login_id=username)
            if cmm_user.login_pwd == password:
                return True
        except CmmLogin.DoesNotExist:
            return False
        
        return False

    





