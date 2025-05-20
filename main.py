import streamlit as st

# --- 다크 모드 스타일 (색 반전) ---
dark_mode_css = """
<style>
/* 배경색과 텍스트 색 반전 */
body, .css-18e3th9 {
    background-color: #121212 !important;
    color: #e0e0e0 !important;
}

/* 선택박스 배경과 텍스트 */
div[data-baseweb="select"] > div {
    background-color: #1e1e1e !important;
    color: #e0e0e0 !important;
}

/* 버튼 색상 */
.stButton > button {
    background-color: #2d2d2d !important;
    color: #e0e0e0 !important;
    border: 1px solid #555 !important;
}

/* 링크 색상 */
a {
    color: #8ab4f8 !important;
}

/* 구분선 색 */
hr {
    border-color: #444 !important;
}

/* 컬럼내 마진 조정 */
.css-1d391kg {
    margin-bottom: 1rem !important;
}
</style>
"""

st.markdown(dark_mode_css, unsafe_allow_html=True)

# --- 기존 MBTI 코드 (정리된 버전) ---
mbti_pairs = {
    "E/I": {
        "E": "🌟 **E (외향형)**: 사람들과 어울릴 때 에너지를 얻어요.",
        "I": "🌙 **I (내향형)**: 혼자 있는 시간이 에너지를 충전해줘요."
    },
    "S/N": {
        "S": "🔎 **S (감각형)**: 사실과 현실에 주의를 기울여요.",
        "N": "🌈 **N (직관형)**: 가능성과 미래를 중심으로 생각해요."
    },
    "T/F": {
        "T": "⚖️ **T (사고형)**: 논리와 객관적 판단을 중요시해요.",
        "F": "💖 **F (감정형)**: 공감과 감정을 중요하게 여겨요."
    },
    "J/P": {
        "J": "🗂️ **J (판단형)**: 계획적이고 체계적인 것을 좋아해요.",
        "P": "🎨 **P (인식형)**: 융통성과 즉흥성을 선호해요."
    }
}

mbti_data = {
    "INTJ": {
        "jobs": ["전략기획가", "데이터 과학자", "기술 분석가", "시스템 설계자", "AI 연구원"],
        "similar": "INFJ, ENTJ",
        "opposite": "ESFP",
        "books": ["『이기적 유전자』", "『생각의 기술』"],
        "movies": ["🎥 인터스텔라", "🎥 소셜 네트워크"]
    },
    # ... (중략: 나머지 MBTI 데이터 동일)
    "INFP": {
        "jobs": ["소설가", "시인", "상담가", "애니메이터", "UX 디자이너"],
        "similar": "INFJ, ENFP",
        "opposite": "ESTJ",
        "books": ["『어린 왕자』", "『나미야 잡화점의 기적』"],
        "movies": ["🎥 월플라워", "🎥 인사이드 아웃"]
    },
    # 여기부터 아래 모든 MBTI 유형 데이터 다 넣으시면 됩니다.
}

st.set_page_config(page_title="MBTI 성격 추천기 (다크모드)", page_icon="🧠")

st.title("💼 MBTI 기반 성격 & 직업 추천기 (다크모드)")
st.markdown("MBTI를 선택하면 성격 분석과 어울리는 직업, 추천 책/영화, 유사 MBTI까지 알려드려요!")

st.markdown("### 🔠 MBTI 알파벳 설명")
for pair, letters in mbti_pairs.items():
    cols = st.columns(2)
    with cols[0]:
        st.markdown(letters[list(letters.keys())[0]])
    with cols[1]:
        st.markdown(letters[list(letters.keys())[1]])
st.markdown("---")

mbti_types = sorted(mbti_data.keys())
user_mbti = st.selectbox("👉 자신의 MBTI를 선택하세요:", options=[""] + mbti_types)

if user_mbti:
    data = mbti_data[user_mbti]
    st.success(f"🔍 {user_mbti} 유형 분석 결과입니다!")
    st.snow()

    st.subheader("💼 어울리는 직업")
    for job in data["jobs"]:
        st.markdown(f"- {job}")

    st.subheader("📚 추천 책")
    for book in data["books"]:
        st.markdown(f"- {book}")

    st.subheader("🎬 추천 영화")
    for movie in data["movies"]:
        st.markdown(f"- {movie}")

    st.subheader("🧑‍🤝‍🧑 비슷한 성격 유형")
    st.markdown(f"✅ {data['similar']}")

    st.subheader("🙅 가장 안 맞는 성격 유형")
    st.markdown(f"⚠️ {data['opposite']}")
