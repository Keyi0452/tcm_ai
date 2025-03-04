from recommender.personalized_recommender import PersonalizedRecommender
from data.recommendations import lifestyle_recommendations

def get_personalized_recommendations():
    # 实例化推荐系统
    recommender = PersonalizedRecommender(lifestyle_recommendations)
    
    # 测试数据
    constitution_scores = {
        "气虚质": 65.7,
        "阳虚质": 65.0,
        "血瘀质": 64.0
    }
    
    # 用户信息
    user_info = {
        "age": 35,
        "gender": "female",
        "location": "北京",
        "allergies": ["花生", "海鲜"],
        "preferences": {
            "exercise": ["瑜伽", "散步"],
            "diet": ["素食为主"]
        }
    }
    
    # 获取个性化建议
    recommendations = recommender.get_personalized_advice(
        constitution_scores,
        user_info
    )
    
    return recommendations

if __name__ == "__main__":
    recommendations = get_personalized_recommendations()
    print(json.dumps(recommendations, ensure_ascii=False, indent=2))