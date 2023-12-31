from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from finlife.models import DepositOptions, SavingOptions
from .models import User
from .serializers import UserSerializer
from .recommend import CollaborativeFilteringRecommender, MBTIRecommender

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_chart(request):
    user = request.user
    if user.financial_products:
        financial_products = user.financial_products.split(',')
        saving_rates = []
        max_rates = []
        fin_prdt_nms = []
        # print(type(financial_products))
        for product_code in financial_products:
            # print(product_code)
            d_options = DepositOptions.objects.filter(fin_prdt_cd=product_code).first()
            s_options = SavingOptions.objects.filter(fin_prdt_cd=product_code).first()
            # print(f'd_options: {d_options}')
            # print(f's_options: {s_options}')
            if d_options:
                # for deposit_option in d_options:
                saving_rates.append(d_options.intr_rate)
                max_rates.append(d_options.intr_rate2)
                fin_prdt_nms.append(d_options.product.fin_prdt_nm)
            if s_options:
                # for saving_option in s_options:
                saving_rates.append(s_options.intr_rate)
                max_rates.append(s_options.intr_rate2)
                fin_prdt_nms.append(s_options.product.fin_prdt_nm)
                # print(s_options.product.fin_prdt_nm)

            
        average_saving_rate = sum(saving_rates) / len(saving_rates) if saving_rates else 0
        average_max_rate = sum(max_rates) / len(max_rates) if max_rates else 0

        return JsonResponse({
            'saving_rates': saving_rates,
            'max_rates': max_rates,
            'average_saving_rate': average_saving_rate,
            'average_max_rate': average_max_rate,
            'fin_prdt_nms': fin_prdt_nms
        })
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_products(request):
    user_profile = request.user
    if user_profile.money:
        if user_profile.salary:
            if user_profile.age:
                all_user_profiles = User.objects.exclude(id=user_profile.id)

                recommender = CollaborativeFilteringRecommender()
                recommended_products = recommender.recommend_products(user_profile, all_user_profiles)
                # print(recommended_products)
                serializer = UserSerializer(user_profile)
                companies = []
                pd_names = []
                for product_code in recommended_products:
                    # print(product_code)
                    d_options = DepositOptions.objects.filter(fin_prdt_cd=product_code).first()
                    s_options = SavingOptions.objects.filter(fin_prdt_cd=product_code).first()
                    if d_options:
                        # for deposit_option in d_options:
                        companies.append(d_options.product.kor_co_nm)
                        pd_names.append(d_options.product.fin_prdt_nm)
                    if s_options:
                        # for saving_option in s_options:
                        companies.append(s_options.product.kor_co_nm)
                        pd_names.append(s_options.product.fin_prdt_nm)
                        # print(s_options.product.fin_prdt_nm)
                data = {
                    'recommended_products': recommended_products,
                    'companies': companies,
                    'pd_names': pd_names
                }
                # print(data)
                return Response(data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mbti_recommend(request):
    user_profile = request.user
    if user_profile.mbti:
        all_user_profiles = User.objects.exclude(id=user_profile.id)

        recommender = MBTIRecommender()
        recommended_products = recommender.recommend_products(user_profile, all_user_profiles)

        serializer = UserSerializer(user_profile)
        companies = []
        pd_names = []

        for product_code in recommended_products:
            d_options = DepositOptions.objects.filter(fin_prdt_cd=product_code).first()
            s_options = SavingOptions.objects.filter(fin_prdt_cd=product_code).first()

            if d_options:
                companies.append(d_options.product.kor_co_nm)
                pd_names.append(d_options.product.fin_prdt_nm)

            if s_options:
                companies.append(s_options.product.kor_co_nm)
                pd_names.append(s_options.product.fin_prdt_nm)

        data = {
            'mbti': user_profile.mbti,
            'recommended_products': recommended_products,
            'companies': companies,
            'pd_names': pd_names
        }

        return Response(data)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)