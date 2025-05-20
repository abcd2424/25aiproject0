import streamlit as st

# MBTI 작업 추천
mbti_jobs = {
    "INTJ": ["📊 전략기획", "🧠 데이터 분석", "🔬 연구개발"],
    "INFP": ["🎨 예술가", "📝 시인", "🎥 콘텐츠 제작자"],
    "ENTP": ["🚀 창업가", "🎯 광고기획자", "🛠️ 기술 개발자"],
    "ISFJ": ["💉 간호사", "🤝 사회복지사", "👶 보조 교사"],
    # 필요한 만큼 추가 가능
}

# MBTI 알파벳 설명
mbti_meanings = {
    "E": "🌟 **E (외향형)**: 사람들과 어울릴 때 에너지를 얻어요.",
    "I": "🌙 **I (내향형)**: 혼자 있는 시간이 에너지를 충전해줘요.",
    "S": "🔎 **S (감각형)**: 현실적이고 구체적인 정보를 중시해요.",
    "N": "🌈 **N (직관형)**: 가능성과 아이디어를 중시해요.",
    "T": "⚖️ **T (사고형)**: 논리와 객관적인 판단을 중시해요.",
    "F": "💖 **F (감정형)**: 감정과 공감을 중시해요.",
    "J": "🗂️ **J (판단형)**: 계획적이고 정돈된 걸 좋아해요.",
    "P": "🎨 **P (인식형)**: 유연하고 즉흥적인 걸 선호해요."
}

# MBTI 책/영화 추천
mbti_recommendations = {
    "INTJ": {
        "books": ["『생각의 기술』 - 에드워드 드 보노", "『이기적 유전자』 - 리처드 도킨스"],
        "movies": ["🎥 인터스텔라", "🎥 소셜 네트워크"]
    },
    "INFP": {
        "books": ["『어린 왕자』", "『나미야 잡화점의 기적』"],
        "movies": ["🎥 월플라워", "🎥 인사이드 아웃"]
    },
    "ENTP": {
        "books": ["『스티브 잡스』", "『제로 투 원』"],
        "movies": ["🎥 아이언맨", "🎥 인셉션"]
    },
    "ISFJ": {
        "books": ["『비밀의 화원』", "『책 읽어주는 남자』"],
        "movies": ["🎥 업", "🎥 포레스트 검프"]
    },
}

# 페이지 설정
st.set_page_config(page_title="MBTI 작업 추천기 ✨", page_icon="💼")

# 제목
st.title("💼 MBTI 기반 작업 추천기")
st.markdown("당신의 **MBTI**를 입력하면:")
st.markdown("- 🎯 어울리는 작업")
st.markdown("- 🔤 성격 알파벳 해석")
st.markdown("- 📚 추천 책과 🎬 영화까지!")
st.markdown("👇 아래에 MBTI를 입력해주세요 (예: INFP, INTJ 등)")

# 사용자 입력
user_mbti = st.text_input("✏️ MBTI").upper()

if user_mbti:
    if user_mbti in mbti_jobs:
        st.success(f"✅ {user_mbti} 유형을 분석했어요!")
        st.snow()  # 눈 내리는 효과로 "스크린 깨짐" 느낌 제공!

        # 1. 어울리는 작업
        st.subheader("🧭 어울리는 작업:")
        for job in mbti_jobs[user_mbti]:
            st.markdown(f"- {job}")

        # 2. 알파벳 해석
        st.markdown("---")
        st.subheader("🔤 MBTI 구성 해석:")
        for letter in user_mbti:
            if letter in mbti_meanings:
                st.markdown(mbti_meanings[letter])

        # 3. 책/영화 추천
        if user_mbti in mbti_recommendations:
            st.markdown("---")
            st.subheader("📚 추천 책:")
            for book in mbti_recommendations[user_mbti]["books"]:
                st.markdown(f"- {book}")

            st.subheader("🎬 추천 영화:")
            for movie in mbti_recommendations[user_mbti]["movies"]:
                st.markdown(f"- {movie}")

        st.markdown("---")
        st.markdown("다른 MBTI도 궁금하다면 다시 입력해보세요! 😉")
    else:
        st.error("❌ 유효한 MBTI를 입력해주세요 (예: ENFP, ISTJ 등).")
