from data.recommendations import lifestyle_recommendations
from recommender.personalized_recommender import PersonalizedRecommender

def test_personalized_recommendations():
    # 初始化推荐系统
    recommender = PersonalizedRecommender(lifestyle_recommendations)
    
    # 模拟体质测试结果（分数）
    test_scores = {
        "气虚质": 75,
        "阳虚质": 45,
        "阴虚质": 30,
        "痰湿质": 25,
        "湿热质": 20,
        "血瘀质": 15,
        "气郁质": 10,
        "特禀质": 5,
        "平和质": 40
    }
    
    # 模拟用户信息
    test_user_info = {
        "age": 30,
        "gender": "女",
        "allergies": ["花粉", "海鲜"],
        "preferences": {
            "exercise": ["瑜伽", "散步", "游泳"]
        }
    }
    
    # 获取个性化建议
    advice = recommender.get_personalized_advice(test_scores, test_user_info)
    
    # 打印建议
    print("\n=== 个性化调理建议 ===")
    
    print("\n【个性化运动建议】")
    if "exercise_advice" in advice:
        for exercise in advice["exercise_advice"].get("recommended_exercises", []):
            print(f"\n{exercise['type']}:")
            print(f"- 推荐项目：{', '.join(exercise['items'])}")
            print(f"- 建议时长：{exercise['duration']}")
            print(f"- 运动频率：{exercise['frequency']}")

    print("\n【个性化饮食建议】")
    if "diet_advice" in advice:
        print("\n适宜食物：")
        for food in advice["diet_advice"].get("suitable_foods", []):
            print(f"- {food}")

    print("\n【季节性调养建议】")
    if "seasonal_tips" in advice:
        print(advice["seasonal_tips"])

    print("\n【每日作息建议】")
    if "personalized_schedule" in advice:
        schedule = advice["personalized_schedule"]
        for time, activities in schedule.items():
            print(f"\n{time}:")
            for activity in activities:
                print(f"- {activity}")

if __name__ == "__main__":
    test_personalized_recommendations()