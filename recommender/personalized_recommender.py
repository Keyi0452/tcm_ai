from datetime import datetime
import json
from models.user_profile import UserProfile

class PersonalizedRecommender:
    def __init__(self, recommendations_data):
        self.base_recommendations = recommendations_data
        
    def get_personalized_advice(self, constitution_scores, user_info):
        # 添加调试日志
        print("Input constitution scores:", constitution_scores)
        print("User info:", user_info)
        
        main_constitution = max(constitution_scores.items(), key=lambda x: x[1])[0]
        base_advice = self.base_recommendations.get(main_constitution, {})  # 修正这里
        
        # 检查基础建议内容
        print("Base advice keys:", list(base_advice.keys()))
        
        # 确保所有建议类型都被包含
        advice = {
            "daily_routines": base_advice.get("daily_routines", []),
            "emotional_care": base_advice.get("emotional_care", {}),
            "exercise_advice": base_advice.get("exercise_advice", {}),
            "diet_advice": base_advice.get("diet_advice", {}),
            "herbal_tea": base_advice.get("herbal_tea", {}),
            "acupoint_care": base_advice.get("acupoint_care", {})
        }
        
        return advice
        """
        根据体质测试分数和用户信息生成个性化建议
        """
        # 获取主要体质（分数最高的）
        main_constitution = max(constitution_scores.items(), key=lambda x: x[1])[0]
        base_advice = self.base_recommendations.get(main_constitution, {})
        
        # 创建个性化建议
        personalized_advice = {
            "exercise_advice": self._customize_exercise(base_advice.get("exercise_advice", {}), user_info),  # 添加下划线
            "diet_advice": self._customize_diet(base_advice.get("diet_advice", {}), user_info),
            "seasonal_tips": self._get_seasonal_tips(base_advice),
            "personalized_schedule": self._create_daily_schedule(user_info)
        }
        
        return personalized_advice

    # 修改方法名，添加下划线
    def _customize_exercise(self, exercise_advice, user_info):
        """根据用户信息调整运动建议"""
        if not user_info:
            return exercise_advice
            
        customized = exercise_advice.copy()
        recommended_exercises = customized.get("recommended_exercises", [])
        
        # 根据年龄调整运动时长
        if "age" in user_info:
            age = user_info["age"]
            if age >= 60:
                for exercise in recommended_exercises:
                    if "duration" in exercise:
                        duration = exercise["duration"]
                        if "-" in duration:
                            min_time, max_time = map(int, duration.replace("分钟", "").split("-"))
                            exercise["duration"] = f"{int(min_time*0.7)}-{int(max_time*0.7)}分钟"
        
        # 根据用户偏好调整运动项目
        if "preferences" in user_info and "exercise" in user_info["preferences"]:
            preferred = user_info["preferences"]["exercise"]
            # 将用户喜欢的运动项目排在前面
            recommended_exercises.sort(
                key=lambda x: any(pref in x["items"] for pref in preferred),
                reverse=True
            )
            
        return customized
    
    def _customize_diet(self, diet_advice, user_info):
        """根据用户信息调整饮食建议"""
        if not user_info:
            return diet_advice
            
        customized = diet_advice.copy()
        
        # 过滤过敏食物
        if "allergies" in user_info and user_info["allergies"]:
            suitable_foods = customized.get("suitable_foods", [])
            filtered_foods = [
                food for food in suitable_foods
                if not any(allergen in food for allergen in user_info["allergies"])
            ]
            customized["suitable_foods"] = filtered_foods
            
        return customized
    
    def _get_seasonal_tips(self, base_advice):
        """获取季节性建议"""
        current_season = self._get_current_season()
        
        # 定义季节性建议
        seasonal_tips = {
            "spring": "春季养生要注意保暖，适当运动，饮食清淡",
            "summer": "夏季注意防暑降温，多饮水，适当运动",
            "autumn": "秋季养生要注意保湿，适当补充营养",
            "winter": "冬季要注意保暖，适当进补，保持运动"
        }
        
        # 获取当前季节的建议
        current_tip = seasonal_tips.get(current_season, "")
        
        # 如果基础建议中有季节性调整，则合并建议
        if base_advice and "seasonal_adjustments" in base_advice:
            base_seasonal = base_advice["seasonal_adjustments"].get(current_season, "")
            if base_seasonal:
                current_tip = f"{current_tip}；{base_seasonal}"
                
        return current_tip
    
    def _get_current_season(self):
        """获取当前季节"""
        month = datetime.now().month
        if month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        elif month in [9, 10, 11]:
            return "autumn"
        else:
            return "winter"
    
    def create_daily_schedule(self, user_info):
        """创建个性化作息建议"""
        schedule = {
            "morning": [
                "晨起温水",
                "适量运动",
                "营养早餐"
            ],
            "noon": [
                "午餐细嚼慢咽",
                "适度午休",
                "喝养生茶"
            ],
            "evening": [
                "适量运动",
                "清淡晚餐",
                "早睡保养"
            ]
        }
        
        # 根据年龄调整作息
        if user_info and "age" in user_info:
            age = user_info["age"]
            if age >= 60:
                schedule["morning"].append("太极或八段锦")
                schedule["noon"].append("午休时间延长至1小时")
                schedule["evening"].append("睡前按摩穴位")
                
        return schedule
    
    def get_season(self):
        month = datetime.now().month
        if month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        elif month in [9, 10, 11]:
            return "autumn"
        else:
            return "winter"
    
    def customize_recommendations(self, user_profile: UserProfile):
        main_constitution = user_profile.main_constitution
        base_advice = self.base_recommendations.get(main_constitution, {})
        
        # 根据用户年龄调整运动建议
        customized_exercise = self._adjust_exercise_by_age(
            base_advice.get("exercise_advice", {}),
            user_profile.age
        )
        
        # 根据季节调整饮食和茶饮建议
        current_season = self.get_season()
        customized_diet = self._adjust_diet_by_season(
            base_advice.get("diet_advice", {}),
            current_season
        )
        
        # 考虑用户过敏情况
        customized_diet = self._filter_allergies(
            customized_diet,
            user_profile.allergies
        )
        
        return {
            "exercise_advice": customized_exercise,
            "diet_advice": customized_diet,
            "seasonal_tips": self._get_seasonal_tips(current_season),
            "personalized_schedule": self._create_daily_schedule(user_profile)
        }
    
    def _adjust_exercise_by_age(self, exercise_advice, age):
        if age >= 60:
            # 调整运动强度和时长
            adjusted_advice = exercise_advice.copy()
            for exercise in adjusted_advice.get("recommended_exercises", []):
                exercise["duration"] = self._reduce_duration(exercise["duration"])
            return adjusted_advice
        return exercise_advice
    
    def _reduce_duration(self, duration):
        # 将运动时间减少 30%
        if "-" in duration:
            min_time, max_time = map(lambda x: int(x.replace("分钟", "")), 
                                   duration.split("-"))
            new_min = int(min_time * 0.7)
            new_max = int(max_time * 0.7)
            return f"{new_min}-{new_max}分钟"
        return duration
    
    def _adjust_diet_by_season(self, diet_advice, season):
        seasonal_adjustments = {
            "spring": ["芽菜", "青菜", "花草茶"],
            "summer": ["苦瓜", "绿豆", "薄荷"],
            "autumn": ["山药", "梨", "银耳"],
            "winter": ["生姜", "羊肉", "红枣"]
        }
        
        adjusted_diet = diet_advice.copy()
        seasonal_foods = seasonal_adjustments.get(season, [])
        if "suitable_foods" in adjusted_diet:
            adjusted_diet["suitable_foods"].extend(seasonal_foods)
        
        return adjusted_diet
    
    def _filter_allergies(self, diet_advice, allergies):
        if not allergies:
            return diet_advice
            
        filtered_diet = diet_advice.copy()
        if "suitable_foods" in filtered_diet:
            filtered_diet["suitable_foods"] = [
                food for food in filtered_diet["suitable_foods"]
                if not any(allergen in food for allergen in allergies)
            ]
        return filtered_diet
    
    
    def _create_daily_schedule(self, user_profile):
        # 创建个性化作息建议
        return {
            "morning": [
                "晨起喝温水",
                "进行15分钟八段锦",
                "营养早餐"
            ],
            "noon": [
                "适量运动",
                "清淡午餐",
                "午休20分钟"
            ],
            "evening": [
                "晚餐后散步",
                "按摩保健穴位",
                "泡养生茶"
            ]
        }

    def _adjust_by_location(self, advice, city):
        # 根据城市名称获取所属区域
        north_cities = ["北京", "天津", "沈阳", "长春", "哈尔滨"]
        south_cities = ["广州", "深圳", "厦门", "海口", "南宁"]
        east_cities = ["上海", "杭州", "南京", "苏州", "宁波"]
        west_cities = ["成都", "重庆", "昆明", "西安", "兰州"]
        
        # 根据城市特点调整建议
        if city in north_cities:
            # 北方城市调整
            self._adjust_for_north(advice)
        elif city in south_cities:
            # 南方城市调整
            self._adjust_for_south(advice)
        elif city in east_cities:
            # 东部城市调整
            self._adjust_for_east(advice)
        elif city in west_cities:
            # 西部城市调整
            self._adjust_for_west(advice)
        
        return advice
    
    def _adjust_for_north(self, advice):
        # 北方地区的调整建议
        if "diet_advice" in advice:
            advice["diet_advice"].setdefault("regional_recommendations", []).extend([
                "多食用温热性食物",
                "注意防寒保暖",
                "适当增加热量摄入"
            ])
        
        if "exercise_advice" in advice:
            advice["exercise_advice"].setdefault("regional_notes", []).extend([
                "冬季注意室内运动为主",
                "户外运动需要充分防寒",
                "避免在寒冷天气剧烈运动"
            ])

    def _adjust_for_south(self, advice):
        # 南方地区的调整建议
        if "diet_advice" in advice:
            advice["diet_advice"].setdefault("regional_recommendations", []).extend([
                "多食用温热性食物",
                "注意防寒保暖",
                "适当增加热量摄入"
            ])
        
        if "exercise_advice" in advice:
            advice["exercise_advice"].setdefault("regional_notes", []).extend([
                "冬季注意室内运动为主",
                "户外运动需要充分防寒",
                "避免在寒冷天气剧烈运动"
            ])

    def _adjust_for_east(self, advice):
        # 东部地区的调整建议
        if "diet_advice" in advice:
            advice["diet_advice"].setdefault("regional_recommendations", []).extend([
                "多食用温热性食物",
                "注意防寒保暖",
                "适当增加热量摄入"
            ])
        
        if "exercise_advice" in advice:
            advice["exercise_advice"].setdefault("regional_notes", []).extend([
                "冬季注意室内运动为主",
                "户外运动需要充分防寒",
                "避免在寒冷天气剧烈运动"
            ])

    def _adjust_for_west(self, advice):
        # 西部地区的调整建议
        if "diet_advice" in advice:
            advice["diet_advice"].setdefault("regional_recommendations", []).extend([
                "多食用温热性食物",
                "注意防寒保暖",
                "适当增加热量摄入"
            ])
        
        if "exercise_advice" in advice:
            advice["exercise_advice"].setdefault("regional_notes", []).extend([
                "冬季注意室内运动为主",
                "户外运动需要充分防寒",
                "避免在寒冷天气剧烈运动"
            ])