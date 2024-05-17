# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import CustomRegisterSerializer

# @api_view(['POST'])
# def signup(request):
#     if request.method == 'POST':
#         print(request.data)  # 요청 데이터 출력
#         serializer = CustomRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

