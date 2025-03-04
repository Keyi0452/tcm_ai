from data.questions import questions_data
from data.recommendations import lifestyle_recommendations
from recommender.personalized_recommender import PersonalizedRecommender

class TCMConsultant:
    def __init__(self):
        self.questions = questions_data
        self.recommendations = lifestyle_recommendations  # 添加推荐数据
        self.personalized_recommender = PersonalizedRecommender(lifestyle_recommendations)  # 初始化个性化推荐系统
        self.constitution_types = {
            "平和质": {"questions": range(1, 9), "threshold": 60},
            "气虚质": {"questions": range(9, 16), "threshold": 30},
            "阳虚质": {"questions": range(16, 24), "threshold": 30},
            "阴虚质": {"questions": range(24, 32), "threshold": 30},
            "痰湿质": {"questions": range(32, 40), "threshold": 30},
            "湿热质": {"questions": range(40, 48), "threshold": 30},
            "血瘀质": {"questions": range(48, 53), "threshold": 30},
            "气郁质": {"questions": range(53, 57), "threshold": 30},
            "特禀质": {"questions": range(57, 61), "threshold": 30}
        }

    def analyze_constitution(self, answers):
        scores = {}
        
        # 计算每种体质的得分
        for type_name, type_info in self.constitution_types.items():
            total_questions = len(list(type_info["questions"]))
            type_score = 0
            for q_id in type_info["questions"]:
                if q_id in answers:
                    type_score += answers[q_id]
            
            # 转换为百分制
            scores[type_name] = (type_score / (total_questions * 5)) * 100

        # 按得分排序
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # 获取主要体质类型
        main_types = []
        highest_score = sorted_scores[0][1]
        
        # 检查是否有体质超过阈值
        has_valid_constitution = False
        for type_name, score in sorted_scores:
            if score >= self.constitution_types[type_name]["threshold"]:
                has_valid_constitution = True
                if score >= highest_score - 5:
                    main_types.append((type_name, score))

        # 如果没有体质超过阈值，则判定为平和质
        if not has_valid_constitution:
            return [("平和质", scores["平和质"])]

        return main_types

    def provide_recommendations(self, constitution_results):
        print("\n体质测试结果：")
        for type_name, score in constitution_results:
            print(f"{type_name}: {score:.1f}分")
        
        # 确保至少有一个主要体质类型
        if not constitution_results:
            print("\n未能确定明显的体质倾向，建议重新测试。")
            return
            
        # 获取最高分的体质类型
        main_type, highest_score = constitution_results[0]
        
        print(f"\n=== 主要体质倾向：{main_type} ({highest_score:.1f}分) ===")
        if main_type in self.recommendations:
            self._display_type_recommendations(main_type, self.recommendations[main_type])
        
        # 只有当第二名体质分数接近最高分（差距在5分以内）时才显示
        if len(constitution_results) > 1:
            second_type, second_score = constitution_results[1]
            if highest_score - second_score <= 5:
                print(f"\n=== 次要体质倾向：{second_type} ({second_score:.1f}分) ===")
                if second_type in self.recommendations:
                    self._display_type_recommendations(second_type, self.recommendations[second_type])
        
        print("\n主要体质倾向：")
        for type_name, score in constitution_results[:2]:
            print(f"\n=== {type_name} ===")
            if type_name in self.recommendations:  # 修改这里
                rec = self.recommendations[type_name]  # 使用实例变量
                print(f"\n【体质说明】")
                print(rec["description"])
                
                # 添加饮食建议
                diet = rec.get("diet_advice", {})
                print("\n【饮食建议】")
                print("适宜食物：")
                for food in diet.get("suitable_foods", []):
                    print(f"- {food}")
                
                print("\n饮食习惯：")
                for habit in diet.get("eating_habits", []):
                    print(f"- {habit}")
                
                # 添加运动建议
                exercise = rec.get("exercise_advice", {})
                print("\n【运动建议】")
                for ex in exercise.get("recommended_exercises", []):
                    print(f"\n{ex['type']}:")
                    print(f"- 推荐项目：{', '.join(ex['items'])}")
                    print(f"- 持续时间：{ex['duration']}")
                    print(f"- 频率：{ex['frequency']}")
                
                # 添加情志调养
                emotion = rec.get("emotional_care", {})
                print("\n【情志调养】")
                print("日常管理：")
                for item in emotion.get("daily_management", []):
                    print(f"- {item}")
                
                # 添加茶饮建议
                tea = rec.get("herbal_tea", {})
                print("\n【养生茶饮】")
                for recipe in tea.get("daily_recipes", []):
                    print(f"\n{recipe['name']}:")
                    print("配料：")
                    for ing in recipe["ingredients"]:
                        print(f"- {ing['name']} {ing['amount']}")
                    print(f"泡制方法：{recipe['brewing']}")
                    print(f"饮用时间：{recipe['drinking_time']}")
                
                # 添加穴位保健
                acupoint = rec.get("acupoint_care", {})
                print("\n【穴位保健】")
                for point in acupoint.get("daily_points", []):
                    print(f"\n{point['name']}:")
                    print(f"位置：{point['location']}")
                    print(f"方法：{point['method']}")
                    print(f"时间：{point['timing']}")
                    print(f"功效：{point['benefits']}")
                
                print("\n" + "="*50)

        print("\n调理建议：")
        # ... 后续添加具体的调理建议 ...

        # 在显示完基本建议后，添加个性化推荐部分
        print("\n=== 个性化调理建议 ===")
        
        # 转换体质测试结果为分数字典
        scores = {type_name: score for type_name, score in constitution_results}
        
        # 收集用户个人信息
        user_info = self._collect_user_info()
        
        # 获取个性化建议
        personalized_advice = self.personalized_recommender.get_personalized_advice(
            scores,
            user_info
        )
        
        # 显示个性化建议
        self._display_personalized_advice(personalized_advice)

    def _collect_user_info(self):
        """收集用户个人信息"""
        print("\n为了提供更精准的个性化建议，请提供一些基本信息：")
        
        user_info = {}
        
        try:
            user_info["age"] = int(input("请输入您的年龄："))
            user_info["gender"] = input("请输入您的性别（男/女）：")
            
            # 收集过敏信息
            allergies = input("请输入您的过敏源（多个请用逗号分隔，如：花生,海鲜）：")
            user_info["allergies"] = [item.strip() for item in allergies.split(",") if item.strip()]
            
            # 收集运动偏好
            exercise_pref = input("您喜欢的运动类型（多个请用逗号分隔，如：瑜伽,散步）：")
            user_info["preferences"] = {
                "exercise": [item.strip() for item in exercise_pref.split(",") if item.strip()]
            }
            
        except ValueError:
            print("输入格式有误，将使用默认推荐")
            return {}
            
        return user_info

    def _display_personalized_advice(self, advice):
        """显示个性化建议"""
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

    def start_consultation(self):
        print("欢迎使用中医体质辨识系统")
        print("免责声明：本系统仅供参考，不作为医疗诊断依据。如有不适请及时就医。")
        
        answers = self.collect_answers()
        constitution = self.analyze_constitution(answers)
        self.provide_recommendations(constitution)

    def collect_answers(self):
        answers = {}
        for question in self.questions:
            print(f"\n{question['content']}")
            for i, option in enumerate(question['options'], 1):
                print(f"{i}. {option}")
            
            while True:
                try:
                    answer = int(input("请选择（1-5）: "))
                    if 1 <= answer <= 5:
                        answers[question['id']] = answer
                        break
                    print("请输入1-5之间的数字")
                except ValueError:
                    print("请输入有效的数字")
        return answers

    def _display_type_recommendations(self, type_name, rec):
        """显示特定体质类型的建议"""
        print(f"\n【体质说明】")
        print(rec["description"])
        
        # 添加饮食建议
        diet = rec.get("diet_advice", {})
        print("\n【饮食建议】")
        print("适宜食物：")
        for food in diet.get("suitable_foods", []):
            print(f"- {food}")
        
        print("\n饮食习惯：")
        for habit in diet.get("eating_habits", []):
            print(f"- {habit}")
        
        # 添加运动建议
        exercise = rec.get("exercise_advice", {})
        print("\n【运动建议】")
        for ex in exercise.get("recommended_exercises", []):
            print(f"\n{ex['type']}:")
            print(f"- 推荐项目：{', '.join(ex['items'])}")
            print(f"- 持续时间：{ex['duration']}")
            print(f"- 频率：{ex['frequency']}")
        
        # 添加情志调养
        emotion = rec.get("emotional_care", {})
        print("\n【情志调养】")
        print("日常管理：")
        for item in emotion.get("daily_management", []):
            print(f"- {item}")
        
        # 添加茶饮建议
        tea = rec.get("herbal_tea", {})
        print("\n【养生茶饮】")
        for recipe in tea.get("daily_recipes", []):
            print(f"\n{recipe['name']}:")
            print("配料：")
            for ing in recipe["ingredients"]:
                print(f"- {ing['name']} {ing['amount']}")
            print(f"泡制方法：{recipe['brewing']}")
            print(f"饮用时间：{recipe['drinking_time']}")
        
        # 添加穴位保健
        acupoint = rec.get("acupoint_care", {})
        print("\n【穴位保健】")
        for point in acupoint.get("daily_points", []):
            print(f"\n{point['name']}:")
            print(f"位置：{point['location']}")
            print(f"方法：{point['method']}")
            print(f"时间：{point['timing']}")
            print(f"功效：{point['benefits']}")
        
        print("\n" + "="*50)

def main():
    consultant = TCMConsultant()
    consultant.start_consultation()

if __name__ == "__main__":
    main()