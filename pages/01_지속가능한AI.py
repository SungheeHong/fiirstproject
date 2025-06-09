import streamlit as st

# 🎈 첫 진입 풍선 효과
st.balloons()

# 🎬 타이틀
st.title("🤖🌱 AI로 만드는 지속가능한 미래")

# 💬 설명 텍스트
st.markdown("""
AI는 **지속가능한 개발 목표(SDGs)** 달성에 큰 힘이 돼! 🌍  
관심 있는 목표를 골라보면,  
- 📌 **AI가 어떻게 기여하는지**  
- 📸 **관련 이미지**  
- 🧾 **실제 적용 사례**  
까지 알려줄게!  
""")

# 🌱 SDG 목록 (이름, 설명, 사례, 이미지 URL)
sdg_info = {
    "🎓 양질의 교육 (SDG 4)": {
        "ai_use": "AI 튜터, 학습 예측 모델, 학습 데이터 분석 등을 통해 교육 격차를 줄일 수 있어 📘🧠",
        "example": "케냐에서는 AI 기반 앱이 문자 해독을 도와주는 교육 도구로 사용되고 있어.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Sustainable_Development_Goal_4.png/240px-Sustainable_Development_Goal_4.png"
    },
    "🍚 기아 종식 (SDG 2)": {
        "ai_use": "AI 기반 농업 예측, 수확량 분석, 작물 질병 진단으로 식량 문제 해결에 기여할 수 있어 🌾🤖",
        "example": "IBM의 ‘Watson Decision Platform’은 농부들에게 병충해를 예측해줘서 수확량을 늘리고 있어.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Sustainable_Development_Goal_2.png/240px-Sustainable_Development_Goal_2.png"
    },
    "💧 깨끗한 물과 위생 (SDG 6)": {
        "ai_use": "센서 + AI 분석으로 수질 관리, 오염 감지, 정수 시스템 최적화 💦📊",
        "example": "인도에서는 AI로 지하수 오염을 실시간 감지해서 안전한 식수를 확보하고 있어.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Sustainable_Development_Goal_6.png/240px-Sustainable_Development_Goal_6.png"
    },
    "🌍 기후 행동 (SDG 13)": {
        "ai_use": "기후 데이터 예측, 탄소 배출 추적, 에너지 사용 최적화에 AI가 활약 중! 🌡️🌳",
        "example": "Google의 AI는 기상 패턴을 분석해서 풍력 에너지 예측에 활용되고 있어.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sustainable_Development_Goal_13.png/240px-Sustainable_Development_Goal_13.png"
    },
}

# 📌 드롭다운으로 SDG 선택
selected = st.selectbox("👉 알고 싶은 SDG를 골라봐!", [""] + list(sdg_info.keys()))

# ✨ 선택 시 정보 보여주기
if selected:
    st.subheader(f"{selected}에 AI는 이렇게 쓰이고 있어!")
    
    # 🔍 AI 기여 설명
    st.markdown(f"🧠 **AI 역할:** {sdg_info[selected]['ai_use']}")

    # 🧾 실제 사례
    st.markdown(f"📌 **사례:** {sdg_info[selected]['example']}")

    # 🖼️ 이미지
    st.image(sdg_info[selected]['image'], use_column_width=True, caption=f"{selected} 관련 이미지")

    st.balloons()

    # 🧠 퀴즈 버튼
    if st.button("🧠 나 퀴즈 낼래!"):
        st.info("❓ 문제: AI가 작물 질병을 예측하는 데 도움이 되는 SDG는 무엇일까?")
        st.markdown("""
        - A) SDG 4  
        - B) SDG 2  
        - C) SDG 6  
        - D) SDG 13
        """)
        answer = st.radio("정답을 골라봐!", ["A", "B", "C", "D"], index=0)
        if answer == "B":
            st.success("🎉 정답! AI는 식량 문제 해결에 큰 역할을 해!")
            st.balloons()
        else:
            st.error("🙅‍♂️ 아쉬워! 다시 생각해봐~ 정답은 SDG 2야!")
