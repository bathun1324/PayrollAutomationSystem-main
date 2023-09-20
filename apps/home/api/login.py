from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import json
import secrets

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
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

import json

# @login_required(login_url="/login/")
class LoginAPI(APIView):
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # CMM_LOGIN에 있는 아이디와 비밀번호 비교 로직 구현
            user = self.is_valid_login(username, password)
            if user:
                user = self.is_valid_login(username, password)  # CmmLogin 모델에서 사용자 정보 가져오기
                refresh = RefreshToken()
                access = AccessToken()
                access.access_token = self.generate_access_token(user)
                refresh.refresh_token = self.generate_refresh_token(user) 

                return JsonResponse({
                    'message': '로그인 성공',
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'user_info': {
                        'login_id': user.login_id,
                        'perm' : user.perm,
                        'empl_no': user.empl_no,
                        'corp_no' : user.corp_no,
                        'dept_no ' : user.dept_no,
                        # 추가로 포함시키고 싶은 필드들을 여기에 추가
                    }
                })
            else:
                return JsonResponse({'message': '로그인 실패'}, status=401)
        except Exception as e:
            print(f'에러 발생: {e}')
            return JsonResponse({'message': '에러 발생'}, status=500)
        
    @staticmethod
    def generate_access_token(user):
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def generate_refresh_token(user):
        return secrets.token_urlsafe(64)
    
    def is_valid_login(self, username, password):
        # CMM_LOGIN에 있는 아이디와 비밀번호를 확인하는 로직을 구현합니다.
        # 예를 들어, 아래처럼 데이터베이스 조회나 다른 방식으로 확인할 수 있습니다.
        
        try:
            cmm_user = CmmLogin.objects.get(login_id=username)
            if cmm_user.login_pwd == password:
                return cmm_user
        except CmmLogin.DoesNotExist:
            return False
        
        return False


