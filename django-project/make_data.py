import random
import requests
import json
from collections import OrderedDict
from datetime import datetime, timedelta, date

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'

def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

def random_date(start, end):
    return start + timedelta(days=random.randint(0, int((end - start).days)))

def calculate_age(birthday, reference_date):
    return reference_date.year - birthday.year - ((reference_date.month, reference_date.day) < (birthday.month, birthday.day))

# API를 통해 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '40aba2698edb26d1e441c72a37a81982'

deposit_products = []
saving_products = []

params = {
    'auth': API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': 1,
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
deposits = response.get('result').get('baseList')  # 상품 목록

for product in deposits:
    deposit_products.append({
        'code': product['fin_prdt_cd'],
        'name': product['fin_prdt_nm']
    })

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
savings = response.get('result').get('baseList')  # 상품 목록

for product in savings:
    saving_products.append({
        'code': product['fin_prdt_cd'],
        'name': product['fin_prdt_nm']
    })

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = 'django-project/accounts/fixtures/accounts/user_data.json'
data = []

# User 데이터 생성
for i in range(N):
    birthday = random_date(datetime(1920, 1, 1), datetime(2020, 1, 1))
    age = calculate_age(birthday, date.today())

    user_record = OrderedDict({
        'model': 'accounts.User',
        'pk': username_list[i],  # username이 primary key
        'fields': {
            'username': username_list[i],
            'gender': random.choice(["남성", "여성"]),
            'age': age,
            'birthday': birthday.strftime('%Y-%m-%d'),
            'salary': random.randrange(0, 1500000000, 1000000),
            'asset': random.randrange(0, 100000000, 100000),
            'debt': random.randrange(0, 50000000, 100000),
            'is_staff': False,
            'profile_image': None,
            'password': '1234',
        }
    })
    data.append(user_record)

# JSON 데이터 저장
with open(save_dir, 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent='\t')

# UserDeposit 및 UserSaving 데이터 생성
save_related_data_dir = 'django-project/accounts/fixtures/accounts/user_related_data.json'
data = []
pk_counter = 1  # UserDeposit 및 UserSaving의 pk 시작 값

for i in range(N):
    user_deposits = [random.choice(deposit_products) for _ in range(random.randint(0, 5))]
    user_savings = [random.choice(saving_products) for _ in range(random.randint(0, 5))]

    for deposit in user_deposits:
        deposit_record = OrderedDict({
            'model': 'accounts.UserDeposit',
            'pk': pk_counter,
            'fields': {
                'user': username_list[i],  # username이 primary key
                'deposit': deposit['code'],
                'join_date': date.today().strftime('%Y-%m-%d')
            }
        })
        data.append(deposit_record)
        pk_counter += 1

    for saving in user_savings:
        saving_record = OrderedDict({
            'model': 'accounts.UserSaving',
            'pk': pk_counter,
            'fields': {
                'user': username_list[i],  # username이 primary key
                'saving': saving['code'],
                'join_date': date.today().strftime('%Y-%m-%d')
            }
        })
        data.append(saving_record)
        pk_counter += 1

# JSON 데이터 저장
with open(save_related_data_dir, 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent='\t')

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
print(f'상품 데이터 생성 완료 / 저장 위치: {save_related_data_dir}')
