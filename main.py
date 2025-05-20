import streamlit as st

# 알파벳 설명 (입력 전에도 항상 보여줌)
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

# 추천 직업
mbti_jobs = {
    "INTJ": ["📊 전략기획자", "🧠 데이터 과학자", "🔬 연구개발자", "🏦 금융 분석가", "📚 교육 콘텐츠 디자이너"],
    "INFP": ["🎨 일러스트레이터", "📝 시나리오 작가", "📖 편집자", "🎥 영상 콘텐츠 크리에이터", "🧘 명상 지도사"],
    "ENTP": ["🚀 스타트업 창업가", "🎯 마케팅 디렉터", "🎮 게임 디자이너", "🧪 혁신 컨설턴트", "🎤 팟캐스터"],
    "ISFJ": ["💉 간호사", "👩‍🏫 유치원 교사", "🏠 주거복지사", "🧾 사무 행정", "📦 물류관리자"]
}

# 책/영화 추천
mbti_recommendations = {
    "INTJ": {
        "books": ["『이기적 유전자』", "『생각의 기술』"],
        "movies": ["🎥 인터스텔라", "🎥 매트릭스"]
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

# 비슷한/반대 성격 추천
mbti_relations = {
    "INTJ": {"similar": "INFJ, ENTJ", "opposite": "ESFP"},
    "INFP": {"similar": "INFJ, ENFP", "opposite": "ESTJ"},
    "ENTP": {"similar": "ENFP, ENTP", "opposite": "ISFJ"},
    "ISFJ": {"similar": "ESFJ, ISTJ", "opposite": "ENTP"},
}

# 페이지 설정
st.set_page_config(page_title="MBTI 성격 추천기 💼", page_icon="🧠")

# 헤더
st.title("💼 MBTI 기반 성격 & 직업 추천기")
st.markdown("MBTI를 입력하면 아래 정보를 알려드려요:")
st.markdown("- 🧠 성격 알파벳 해석")
st.markdown("- 💼 어울리는 직업 추천")
st.markdown("- 📚 책 & 🎬 영화 추천")
st.markdown("- 🧑‍🤝‍🧑 비슷한/상극 MBTI도 알려줘요!")

# 🔠 알파벳 설명 항상 출력
st.markdown("### 🔤 MBTI 알파벳 의미")
cols = st.columns(4)
for i, letter in enumerate("EISNTFJP"):
    with cols[i % 4]:
        st.markdown(mbti_meanings[letter])

st.markdown("---")

# 사용자 입력
user_mbti = st.text_input("👉 당신의 MBTI를 입력해주세요 (예: INFP)").upper()

# 유효 MBTI만 허용
valid_types = mbti_jobs.keys()

if user_mbti:
    if user_mbti in valid_types:
        st.success(f"🎉 {user_mbti} 유형을 분석했어요!")
        st.snow()  # 눈 효과

        # 직업 추천
        st.subheader("💼 어울리는 직업")
        for job in mbti_jobs[user_mbti]:
            st.markdown(f"- {job}")

        # 책 & 영화
        if user_mbti in mbti_recommendations:
            st.markdown("---")
            st.subheader("📚 추천 책")
            for book in mbti_recommendations[user_mbti]["books"]:
                st.markdown(f"- {book}")
            st.subheader("🎬 추천 영화")
            for movie in mbti_recommendations[user_mbti]["movies"]:
                st.markdown(f"- {movie}")

        # 유사 / 상극 MBTI
        if user_mbti in mbti_relations:
            st.markdown("---")
            st.subheader("🧑‍🤝‍🧑 비슷한 성격 유형")
            st.markdown(f"✅ {mbti_relations[user_mbti]['similar']}")
            st.subheader("🙅 가장 안 맞는 성격 유형")
            st.markdown(f"⚠️ {mbti_relations[user_mbti]['opposite']}")

    else:
        st.error("🚫 유효한 MBTI 유형을 입력해주세요 (예: INFP, INTJ 등 16가지).")
