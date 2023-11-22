from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CollaborativeFilteringRecommender:
    @staticmethod
    def recommend_products(user_profile, all_user_profiles):
        # 사용자 간의 유사성을 계산하는 함수
        def calculate_similarity(user1, user2):
            features = ['age', 'money', 'salary']
            data = np.array([[user1[feature], user2[feature]] for feature in features])
            similarity = cosine_similarity(data)
            return similarity[0, 1]

        # 사용자의 나이, 자산, 연봉 정보 가져오기
        user_data = [user_profile.age, user_profile.money, user_profile.salary]

        # 다른 모든 사용자들과의 유사성 계산
        similarities = [(calculate_similarity(user_data, other_user), other_user) for other_user in all_user_profiles]

        # 유사도가 높은 사용자들의 가입 상품을 추천
        similarities.sort(reverse=True, key=lambda x: x[0])

        # 상위 10명의 사용자들이 가입한 상품 추천
        top_users = similarities[:10]
        recommended_products = set()
        for similarity, other_user in top_users:
            if other_user.financial_products:
                recommended_products.update(other_user.financial_products.split(','))

        return list(recommended_products)[:10]
