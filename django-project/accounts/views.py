from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import CustomUserDetailSerializer, UserDepositSerializer, UserSavingSerializer, UserCreditLoanSerializer
from .models import User, Deposit, Saving, CreditLoan, UserDeposit, UserSaving, UserCreditLoan
from datetime import date
from collections import Counter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns
import io
import base64
import textwrap

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserInfo(request, username):
    """사용자 정보를 반환"""
    try:
        user = User.objects.get(username=username)
        
        # 사용자가 가입한 예적금 정보 조회
        user_deposits = UserDeposit.objects.filter(user=user).values('deposit__fin_prdt_nm', 'deposit__fin_prdt_cd')
        user_savings = UserSaving.objects.filter(user=user).values('saving__fin_prdt_nm', 'saving__fin_prdt_cd')

        # 예금 정보 정리
        deposits = [{'name': deposit['deposit__fin_prdt_nm'], 'code': deposit['deposit__fin_prdt_cd']} for deposit in user_deposits]

        # 적금 정보 정리
        savings = [{'name': saving['saving__fin_prdt_nm'], 'code': saving['saving__fin_prdt_cd']} for saving in user_savings]

        user_data = {
            "username": user.username,
            "birthday": user.birthday,
            "age": user.age,
            "gender": user.gender,
            "deposits": deposits,  # 예금 정보 추가
            "savings": savings     # 적금 정보 추가
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

#  한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf' 
fontprop = fm.FontProperties(fname=font_path)
matplotlib.rc('font', family=fontprop.get_name())

def create_graph(data, title):
    """데이터를 기반으로 막대 그래프를 생성하고 Base64 문자열로 반환합니다."""
    labels = [item['name'] for item in data]
    values = [item['count'] for item in data]

    # 텍스트를 줄 바꿈 처리
    wrapped_labels = ['\n'.join(textwrap.wrap(label, 10)) for label in labels]

    plt.figure(figsize=(12, 6))
    sns.barplot(x=wrapped_labels, y=values, palette='viridis', dodge=False)
    plt.legend([],[], frameon=False)
    plt.xlabel('Products')
    plt.ylabel('Count')
    plt.title(title)
    plt.tight_layout()  # 자동 레이아웃 조정

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return image_base64


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProductRecommend(request, username):
    """해당 사용자의 성별과 연령대가 일치하는 사람들이 많이 가입한 예금 및 적금"""
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    
    user_gender = user.gender
    user_age_group = (user.age // 10) * 10

    # 동일한 성별과 연령대의 사용자 필터링
    similar_users = User.objects.filter(gender=user_gender, age__gte=user_age_group, age__lt=user_age_group + 10)

    # 예금 및 적금 상품 목록 수집
    deposit_counter = Counter()
    saving_counter = Counter()

    # 사용자가 이미 가입한 예금 및 적금 상품 목록 수집
    user_deposits = set(UserDeposit.objects.filter(user=user).values_list('deposit__fin_prdt_cd', flat=True))
    user_savings = set(UserSaving.objects.filter(user=user).values_list('saving__fin_prdt_cd', flat=True))

    for similar_user in similar_users:
        similar_user_deposits = UserDeposit.objects.filter(user=similar_user).values_list('deposit__fin_prdt_cd', flat=True)
        similar_user_savings = UserSaving.objects.filter(user=similar_user).values_list('saving__fin_prdt_cd', flat=True)
        
        # 사용자가 이미 가입한 상품은 제외하고 카운트
        deposit_counter.update([d for d in similar_user_deposits if d not in user_deposits])
        saving_counter.update([s for s in similar_user_savings if s not in user_savings])

    # 많이 가입한 예금 및 적금 상위 5개 추출
    top_deposits = deposit_counter.most_common(5)
    top_savings = saving_counter.most_common(5)

    # 예금 및 적금 상품의 상세 정보 조회
    top_deposit_details = []
    for fin_prdt_cd, count in top_deposits:
        deposit_product = Deposit.objects.get(fin_prdt_cd=fin_prdt_cd)
        top_deposit_details.append({
            'name': deposit_product.fin_prdt_nm,
            'code': deposit_product.fin_prdt_cd,
            'count': count
        })

    top_saving_details = []
    for fin_prdt_cd, count in top_savings:
        saving_product = Saving.objects.get(fin_prdt_cd=fin_prdt_cd)
        top_saving_details.append({
            'name': saving_product.fin_prdt_nm,
            'code': saving_product.fin_prdt_cd,
            'count': count
        })

    # 그래프 생성
    deposit_graph = create_graph(top_deposit_details, "Top Deposits")
    saving_graph = create_graph(top_saving_details, "Top Savings")

    return Response({
        "top_deposits": top_deposit_details,
        "top_savings": top_saving_details,
        "deposit_graph": deposit_graph,
        "saving_graph": saving_graph
    })