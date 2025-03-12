from typing import Dict, List

class ConstitutionScore:
    def __init__(self):
        self.scores = {
            "平和质": 0,
            "气虚质": 0,
            "阳虚质": 0,
            "阴虚质": 0,
            "痰湿质": 0,
            "湿热质": 0,
            "血瘀质": 0,
            "气郁质": 0,
            "特禀质": 0
        }
        
    def calculate_scores(self, answers: Dict[int, int]) -> Dict[str, float]:
        for question_id, score in answers.items():
            question = questions_data["questions"][question_id - 1]
            constitution_type = question["constitution_type"]
            self.scores[constitution_type] += score
            
        for constitution_type in self.scores:
            total_questions = len([q for q in questions_data["questions"] 
                                if q["constitution_type"] == constitution_type])
            if total_questions > 0:
                self.scores[constitution_type] = (self.scores[constitution_type] / 
                                                (total_questions * 5)) * 100
        
        return self.scores

    def determine_constitution(self) -> List[str]:
        constitutions = []
        
        if (self.scores["平和质"] >= 60 and
            all(self.scores[t] < 30 for t in self.scores if t != "平和质")):
            return ["平和质"]
            
        for constitution_type, score in self.scores.items():
            if constitution_type != "平和质" and score >= 40:
                constitutions.append(constitution_type)
        
        return constitutions if constitutions else ["平和质"]

questions_data = {
    "title": "中医体质辨识问卷",
    "description": "基于《中医体质分类与判定》标准",
    "questions": [
        # 平和质相关问题 (1-8)
        {
            "id": 1,
            "question": "您精力充沛吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 2,
            "question": "您容易入睡吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 3,
            "question": "您睡眠质量好吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 4,
            "question": "您容易醒吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 5,
            "question": "您白天精神好吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 6,
            "question": "您说话声音洪亮吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 7,
            "question": "您能适应气候和环境的变化吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },
        {
            "id": 8,
            "question": "您性格乐观开朗吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "平和质"
        },

        # 气虚质相关问题 (9-15)
        {
            "id": 9,
            "question": "您容易疲劳吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 10,
            "question": "您容易气短，呼吸急促吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 11,
            "question": "您说话声音低弱无力吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 12,
            "question": "您活动量稍大就容易出虚汗吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 13,
            "question": "您容易患感冒吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 14,
            "question": "您平时容易腹泻吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },
        {
            "id": 15,
            "question": "您舌头边上有齿痕吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气虚质"
        },

        # 阳虚质相关问题 (16-23)
        {
            "id": 16,
            "question": "您手脚发凉吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 17,
            "question": "您胃脘部、背部或腰膝部怕冷吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 18,
            "question": "您感到怕冷、衣服比别人穿得多吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 19,
            "question": "您比一般人耐受不了寒冷吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 20,
            "question": "您喜欢热饮吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 21,
            "question": "您大便稀溏吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 22,
            "question": "您小便清长吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },
        {
            "id": 23,
            "question": "您面色白或萎黄吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阳虚质"
        },

        # 阴虚质相关问题 (24-31)
        {
            "id": 24,
            "question": "您感到手脚心发热吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 25,
            "question": "您感到口干吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 26,
            "question": "您感到眼睛干涩吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 27,
            "question": "您感到咽喉干燥吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 28,
            "question": "您皮肤干燥吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 29,
            "question": "您便秘或大便干燥吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 30,
            "question": "您面部或颧部有潮红吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },
        {
            "id": 31,
            "question": "您感到身体瘦弱或容易瘦吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "阴虚质"
        },

        # 痰湿质相关问题 (32-39)
        {
            "id": 32,
            "question": "您感到胸闷或腹部胀满吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 33,
            "question": "您感到身体沉重不轻松吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 34,
            "question": "您腹部肥满松软吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 35,
            "question": "您有痰或痰多吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 36,
            "question": "您口中有黏黏的感觉吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },

        # 继续痰湿质相关问题
        {
            "id": 37,
            "question": "您感到口中有异味吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 38,
            "question": "您大便黏滞不爽、有不完全感吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },
        {
            "id": 39,
            "question": "您舌苔厚腻吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "痰湿质"
        },

        # 湿热质相关问题 (40-47)
        {
            "id": 40,
            "question": "您面部或鼻部有油腻感吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 41,
            "question": "您感到口苦或嘴里有异味吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 42,
            "question": "您大便黏滞不爽、有不完全感吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 43,
            "question": "您小便浓茶色或者发黄吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 44,
            "question": "您带下色黄（白带颜色发黄）吗？（限女性回答）",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 45,
            "question": "您容易生痤疮或疮疖吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 46,
            "question": "您感到口干咽燥、总想喝水吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },
        {
            "id": 47,
            "question": "您感到身体沉重不轻松，或者疲乏无力吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "湿热质"
        },

        # 血瘀质相关问题 (48-52)
        {
            "id": 48,
            "question": "您面部或鼻唇部有细微红丝吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "血瘀质"
        },
        {
            "id": 49,
            "question": "您两颧部有细微红丝吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "血瘀质"
        },
        {
            "id": 50,
            "question": "您身上有青紫瘀斑吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "血瘀质"
        },
        {
            "id": 51,
            "question": "您容易有黑眼圈吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "血瘀质"
        },
        {
            "id": 52,
            "question": "您口唇颜色偏暗吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "血瘀质"
        },

        # 气郁质相关问题 (53-56)
        {
            "id": 53,
            "question": "您感到闷闷不乐、情绪低沉吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气郁质"
        },
        {
            "id": 54,
            "question": "您容易感到害怕或受到惊吓吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气郁质"
        },
        {
            "id": 55,
            "question": "您容易感到心烦吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气郁质"
        },
        {
            "id": 56,
            "question": "您容易感到胸闷或胸胁胀满吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "气郁质"
        },

        # 特禀质相关问题 (57-60)
        {
            "id": 57,
            "question": "您容易过敏吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "特禀质"
        },
        {
            "id": 58,
            "question": "您的皮肤容易起荨麻疹吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "特禀质"
        },
        {
            "id": 59,
            "question": "您容易哮喘吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "特禀质"
        },
        {
            "id": 60,
            "question": "您有因季节改变而加重的病症吗？",
            "options": ["没有", "很少", "有时", "经常", "总是"],
            "scores": [1, 2, 3, 4, 5],
            "constitution_type": "特禀质"
        }
    ],
    "scoring_rules": {
        "thresholds": {
            "平和质": {
                "main": 60,
                "others": 30
            },
            "其他体质": {
                "main": 40
            }
        },
        "options_weight": {
            "没有": 1,
            "很少": 2,
            "有时": 3,
            "经常": 4,
            "总是": 5
        }
    }
}