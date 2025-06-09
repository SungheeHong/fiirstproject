import streamlit as st

# 🎈 첫 화면에서 풍선 효과
st.balloons()

# 🎉 타이틀
st.title("🎬✨ MBTI로 추천받는 명작 과학/수학 영화 🍿🧠")

# 💬 설명 텍스트
st.markdown("""
MBTI를 아래에서 선택하면  
**너만을 위한 과학 🧪 / 수학 📐 명작 영화**를 추천해줄게!  
""")

# 🎯 MBTI 목록
mbti_list = [
    "INTP", "INTJ", "ENTP", "INFJ", "ENFP", "ISTJ", "ISFP", "ESTJ",
    "ESFP", "INFP", "ENTJ", "ISFJ", "ESTP", "ESFJ", "ISTP", "ENFJ"
]

# 📌 드롭다운으로 MBTI 선택
selected_mbti = st.selectbox("👉 너의 MBTI를 골라봐!", [""] + mbti_list)

# 🧠 영화 추천 딕셔너리
movie_dict = {
    "INTP": ("📽️ 《굿 윌 헌팅》", "수학 천재의 성장과 감동 스토리 💡"),
    "INTJ": ("🎬 《이미테이션 게임》", "논리와 전략의 천재 튜링 이야기 🔐"),
    "ENTP": ("🧪 《인터스텔라》", "끝없는 호기심, 우주 과학 대서사시 🌌"),
    "INFJ": ("🎥 《

        movie, desc = movie_dict[mbti]
        st.success(f"🎉 {mbti}에게 딱 맞는 영화는...\n\n### {movie}\n> {desc}")
        st.balloons()
    else:
        st.error("😥 알 수 없는 MBTI야! 다시 입력해줘 (예: INTP)")
