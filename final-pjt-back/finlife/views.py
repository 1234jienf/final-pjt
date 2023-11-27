from django.shortcuts import render
from django.db.models import Max
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer, BankSerializer
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions, Bank


# Create your views here.
@api_view(['GET'])
def d_index(request):
    api_key = settings.API_KEY

    d_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    d_response = requests.get(d_url).json()

    for li in d_response.get("result").get("baseList"):
        save_product_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_deny' :li.get('join_deny'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }
        bank_data = {'name': li.get('kor_co_nm')}
        
        serializer_b = BankSerializer(data=bank_data)

        if DepositProducts.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            continue
        else:
            serializer_p = DepositProductsSerializer(data=save_product_data)
            if serializer_p.is_valid(raise_exception=True):
                serializer_p.save()
    
        if serializer_b.is_valid(raise_exception=True):
            try:
                bank = Bank.objects.get_or_create(name=serializer_b.validated_data['name'])
            except Bank.DoesNotExist:
                bank = serializer_b.save()
    for li in d_response.get("result").get("optionList"):
        save_option_data = {
            'dcls_month': li.get('dcls_month'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate' : li.get('intr_rate') or -1,
            'intr_rate2' :li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }

        if DepositOptions.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd'), save_trm=li.get('save_trm')).exists():
            continue
        else:
            serializer_o = DepositOptionsSerializer(data=save_option_data)
            if serializer_o.is_valid(raise_exception=True):
                product = DepositProducts.objects.filter(fin_prdt_cd=save_option_data.get('fin_prdt_cd')).first()
                serializer_o.save(product=product)

    products = DepositOptions.objects.all()
    serializer = DepositOptionsSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def s_index(request):
    api_key = settings.API_KEY

    s_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    s_response = requests.get(s_url).json()

    for li in s_response.get("result").get("baseList"):
        save_product_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'dcls_month': li.get('dcls_month'),
            'kor_co_nm': li.get('kor_co_nm'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'join_deny' :li.get('join_deny'),
            'join_way' : li.get('join_way'),
            'spcl_cnd' : li.get('spcl_cnd'),
        }

        if SavingProducts.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            continue
        else:
            serializer_p = SavingProductsSerializer(data=save_product_data)
            if serializer_p.is_valid(raise_exception=True):
                serializer_p.save()

    for li in s_response.get("result").get("optionList"):
        save_option_data = {
            'dcls_month': li.get('dcls_month'),
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'intr_rate_type_nm': li.get('intr_rate_type_nm'),
            'intr_rate' : li.get('intr_rate') or -1,
            'intr_rate2' :li.get('intr_rate2'),
            'save_trm' : li.get('save_trm'),
        }

        if SavingOptions.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd'), save_trm=li.get('save_trm')).exists():
            continue
        else:
            serializer_o = SavingOptionsSerializer(data=save_option_data)
            if serializer_o.is_valid(raise_exception=True):
                product = SavingProducts.objects.filter(fin_prdt_cd=save_option_data.get('fin_prdt_cd')).first()
                serializer_o.save(product=product)

    products = SavingOptions.objects.all()
    serializer = SavingOptionsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositProductsSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def saving_detail(request, fin_prdt_cd):
    product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingProductsSerializer(product)
    return Response(serializer.data)


# 필터링된 예금 정보
@api_view(['GET'])
def deposit_sort(request, sort_num1, sort_num2=None):

    bank = Bank.objects.get(id=sort_num1)
    d_list = []

    deposit_products = DepositProducts.objects.filter(kor_co_nm=bank)
    products = DepositOptions.objects.filter(product__in=deposit_products)

    if sort_num2:
        if sort_num2 in [6, 12, 24, 36]:
            products = products.filter(save_trm=sort_num2)
        else:
            return Response([{"message": "검색조건에 해당하는 상품이 없습니다."}])
    serializer = DepositOptionsSerializer(products, many=True)
    d_list.extend(serializer.data)
    return Response(d_list)


# 필터링된 적금 정보
@api_view(['GET'])
def saving_sort(request, sort_num1, sort_num2=None):

    bank = Bank.objects.get(id=sort_num1)
    s_list = []

    saving_products = SavingProducts.objects.filter(kor_co_nm=bank)
    products = SavingOptions.objects.filter(product__in=saving_products)

    if sort_num2:
        if sort_num2 in [6, 12, 24, 36]:
            products = products.filter(save_trm=sort_num2)
        else:
            return Response([{"message": "검색조건에 해당하는 상품이 없습니다."}])
    serializer = SavingOptionsSerializer(products, many=True)
    s_list.extend(serializer.data)
    return Response(s_list)