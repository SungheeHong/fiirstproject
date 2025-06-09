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

# 🗺️ MBTI별 추천 여행지 데이터
mbti_destinations = {
    "INTJ": ("🇯🇵 교토, 일본", "전통과 조용한 사색이 공존하는 도시. 명상과 역사적 성찰을 좋아하는 INTJ에게 딱! 🧘‍♂️⛩️"),
    "INTP": ("🇩🇪 베를린, 독일", "자유롭고 창의적인 분위기에서 아이디어 뿜뿜! 철학과 예술이 가득한 도시 🎨🧠"),
    "ENTJ": ("🇺🇸 뉴욕, 미국", "빠르게 움직이고 도전하는 삶! 비즈니스와 성장을 즐기는 ENTJ에게 찰떡 🗽💼"),
    "ENTP": ("🇰🇷 서울, 대한민국", "활발한 변화와 트렌드의 중심! 아이디어 뱅크인 ENTP에게 어울리는 도시 🔥📱"),
    "INFJ": ("🇨🇦 밴쿠버, 캐나다", "자연 속에서 조용한 자기 성찰 🌲 깊은 감성을 가진 INFJ에게 안성맞춤 🧘‍♀️"),
    "INFP": ("🇳🇿 퀸스타운, 뉴질랜드", "꿈과 자연을 사랑하는 INFP에게 완벽한 힐링 여행지 🏞️🌈"),
    "ENFJ": ("🇫🇷 파리, 프랑스", "로맨틱하고 감성을 나눌 수 있는 도시 💖 따뜻한 ENFJ에게 잘 맞아 ✨🗼"),
    "ENFP": ("🇮🇹 로마, 이탈리아", "역사도 예술도 열정도 한가득! 열정적인 ENFP에겐 최고의 무대 🎭🍝"),
    "ISTJ": ("🇸🇪 스톡홀름, 스웨덴", "질서와 계획을 중시하는 ISTJ에게 어울리는 정갈한 도시 🧩📚"),
    "ISFJ": ("🇨🇭 루체른, 스위스", "조용하고 따뜻한 풍경, 안정감 있는 여행을 좋아하는 ISFJ에게 찰떡 🏔️🚶‍♀️"),
    "ESTJ": ("🇬🇧 런던, 영국", "효율과 전통을 함께! 정돈된 도시를 좋아하는 ESTJ에게 딱 👑📊"),
    "ESFJ": ("🇦🇺 시드니, 호주", "사람들과 즐겁게 어울리기 좋은 활기찬 도시 🎉🏖️"),
    "ISTP": ("🇮🇸 레이캬비크, 아이슬란드", "색다른 모험과 자연 탐험을 사랑하는 ISTP에겐 환상의 땅 🌋❄️"),
    "ISFP": ("🇹🇭 치앙마이, 태국", "예술, 감성, 자유로운 분위기를 느낄 수 있는 도시 🎨🌺"),
    "ESTP": ("🇧🇷 리우데자네이루, 브라질", "액티브하고 열정적인 ESTP에게 딱! 춤과 모험의 나라 🎉🌊"),
    "ESFP": ("🇪🇸 바르셀로나, 스페인", "음악과 예술, 열정 가득한 파티 도시! ESFP에게 최고의 즐거움 💃🎨")
}

# 🎯 선택 박스
selected_mbti = st.selectbox("🔍 MBTI를 골라봐!", [""] + mbti_types)

# 🎁 결과 출력
if selected_mbti:
    destination, description = mbti_destinations[selected_mbti]
    st.success(f"🌟 추천 여행지: {destination}")
    st.markdown(f"📌 {description}")
    st.balloons()
