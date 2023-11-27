from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from collections import Counter

class CollaborativeFilteringRecommender:
    @staticmethod
    def recommend_products(user_profile, all_user_profiles):
        # 사용자 간의 유사성을 계산하는 함수
        def calculate_similarity(user1, user2):
            features = ['age', 'money', 'salary']
            
            # Replace None values with 0
            data = np.array([[getattr(user1, feature) if getattr(user1, feature) is not None else 0,
                            getattr(user2, feature) if getattr(user2, feature) is not None else 0] for feature in features])

            # Replace NaN values with the mean of the column
            data = np.nan_to_num(data, nan=np.nanmean(data, axis=0))

            similarity = cosine_similarity(data)
            return similarity[0, 1]



        # 사용자의 나이, 자산, 연봉 정보 가져오기
        user_data = [user_profile.age, user_profile.money, user_profile.salary]

        # 다른 모든 사용자들과의 유사성 계산
        similarities = [(calculate_similarity(user_profile, other_user), other_user) for other_user in all_user_profiles]

        # 유사도가 높은 사용자들의 가입 상품을 추천
        similarities.sort(reverse=True, key=lambda x: x[0])

        # 상위 10명의 사용자들이 가입한 상품 추천
        top_users = similarities[:10]
        recommended_products = set()
        for similarity, other_user in top_users:
            if other_user.financial_products:
                recommended_products.update(other_user.financial_products.split(','))

        return list(recommended_products)[:10]


class MBTIRecommender:
    @staticmethod
    def recommend_products(user, all_users):
        # 사용자의 MBTI
        user_mbti = user.mbti
        
        # 같은 MBTI를 가진 사용자들의 금융 상품 목록을 수집
        mbti_users = [other_user for other_user in all_users if other_user.mbti == user_mbti]
        mbti_products = [product for other_user in mbti_users for product in (other_user.financial_products.split(',') if other_user.financial_products else []) if product]

        # 상품별 선택 횟수를 계산
        product_counts = Counter(mbti_products)

        # 가장 많이 선택된 상품 순으로 상위 10개의 상품 코드만 추출
        recommended_products = [product[0] for product in product_counts.most_common(10)]

        return recommended_products