import streamlit as st

# 🎬 타이틀
st.title("🤖🌱 AI로 만드는 지속가능한 미래")

# 💬 설명 텍스트
st.markdown("""
AI는 **지속가능한 개발 목표(SDGs)** 달성에 큰 힘이 돼! 🌍  
관심 있는 목표를 골라보면,  
- 📌 **AI가 어떻게 기여하는지**  
- 📺 **관련 동영상**  
- 🧾 **실제 적용 사례**  
까지 알려줄게!  
""")

# 🌱 SDG 정보 (이름, 설명, 사례, 동영상 URL)
sdg_info = {
    "🎓 양질의 교육 (SDG 4)": {
        "ai_use": "AI 튜터, 학습 예측 모델, 학습 데이터 분석 등을 통해 교육 격차를 줄일 수 있어 📘🧠",
        "example": "케냐에서는 AI 기반 앱이 문자 해독을 도와주는 교육 도구로 사용되고 있어.",
        "video": "https://www.youtube.com/watch?v=5MgBikgcWnY"  # 예시 유튜브 링크
    },
    "🍚 기아 종식 (SDG 2)": {
        "ai_use": "AI 기반 농업 예측, 수확량 분석, 작물 질병 진단으로 식량 문제 해결에 기여할 수 있어 🌾🤖",
        "example": "IBM의 ‘Watson Decision Platform’은 농부들에게 병충해를 예측해줘서 수확량을 늘리고 있어.",
        "video": "https://www.youtube.com/watch?v=5vBCRn0kLgI"
    },
    "💧 깨끗한 물과 위생 (SDG 6)": {
        "ai_use": "센서 + AI 분석으로 수질 관리, 오염 감지, 정수 시스템 최적화 💦📊",
        "example": "인도에서는 AI로 지하수 오염을 실시간 감지해서 안전한 식수를 확보하고 있어.",
        "video": "https://www.youtube.com/watch?v=6M5VXKLf4D4"
    },
    "🌍 기후 행동 (SDG 13)": {
        "ai_use": "기후 데이터 예측, 탄소 배출 추적, 에너지 사용 최적화에 AI가 활약 중! 🌡️🌳",
        "example": "Google의 AI는 기상 패턴을 분석해서 풍력 에너지를 예측에 활용되고 있어.",
        "video": "https://www.youtube.com/watch?v=Vx4v3ybnRJs"
    },
}

# 📌 선택형 SDG 드롭다운
selected = st.selectbox("👉 알고 싶은 SDG를 골라봐!", [""] + list(sdg_info.keys()))

# ✨ 선택한 SDG에 대한 정보 출력
if selected:
    st.subheader(f"{selected}에 AI는 이렇게 쓰이고 있어!")

    st.markdown(f"🧠 **AI 역할:** {sdg_info[selected]['ai_use']}")
    st.markdown(f"📌 **사례:** {sdg_info[selected]['example']}")

    # 🖥️ 유튜브 동영상 임베드 (YouTube URL이 포함된 경우)
    video_url = sdg_info[selected]['video']
    st.video(video_url)
