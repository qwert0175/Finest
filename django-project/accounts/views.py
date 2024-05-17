# # django 내에서 템플릿 만들어서 볼게 아님
# # from django.shortcuts import render

# # 서버에서는 클라이언트로 JSON을 반환
# import json
# from django.http import JsonResponse 

# from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view
# from rest_framework.decorators import permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status

# from .models import User, DetailUser
# from .serializers import UserDetailSerializer 

# User = get_user_model()


# ### 회원 상세정보 수정 ###

# @api_view(['GET', 'PUT'])
# # 로그인 여부 확인
# @permission_classes([IsAuthenticated])
# def userDetail_list(request):
#     # 회원 상세정보를 만든적이 없다면 생성
#     if not DetailUser.objects.filter(user=request.user).exists():
#         DetailUser.objects.create(user=request.user)
#         userdetail = DetailUser.objects.get(user=request.user)

#     # 회원 상세정보를 만든적이 있다면 수정
#     else:
#         userdetail = DetailUser.objects.get(user=request.user)

#     # 요청이 'get'이라면 조회한 내용을 리턴
#     if request.method == 'GET':
#         serializer = UserDetailSerializer(userdetail)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     # 요청이 'put'이라면 수정한 내용을 DB에 저장
#     elif request.method == "PUT":
#         serializer = UserDetailSerializer(userdetail, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
      

# ### 회원 삭제 ###

# @api_view(['DELETE'])
# # 로그인 여부 확인
# @permission_classes([IsAuthenticated])
# def delete_user(request):
#     user = request.user
#     detail = DetailUser.objects.get(user=user)
#     detail.delete()
#     user.delete()
#     return Response('{msg: delete complete}', status=status.HTTP_200_OK)


# ### 아이디 생성시 일치여부 확인 ###

# @api_view(['POST'])
# def checkUserID(request):
#     username = request.data['username']

#     if User.objects.filter(username=username).exists():
#         isExist = True
#     else:
#         isExist = False

#     result = {'isExist': isExist}
#     return JsonResponse(result, status=status.HTTP_200_OK)