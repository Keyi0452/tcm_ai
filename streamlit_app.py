import streamlit as st
from main import TCMConsultant
from data.questions import questions_data
from recommender.personalized_recommender import PersonalizedRecommender
from data.recommendations import lifestyle_recommendations

def main():
    # 设置页面配置，启用移动端响应式布局
    st.set_page_config(
        page_title="中医体质辨识系统",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # 添加现代化的CSS样式
    st.markdown("""
        <style>
        /* 全局样式 */
        .main {
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            color: #1d1d1f;
            background: #fbfbfd;
        }
        
        /* 标题样式 */
        h1 {
            font-size: 48px;
            font-weight: 600;
            letter-spacing: -0.003em;
            margin-bottom: 1.5rem;
        }
        
        /* 问卷卡片样式 */
        .stExpander {
            background: white;
            border-radius: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            transition: all 0.3s ease;
            margin: 1rem 0;
        }
        
        .stExpander:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }
        
        /* 按钮样式 */
        .stButton > button {
            background: linear-gradient(180deg, #0071e3 0%, #0077ed 100%);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 980px;
            font-size: 16px;
            font-weight: 500;
            transition: all 0.3s ease;
            width: auto;
            margin: 2rem auto;
            display: block;
        }
        
        .stButton > button:hover {
            background: linear-gradient(180deg, #0077ed 0%, #0082f6 100%);
            transform: scale(1.02);
        }
        
        /* 结果卡片样式 */
        .constitution-card {
            background: white;
            border-radius: 20px;
            padding: 1.2rem 2rem;
            margin: 1rem 0;
            box-shadow: 0 4px 10px -3px rgba(0, 0, 0, 0.1);
        }
        
        /* 结果卡片样式 */
        .constitution-card {
            background: white;
            border-radius: 20px;
            padding: 1.2rem 2rem;
            margin: 1rem 0;
            box-shadow: 0 4px 10px -3px rgba(0, 0, 0, 0.1);
        }
        
        /* 建议卡片样式 */
        .advice-card {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 20px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        
        .advice-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        
        /* 输入框样式 */
        .stTextInput > div > div > input {
            border-radius: 12px;
            border: 1px solid #d2d2d7;
            padding: 12px;
            font-size: 16px;
        }
        
        /* 单选按钮组样式 */
        .stRadio > div {
            background: white;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #d2d2d7;
        }
        
        /* 展开器标题样式 */
        .streamlit-expanderHeader {
            font-size: 18px;
            font-weight: 500;
            color: #1d1d1f;
        }
        
        /* 进度条样式 */
        .stProgress > div > div > div {
            background-color: #0071e3;
            border-radius: 999px;
        }
        
        /* 响应式布局 */
        @media (max-width: 768px) {
            .main {
                padding: 1rem;
            }
            
            h1 {
                font-size: 32px;
            }
            
            .constitution-card {
                padding: 1.5rem;
            }
            
            .stButton > button {
                width: 100%;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # 页面标题和介绍
    st.markdown("""
        <div style='text-align: center; padding: 3rem 0;'>
            <h1>中医体质辨识系统</h1>
            <p style='font-size: 1.2rem; color: #86868b; max-width: 600px; margin: 0 auto;'>
                通过现代化的分析方法，了解您的体质特点，获取个性化调养建议
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 免责声明
    st.markdown("""
        <div style='background: #f5f5f7; border-radius: 16px; padding: 1rem; margin: 2rem 0;'>
            <p style='color: #86868b; margin: 0;'>
                ⚠️ 免责声明：本系统仅供参考，不作为医疗诊断依据。如有不适请及时就医。
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 用户信息收集 - 移除 expander，直接显示
    # 用户信息收集 - 将标题和内容放在同一个卡片中
    st.markdown("""
        <div class="constitution-card" style='padding: 1.5rem;'>
            <h2 style='font-size: 1.3rem; margin-bottom: 1rem;'>个人信息</h2>
            <div style='padding: 0 0.5rem;'>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("年龄", 1, 120, 25)
        gender = st.radio("性别", ["男", "女"])
        city = st.text_input("所在城市", placeholder="例如：北京")
    with col2:
        allergies = st.text_input("过敏源", placeholder="多个请用逗号分隔，如：花粉,海鲜")
        exercise_pref = st.text_input("运动偏好", placeholder="多个请用逗号分隔，如：瑜伽,散步")
    
    st.markdown("</div></div>", unsafe_allow_html=True)

    # 问卷部分
    st.markdown("""
        <div class="constitution-card" style='margin-top: 2rem;'>
            <h2 style='font-size: 1.5rem; margin-bottom: 1.5rem;'>体质测评问卷</h2>
            <p style='color: #666; margin-bottom: 2rem;'>请根据您最近一年的体验和感觉回答以下问题：</p>
        </div>
    """, unsafe_allow_html=True)
    
    answers = {}
    for question in questions_data:
        # 修改问题编号和内容的颜色
        st.markdown(f"""
            <div style='background: white; padding: 1.5rem; border-radius: 12px; margin: 1rem 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                <p style='font-weight: 500; color: #1d1d1f; margin-bottom: 1rem;'>
                    <span style='color: #1d1d1f; margin-right: 0.5rem;'>问题 {question['id']}:</span>
                    {question['content']}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 在 CSS 样式部分修改按钮和标题样式
        st.markdown("""
            <style>
            /* 全局样式 */
            .main {
                font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
                color: #1d1d1f;
                background: #fbfbfd;
            }
            
            /* 标题样式 */
            h1 {
                font-size: 48px;
                font-weight: 600;
                letter-spacing: -0.003em;
                margin-bottom: 1.5rem;
            }
            
            /* 问卷卡片样式 */
            .stExpander {
                background: white;
                border-radius: 20px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                transition: all 0.3s ease;
                margin: 1rem 0;
            }
            
            .stExpander:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            }
            
            /* 按钮样式 */
            .stButton > button {
                background: rgba(0, 0, 0, 0.05);
                color: #1d1d1f;
                border: none;
                padding: 12px 24px;
                border-radius: 980px;
                font-size: 16px;
                font-weight: 500;
                transition: all 0.3s ease;
                width: auto;
                margin: 2rem auto;
                display: block;
            }
            
            .stButton > button:hover {
                background: rgba(0, 0, 0, 0.1);
                transform: scale(1.02);
            }
        
            /* 展开器标题样式 */
            .streamlit-expanderHeader {
                font-size: 1.8rem !important;
                font-weight: 600 !important;
                color: #1d1d1f !important;
                padding: 1rem !important;
            }
            </style>
        """, unsafe_allow_html=True)
        answer = st.radio(
            "",  # 移除标签文本
            options=range(1, 6),
            format_func=lambda x: question['options'][x-1],
            key=f"q_{question['id']}"
        )
        answers[question['id']] = answer

    # 更新用户信息字典
    user_info = {
        "age": age,
        "gender": gender,
        "location": city,  # 使用城市名称
        "allergies": [item.strip() for item in allergies.split(",") if item.strip()],
        "preferences": {
            "exercise": [item.strip() for item in exercise_pref.split(",") if item.strip()]
        }
    }
    
    if st.button("提交分析"):
        with st.spinner("正在分析您的体质特征..."):
            consultant = TCMConsultant()
            results = consultant.analyze_constitution(answers)
        
        st.success("分析完成！")
        
        # 主体质显示（移除详细评分部分）
        main_constitution = max(results, key=lambda x: x[1])
        constitution_type = main_constitution[0]
        
        st.markdown(f"""
            <div class="constitution-card">
                <h2 style='font-size: 1.5rem; margin-bottom: 1rem;'>您的主要体质类型</h2>
                <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
                    <span style='font-size: 2rem; color: #1f77b4;'>{main_constitution[0]}</span>
                    <span style='margin-left: 1rem; font-size: 1.2rem; color: #666;'>得分：{main_constitution[1]:.1f}</span>
                </div>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #eee;'>
                    <p style='font-size: 1.1rem; line-height: 1.6; color: #333;'>
                        {lifestyle_recommendations[constitution_type].get('description', '')}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # 删除原来的体质特点解析部分
        # 直接开始个性化建议部分
        st.markdown("""
            <div class="constitution-card">
                <h2>🎯 个性化调养建议</h2>
                <div style='padding: 0 1rem;'>
        """, unsafe_allow_html=True)
        
        
        with st.container():
            recommender = PersonalizedRecommender(lifestyle_recommendations)
            advice = recommender.get_personalized_advice(
                {type_name: score for type_name, score in results},
                user_info
            )
            
            # 日常起居建议
            if "daily_routines" in advice:
                st.markdown("<h2 class='main-category'>⏰ 日常起居建议</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    for routine in advice["daily_routines"]:
                        st.markdown(f"- {routine}")
            
            # 情志调养
            if "emotional_care" in advice:
                st.markdown("<h2 class='main-category'>🧘‍♀️ 情志调养</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    if "daily_management" in advice["emotional_care"]:
                        st.subheader("日常管理")
                        for item in advice["emotional_care"]["daily_management"]:
                            st.markdown(f"- {item}")
                    if "stress_relief" in advice["emotional_care"]:
                        st.subheader("减压方法")
                        for item in advice["emotional_care"]["stress_relief"]:
                            st.markdown(f"- {item}")
                    if "mood_improvement" in advice["emotional_care"]:
                        st.subheader("情绪改善")
                        for item in advice["emotional_care"]["mood_improvement"]:
                            st.markdown(f"- {item}")
            
            # 运动建议
            if "exercise_advice" in advice:
                st.markdown("<h2 class='main-category'>🏃‍♂️ 运动建议</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    if "exercise_principles" in advice["exercise_advice"]:
                        st.subheader("运动原则")
                        for principle in advice["exercise_advice"]["exercise_principles"]:
                            st.markdown(f"📌 {principle}")
                    
                    st.subheader("推荐运动")
                    for exercise in advice["exercise_advice"].get("recommended_exercises", []):
                        st.markdown(f"""
                            <div class="advice-card">
                                <h4>{exercise['type']}</h4>
                                <p>🎯 推荐项目：{', '.join(exercise['items'])}</p>
                                <p>⏱️ 建议时长：{exercise['duration']}</p>
                                <p>📅 运动频率：{exercise['frequency']}</p>
                            </div>
                        """, unsafe_allow_html=True)
            
            # 饮食建议
            if "diet_advice" in advice:
                st.markdown("<h2 class='main-category'>🍲 饮食建议</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    if "dietary_principles" in advice["diet_advice"]:
                        st.subheader("饮食原则")
                        for principle in advice["diet_advice"]["dietary_principles"]:
                            st.markdown(f"📌 {principle}")
                    
                    if "eating_habits" in advice["diet_advice"]:
                        st.subheader("饮食习惯")
                        for habit in advice["diet_advice"]["eating_habits"]:
                            st.markdown(f"✨ {habit}")
                    
                    if "suitable_foods" in advice["diet_advice"]:
                        st.subheader("适宜食物")
                        for food in advice["diet_advice"]["suitable_foods"]:
                            st.markdown(f"✅ {food}")

            # 中药茶饮
            if "herbal_tea" in advice:
                st.markdown("<h2 class='main-category'>🫖 中药茶饮</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    if "seasonal_adjustments" in advice["herbal_tea"]:
                        st.subheader("季节调整")
                        for season, adj in advice["herbal_tea"]["seasonal_adjustments"].items():
                            st.markdown(f"🍃 {season}：{adj}")
                    
                    st.subheader("推荐茶饮")
                    for recipe in advice["herbal_tea"].get("daily_recipes", []):
                        st.markdown(f"""
                            <div class="advice-card">
                                <h4>{recipe['name']}</h4>
                                <p><strong>配方：</strong></p>
                                {''.join([f'<p>- {ing["name"]} {ing["amount"]}</p>' for ing in recipe['ingredients']])}
                                <p><strong>煎煮方法：</strong>{recipe['brewing']}</p>
                                <p><strong>服用时间：</strong>{recipe['drinking_time']}</p>
                                <p><strong>注意事项：</strong>{recipe.get('notes', '无')}</p>
                            </div>
                        """, unsafe_allow_html=True)
            
            # 穴位保健
            if "acupoint_care" in advice:
                st.markdown("<h2 class='main-category'>🌟 穴位保健</h2>", unsafe_allow_html=True)
                with st.expander("", expanded=True):
                    st.subheader("日常穴位")
                    for point in advice["acupoint_care"].get("daily_points", []):
                        st.markdown(f"""
                            <div class="advice-card">
                                <h4>{point['name']}</h4>
                                <p><strong>位置：</strong>{point['location']}</p>
                                <p><strong>方法：</strong>{point['method']}</p>
                                <p><strong>时间：</strong>{point['timing']}</p>
                                <p><strong>功效：</strong>{point['benefits']}</p>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    if "massage_tools" in advice["acupoint_care"]:
                        st.subheader("推荐工具")
                        for tool in advice["acupoint_care"]["massage_tools"]:
                            st.markdown(f"🔧 {tool}")
            
            # 关闭个性化建议的 div 标签
            st.markdown("</div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()