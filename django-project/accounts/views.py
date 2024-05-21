from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import CustomUserDetailSerializer, UserDepositSerializer, UserSavingSerializer, UserCreditLoanSerializer
from .models import User, Deposit, Saving, CreditLoan, UserDeposit, UserSaving, UserCreditLoan
from datetime import date

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    print(username)

    if request.method == 'GET':
        serializer = CustomUserDetailSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = CustomUserDetailSerializer(user, data=request.data, partial=True)
        # print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_deposit(request):
    username = request.data.get('username')
    fin_prdt_cd = request.data.get('fin_prdt_cd')
    if not fin_prdt_cd:
        return Response({'error': 'fin_prdt_cd is required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    deposit = get_object_or_404(Deposit, fin_prdt_cd=fin_prdt_cd)
    user_deposit = UserDeposit.objects.filter(user=user, deposit=deposit).first()

    if user_deposit:
        # 이미 가입된 경우 제거
        user_deposit.delete()
        return Response({'status': 'success', 'message': 'Deposit removed successfully.'}, status=status.HTTP_200_OK)
    else:
        # 가입되지 않은 경우 새로 가입
        user_deposit = UserDeposit.objects.create(user=user, deposit=deposit, join_date=date.today())
        serializer = UserDepositSerializer(user_deposit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_saving(request):
    username = request.data.get('username')
    fin_prdt_cd = request.data.get('fin_prdt_cd')

    if not fin_prdt_cd:
        return Response({'error': 'fin_prdt_cd is required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    saving = get_object_or_404(Saving, fin_prdt_cd=fin_prdt_cd)
    user_saving = UserSaving.objects.filter(user=user, saving=saving).first()

    if user_saving:
        # 이미 가입된 경우 제거
        user_saving.delete()
        return Response({'status': 'success', 'message': 'Saving removed successfully.'}, status=status.HTTP_200_OK)
    else:
        # 가입되지 않은 경우 새로 가입
        user_saving = UserSaving.objects.create(user=user, saving=saving, join_date=date.today())
        serializer = UserSavingSerializer(user_saving)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_creditloan(request):
    username = request.data.get('username')
    fin_prdt_cd = request.data.get('fin_prdt_cd')
    print(username)

    if not fin_prdt_cd:
        return Response({'error': 'fin_prdt_cd is required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(User, username=username)
    creditloan = get_object_or_404(CreditLoan, fin_prdt_cd=fin_prdt_cd)
    user_creditloan = UserCreditLoan.objects.filter(user=user, creditloan=creditloan).first()

    if user_creditloan:
        # 이미 가입된 경우 제거
        user_creditloan.delete()
        return Response({'status': 'success', 'message': 'CreditLoan removed successfully.'}, status=status.HTTP_200_OK)
    else:
        # 가입되지 않은 경우 새로 가입
        user_creditloan = UserCreditLoan.objects.create(user=user, creditloan=creditloan, join_date=date.today())
        serializer = UserCreditLoanSerializer(user_creditloan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProduct(request, username):
    user_deposit = UserDeposit.objects.filter(user__username=username)
    user_saving = UserSaving.objects.filter(user__username=username)
    user_creditloan = UserCreditLoan.objects.filter(user__username=username)
    deposits_serializer = UserDepositSerializer(user_deposit, many=True)
    savings_serializer = UserSavingSerializer(user_saving, many=True)
    creditloans_serializer = UserCreditLoanSerializer(user_creditloan, many=True)
    return Response({
        "deposits": deposits_serializer.data,
        "savings": savings_serializer.data,
        "creditloans": creditloans_serializer.data,
    }, status=status.HTTP_200_OK)