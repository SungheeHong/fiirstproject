import streamlit as st

# 🎈 풍선 효과
st.balloons()

# 🌟 타이틀
st.title("✈️ MBTI로 떠나는 나만의 여행지 찾기 💼🌎")

# 💬 설명
st.markdown("""
당신의 **MBTI**는 어디로 떠나고 싶을까?  
🧠 성격 유형에 맞는 여행지를 🎯 찰떡같이 추천해줄게!  
MBTI를 선택해봐 ✨
""")

# 🧠 MBTI 유형
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 🗺️ M
