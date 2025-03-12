export const constitutionData = {
    "平和质": {
        name: "平和质",
        description: "平和质是最理想的体质状态。特点是面色红润、精力充沛、睡眠良好、体形匀称、性格开朗、适应能力强。这类人抗病能力强，不易生病。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议6-7点起床，可做八段锦或易筋经等养生功法，注意避免过度劳累。"
            },
            {
                time: "中午",
                content: "午餐后适当休息15-30分钟，保持良好的精神状态。"
            },
            {
                time: "晚上",
                content: "22-23点前入睡，保证7-8小时充足睡眠，睡前可以泡脚放松。"
            }
        ],
        exerciseGeneral: "平和质人群可以进行各种适度运动，注意循序渐进，以保持体质平和状态。",
        exerciseSpecific: [
            {
                name: "太极拳",
                description: "柔和缓慢的运动方式，可以调节气血，增强体质。建议每天晨练30-60分钟。"
            },
            {
                name: "游泳",
                description: "全身性运动，可以增强心肺功能，建议每周2-3次，每次30分钟。"
            },
            {
                name: "快走",
                description: "简单易行的有氧运动，促进新陈代谢，建议每天进行，每次30-60分钟。"
            }
        ],
        dietGeneral: "饮食应以清淡为主，荤素搭配，注意营养均衡。",
        dietRecipes: [
            {
                name: "山药炖排骨",
                ingredients: "山药、排骨、枸杞、红枣",
                method: "将排骨焯水，加入山药、枸杞、红枣，慢火炖煮1小时即可。"
            },
            {
                name: "百合莲子粥",
                ingredients: "百合、莲子、大米、红枣",
                method: "将材料洗净，加水煮至粥稠即可。"
            },
            {
                name: "木耳炒西兰花",
                ingredients: "黑木耳、西兰花、胡萝卜",
                method: "木耳泡发，西兰花焯水，快火翻炒。"
            }
        ],
        teaGeneral: "可以饮用各类养生茶，但不宜过浓。",
        teaRecipes: [
            {
                name: "菊花茶",
                ingredients: "菊花、枸杞",
                method: "沸水冲泡3-5分钟即可。"
            },
            {
                name: "红枣枸杞茶",
                ingredients: "红枣、枸杞、桂圆",
                method: "材料加水煮沸，小火续煮10分钟。"
            },
            {
                name: "绿茶",
                ingredients: "绿茶叶",
                method: "80度水温冲泡，1-2分钟即可。"
            }
        ]
    },

    "气虚质": {
        name: "气虚质",
        description: "气虚质的人容易疲劳，说话声音低弱，气短懒言，容易出汗，舌淡胖嫩。这类人抵抗力较弱，容易感冒。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议7-8点起床，切忌早起强运动，可做缓和的深呼吸练习。"
            },
            {
                time: "中午",
                content: "午餐后必须休息，建议躺床小憩30分钟。"
            },
            {
                time: "晚上",
                content: "21:30前就寝，保证充足睡眠，避免熬夜。"
            }
        ],
        exerciseGeneral: "适合缓和、柔和的运动，避免剧烈运动，注意运动量要循序渐进。",
        exerciseSpecific: [
            {
                name: "八段锦",
                description: "温和传统养生功法，可以补气养生，每天晨练15-20分钟。"  // 修改这里
            },
            {
                name: "散步",
                description: "最适合气虚体质的运动，建议每天进行，每次20-30分钟。"
            },
            {
                name: "导引养生功",
                description: "柔和的养生运动，可以培养元气，建议每天练习15-20分钟。"
            }
        ],
        dietGeneral: "饮食应以温补为主，多食用补气养血的食物。",
        dietRecipes: [
            {
                name: "人参炖鸡汤",
                ingredients: "人参、母鸡、枸杞、红枣",
                method: "将材料一起炖煮2小时，适量饮用汤汁。"
            },
            {
                name: "黄芪红枣粥",
                ingredients: "黄芪、红枣、大米",
                method: "黄芪和红枣先煮汤，加入大米煮粥。"
            },
            {
                name: "山药炖排骨",
                ingredients: "山药、排骨、黄芪、红枣",
                method: "将材料一起炖煮1.5小时即可。"
            }
        ],
        teaGeneral: "适合饮用温补性质的茶饮，避免苦寒性的茶。",
        teaRecipes: [
            {
                name: "人参茶",
                ingredients: "人参片、红枣、枸杞",
                method: "材料加水小火煮15分钟。"
            },
            {
                name: "黄芪红枣茶",
                ingredients: "黄芪、红枣、桂圆",
                method: "材料加水煮20分钟。"
            },
            {
                name: "西洋参茶",
                ingredients: "西洋参片、枸杞",
                method: "材料加水冲泡10分钟。"
            }
        ]
    },

    "阳虚质": {
        name: "阳虚质",
        description: "阳虚质的人怕冷，手脚发凉，精神不振，喜温喜热，舌质淡，脉沉迟。平素畏寒，容易感冒，常有腹泻。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议7:30后起床，避免早起受寒，起床后可做温和的热身运动。"
            },
            {
                time: "中午",
                content: "午餐后在温暖环境下休息，注意保暖。"
            },
            {
                time: "晚上",
                content: "22点前就寝，睡前可泡热水脚，注意睡眠保暖。"
            }
        ],
        exerciseGeneral: "选择温和且能温阳的运动，避免在寒冷环境下运动。",
        exerciseSpecific: [
            {
                name: "太阳功",
                description: "晒太阳时进行的养生功法，可温阳补虚，每天10-15分钟。"
            },
            {
                name: "温水游泳",
                description: "在温水泳池中进行，可增强阳气，每周2-3次。"
            },
            {
                name: "八段锦",
                description: "在温暖环境下进行，可温养阳气，每天15-20分钟。"
            }
        ],
        dietGeneral: "饮食宜温热，多食用温补阳气的食物，避免生冷。",
        dietRecipes: [
            {
                name: "羊肉枸杞汤",
                ingredients: "羊肉、枸杞、生姜、党参",
                method: "将材料一起炖煮1.5小时，加入适量盐调味。"
            },
            {
                name: "桂圆红枣粥",
                ingredients: "桂圆、红枣、大米、生姜",
                method: "材料一起煮粥，加入少许红糖调味。"
            },
            {
                name: "韭菜炒虾仁",
                ingredients: "韭菜、虾仁、生姜、料酒",
                method: "大火快炒，保持食材的温热性。"
            }
        ],
        teaGeneral: "适合温热性质的茶饮，避免寒凉性的茶。",
        teaRecipes: [
            {
                name: "生姜红茶",
                ingredients: "生姜片、红茶、红糖",
                method: "材料一起冲泡，趁热饮用。"
            },
            {
                name: "桂圆红枣茶",
                ingredients: "桂圆、红枣、生姜",
                method: "材料加水煮15分钟即可。"
            },
            {
                name: "肉桂茶",
                ingredients: "肉桂、红茶、枣片",
                method: "材料加水煮10分钟即可。"
            }
        ]
    },

    "阴虚质": {
        name: "阴虚质",
        description: "阴虚质的人手足心热，口燥咽干，面部潮红，容易失眠，大便干燥。舌红少津，脉细数。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议6:30-7:30起床，晨练宜选择阴凉处，避免暴晒。"
            },
            {
                time: "中午",
                content: "午休要避开阳光直射处，保持安静休息。"
            },
            {
                time: "晚上",
                content: "22点前就寝，避免熬夜，睡前可用温水泡脚。"
            }
        ],
        exerciseGeneral: "选择凉爽时段运动，避免剧烈运动和暴晒。",
        exerciseSpecific: [
            {
                name: "太极拳",
                description: "柔和的运动方式，可以滋阴养气，建议清晨或傍晚练习。"
            },
            {
                name: "瑜伽",
                description: "可以静心养阴，建议在室内进行，每次40-60分钟。"
            },
            {
                name: "游泳",
                description: "水中运动可滋养阴液，避免在烈日下进行。"
            }
        ],
        dietGeneral: "饮食宜清淡滋润，避免辛辣刺激，多食用养阴润燥的食物。",
        dietRecipes: [
            {
                name: "银耳雪梨汤",
                ingredients: "银耳、雪梨、冰糖",
                method: "将材料炖煮40分钟，温热食用。"
            },
            {
                name: "百合莲子粥",
                ingredients: "百合、莲子、大米、红枣",
                method: "材料煮至粥稠即可。"
            },
            {
                name: "秋葵炖蛋",
                ingredients: "秋葵、鸡蛋、红枣",
                method: "将材料蒸制10分钟即可。"
            }
        ],
        teaGeneral: "适合清凉滋润的茶饮，避免温热燥热的茶。",
        teaRecipes: [
            {
                name: "菊花枸杞茶",
                ingredients: "菊花、枸杞、洋参片",
                method: "材料用沸水冲泡5分钟。"
            },
            {
                name: "罗汉果茶",
                ingredients: "罗汉果、金银花、甘草",
                method: "材料加水煮10分钟即可。"
            },
            {
                name: "石斛花茶",
                ingredients: "石斛花、枸杞、洋参",
                method: "材料用温水冲泡15分钟。"
            }
        ]
    },

    "痰湿质": {
        name: "痰湿质",
        description: "痰湿质的人容易感到胸闷，体形肥胖，容易疲劳，皮肤油腻，舌苔厚腻。常有痰多，容易呕恶。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议6:00-6:30起床，进行适度运动，帮助代谢。"
            },
            {
                time: "中午",
                content: "午餐后短暂休息，不宜久坐或躺卧。"
            },
            {
                time: "晚上",
                content: "22点前就寝，避免夜宵，保持作息规律。"
            }
        ],
        exerciseGeneral: "选择有助于代谢的运动，坚持规律运动以化湿祛痰。",
        exerciseSpecific: [
            {
                name: "快走",
                description: "每天坚持，可促进代谢，建议每次40-60分钟。"
            },
            {
                name: "游泳",
                description: "可以全身运动，促进水液代谢，每周3-4次。"
            },
            {
                name: "健身操",
                description: "可以增强体质，促进新陈代谢，每天30-40分钟。"
            }
        ],
        dietGeneral: "饮食宜清淡，少食多餐，避免油腻甜腻。",
        dietRecipes: [
            {
                name: "薏仁绿豆粥",
                ingredients: "薏仁、绿豆、红枣、山药",
                method: "材料洗净，加水煮至粥稠即可。"
            },
            {
                name: "荷叶蒸鸡",
                ingredients: "鸡肉、荷叶、生姜、葱",
                method: "鸡肉切块，用荷叶包裹蒸制20分钟。"
            },
            {
                name: "冬瓜排骨汤",
                ingredients: "冬瓜、排骨、陈皮",
                method: "材料一起炖煮，去油食用。"
            }
        ],
        teaGeneral: "适合具有化湿利水功效的茶饮。",
        teaRecipes: [
            {
                name: "荷叶茶",
                ingredients: "荷叶、陈皮、茯苓",
                method: "材料加水煮10分钟即可。"
            },
            {
                name: "普洱茶",
                ingredients: "普洱茶、陈皮",
                method: "开水冲泡5分钟。"
            },
            {
                name: "薏仁茶",
                ingredients: "薏仁、红豆、绿茶",
                method: "薏仁红豆煮汤，加入绿茶冲泡。"
            }
        ]
    },

    "湿热质": {
        name: "湿热质",
        description: "湿热质的人容易口苦、口干，容易长痘痤疮，大便粘滞，小便短黄。身体容易感到困重，特别是在梅雨季节。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议6:00-7:00起床，进行适度运动，注意避免剧烈运动。"
            },
            {
                time: "中午",
                content: "午餐后散步15-20分钟，促进消化。"
            },
            {
                time: "晚上",
                content: "22点前就寝，避免熬夜，注意保持环境通风。"
            }
        ],
        exerciseGeneral: "选择有助于排汗的运动，注意运动后及时擦干汗液。",
        exerciseSpecific: [
            {
                name: "快走",
                description: "促进新陈代谢，每天30-45分钟。"
            },
            {
                name: "游泳",
                description: "可以清热利湿，每周3-4次。"
            },
            {
                name: "瑜伽",
                description: "帮助身心放松，每周2-3次。"
            }
        ],
        dietGeneral: "饮食宜清淡，避免辛辣油腻，多食用具有清热利湿作用的食物。",
        dietRecipes: [
            {
                name: "绿豆薏仁汤",
                ingredients: "绿豆、薏仁、淡竹叶",
                method: "材料加水煮至绿豆开花即可。"
            },
            {
                name: "苦瓜炒蛋",
                ingredients: "苦瓜、鸡蛋、姜丝",
                method: "苦瓜切片，与炒散的鸡蛋同炒。"
            },
            {
                name: "赤小豆煲汤",
                ingredients: "赤小豆、冬瓜、玉米",
                method: "材料一起煮汤，适量调味。"
            }
        ],
        teaGeneral: "适合具有清热利湿功效的茶饮。",
        teaRecipes: [
            {
                name: "菊花茶",
                ingredients: "菊花、绿茶、薄荷叶",
                method: "开水冲泡5分钟。"
            },
            {
                name: "荷叶茶",
                ingredients: "荷叶、绿豆、薄荷",
                method: "材料加水煮10分钟。"
            },
            {
                name: "决明子茶",
                ingredients: "决明子、菊花、山楂",
                method: "材料加水煮5-8分钟。"
            }
        ]
    },

    "血瘀质": {
        name: "血瘀质",
        description: "血瘀质的人面色晦暗，肤色偏暗，容易有黑眼圈，口唇发暗，舌质紫暗。经常感到疼痛，且疼痛位置固定。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议6:30-7:00起床，进行舒缓的运动，促进血液循环。"
            },
            {
                time: "中午",
                content: "午餐后适度活动，避免久坐。"
            },
            {
                time: "晚上",
                content: "22点前就寝，可以做轻柔按摩促进血液循环。"
            }
        ],
        exerciseGeneral: "选择可以活血化瘀的运动，注意循序渐进。",
        exerciseSpecific: [
            {
                name: "太极拳",
                description: "柔和运动，促进气血运行，每天30-45分钟。"
            },
            {
                name: "散步",
                description: "促进血液循环，每天45-60分钟。"
            },
            {
                name: "瑜伽",
                description: "改善血液循环，每周3-4次。"
            }
        ],
        dietGeneral: "饮食宜温和，避免过冷过热，多食用活血化瘀的食物。",
        dietRecipes: [
            {
                name: "当归生姜羊肉汤",
                ingredients: "当归、生姜、羊肉、红枣",
                method: "材料一起炖煮1.5小时。"
            },
            {
                name: "桃仁红枣粥",
                ingredients: "桃仁、红枣、大米",
                method: "材料一起熬煮成粥。"
            },
            {
                name: "菜花炒木耳",
                ingredients: "菜花、黑木耳、胡萝卜",
                method: "材料洗净，快火翻炒。"
            }
        ],
        teaGeneral: "适合具有活血化瘀功效的茶饮。",
        teaRecipes: [
            {
                name: "红花茶",
                ingredients: "红花、枸杞、红枣",
                method: "材料加水煮10分钟。"
            },
            {
                name: "玫瑰花茶",
                ingredients: "玫瑰花、红枣、桂圆",
                method: "开水冲泡5-8分钟。"
            },
            {
                name: "三七花茶",
                ingredients: "三七花、红茶、枸杞",
                method: "材料加水冲泡5分钟。"
            }
        ]
    },

    "气郁质": {
        name: "气郁质",
        description: "气郁质的人容易情绪波动，精神抑郁，容易焦虑忧愁，常觉得胸闷气短。多愁善感，适应能力较差。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议7:00起床，进行舒缓运动，保持心情愉悦。"
            },
            {
                time: "中午",
                content: "午餐后散步，与人交谈，保持心情开朗。"
            },
            {
                time: "晚上",
                content: "22点前就寝，睡前可以听轻音乐放松心情。"
            }
        ],
        exerciseGeneral: "选择舒缓身心的运动，注意保持愉悦心情。",
        exerciseSpecific: [
            {
                name: "瑜伽",
                description: "放松身心，缓解压力，每周3-4次。"
            },
            {
                name: "太极拳",
                description: "调节情志，舒缓心情，每天30-45分钟。"
            },
            {
                name: "慢跑",
                description: "释放压力，每周3-4次，每次30分钟。"
            }
        ],
        dietGeneral: "饮食宜清淡，注意规律，可适当食用理气安神的食物。",
        dietRecipes: [
            {
                name: "玫瑰花茶粥",
                ingredients: "玫瑰花、大米、红枣",
                method: "材料一起熬煮成粥。"
            },
            {
                name: "柠檬蜂蜜水",
                ingredients: "柠檬片、蜂蜜、温水",
                method: "温水冲泡，加入适量蜂蜜。"
            },
            {
                name: "香菇炒青菜",
                ingredients: "香菇、青菜、姜丝",
                method: "材料洗净，快火翻炒。"
            }
        ],
        teaGeneral: "适合具有舒肝解郁功效的茶饮。",
        teaRecipes: [
            {
                name: "玫瑰花茶",
                ingredients: "玫瑰花、茉莉花、红枣",
                method: "开水冲泡5分钟。"
            },
            {
                name: "薄荷茶",
                ingredients: "薄荷叶、菊花、枸杞",
                method: "开水冲泡3-5分钟。"
            },
            {
                name: "柑橘茶",
                ingredients: "柑橘皮、红茶、蜂蜜",
                method: "材料冲泡5分钟，加入适量蜂蜜。"
            }
        ]
    },

    "特禀质": {
        name: "特禀质",
        description: "特禀质的人容易过敏，对环境适应能力差，常有特殊体质表现。容易出现皮肤瘙痒、哮喘症状。",
        dailyAdvice: [
            {
                time: "早上",
                content: "建议7:00-7:30起床，注意防护，避免接触过敏原。"
            },
            {
                time: "中午",
                content: "注意防晒，避免暴露在强烈阳光下。"
            },
            {
                time: "晚上",
                content: "22点前就寝，保持室内空气清新。"
            }
        ],
        exerciseGeneral: "选择温和的运动，避免在易过敏环境中运动。",
        exerciseSpecific: [
            {
                name: "室内健身",
                description: "在清洁环境下进行，每天20-30分钟。"
            },
            {
                name: "游泳",
                description: "在室内恒温泳池进行，每周2-3次。"
            },
            {
                name: "太极拳",
                description: "在空气清新处练习，每天20-30分钟。"
            }
        ],
        dietGeneral: "饮食清淡，避免刺激性食物，注意识别过敏食材。",
        dietRecipes: [
            {
                name: "白木耳炖雪梨",
                ingredients: "白木耳、雪梨、冰糖",
                method: "材料炖煮30分钟。"
            },
            {
                name: "山药粥",
                ingredients: "山药、大米、枸杞",
                method: "材料煮至粥稠即可。"
            },
            {
                name: "清蒸鲈鱼",
                ingredients: "鲈鱼、姜丝、葱花",
                method: "材料清蒸10分钟。"
            }
        ],
        teaGeneral: "选择温和无刺激的茶饮，避免容易引起过敏的品类。",
        teaRecipes: [
            {
                name: "苹果茶",
                ingredients: "苹果片、红枣、枸杞",
                method: "材料加水煮10分钟。"
            },
            {
                name: "山楂茶",
                ingredients: "山楂片、红枣、陈皮",
                method: "材料加水煮8-10分钟。"
            },
            {
                name: "菊花茶",
                ingredients: "菊花、枸杞、洋参片",
                method: "开水冲泡5分钟。"
            }
        ]
    }
};