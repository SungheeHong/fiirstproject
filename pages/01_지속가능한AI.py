import streamlit as st

# 🎬 타이틀
st.title("🤖🌱 AI로 만드는 지속가능한 미래")

# 💬 설명 텍스트
st.markdown("""
AI는 **지속가능한 개발 목표(SDGs)** 달성에 큰 힘이 돼! 🌍  
관심 있는 목표를 골라보면,  
- 📌 **AI가 어떻게 기여하는지**  
- 📺 **관련 동영상**  
- 📚 **추천 도서**  
- 🧾 **실제 적용 사례**  
까지 알려줄게!  
""")

# 🌱 SDG 정보 (이름, 설명, 사례, 동영상 URL, 도서 제목과 소개)
sdg_info = {
    "🎓 양질의 교육 (SDG 4)": {
        "ai_use": "AI 튜터, 학습 예측 모델, 학습 데이터 분석 등을 통해 교육 격차를 줄일 수 있어 📘🧠",
        "example": "케냐에서는 AI 기반 앱이 문자 해독을 도와주는 교육 도구로 사용되고 있어.",
        "video": "https://www.youtube.com/watch?v=5MgBikgcWnY",
        "book": {
            "title": "교육 혁신과 인공지능",
            "desc": "AI가 교육 현장을 어떻게 변화시키는지 알기 쉽게 설명하는 책 📖✨"
        }
    },
    "🍚 기아 종식 (SDG 2)": {
        "ai_use": "AI 기반 농업 예측, 수확량 분석, 작물 질병 진단으로 식량 문제 해결에 기여할 수 있어 🌾🤖",
        "example": "IBM의 ‘Watson Decision Platform’은 농부들에게 병충해를 예측해줘서 수확량을 늘리고 있어.",
        "video": "https://www.youtube.com/watch?v=5vBCRn0kLgI",
        "book": {
            "title": "스마트 농업과 AI",
            "desc": "농업 분야에서 AI가 어떻게 혁신을 일으키는지 알려주는 책 🌱🤖"
        }
    },
    "💧 깨끗한 물과 위생 (SDG 6)": {
        "ai_use": "센서 + AI 분석으로 수질 관리, 오염 감지, 정수 시스템 최적화 💦📊",
        "example": "인도에서는 AI로 지하수 오염을 실시간 감지해서 안전한 식수를 확보하고 있어.",
        "video": "https://www.youtube.com/watch?v=6M5VXKLf4D4",
        "book": {
            "title": "AI와 환경 보호",
            "desc": "환경 분야에서 AI가 어떻게 기여하는지 흥미롭게 풀어낸 책 🌍🤖"
        }
    },
    "🌍 기후 행동 (SDG 13)": {
        "ai_use": "기후 데이터 예측, 탄소 배출 추적, 에너지 사용 최적화에 AI가 활약 중! 🌡️🌳",
        "example": "Google의 AI는 기상 패턴을 분석해서 풍력 에너지를 예측에 활용되고 있어.",
        "video": "https://www.youtube.com/watch?v=Vx4v3ybnRJs",
        "book": {
            "title": "기후변화와 인공지능",
            "desc": "기후변화 문제 해결에 AI가 어떤 역할을 하는지 상세히 다룬 책 🌡️📘"
        }
    },
}

# 📌 선택형 SDG 드롭다운
selected = st.selectbox("👉 알고 싶은 SDG를 골라봐!", [""] + list(sdg_info.keys()))

# ✨ 선택한 SDG에 대한 정보 출력
if selected:
    st.subheader(f"{selected}에 AI는 이렇게 쓰이고 있어!")

    st.markdown(f"🧠 **AI 역할:** {sdg_info[selected]['ai_use']}")
    st.markdown(f"📌 **사례:** {sdg_info[selected]['example']}")

    # 도서 정보 출력
    book = sdg_info[selected]['book']
    st.markdown(f"📚 **추천 도서:** **{book['title']}**\n\n_{book['desc']}_")

    # 🖥️ 유튜브 동영상 임베드
    video_url = sdg_info[selected]['video']
    st.video(video_url)
