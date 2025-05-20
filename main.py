import streamlit as st

# MBTI별 추천 작업 데이터
mbti_jobs = {
    "INTJ": ["📊 전략기획", "🧠 데이터 분석", "🔬 연구개발"],
    "INTP": ["💻 프로그래머", "🔭 과학자", "📚 철학자"],
    "ENTJ": ["📈 경영 컨설턴트", "📂 프로젝트 매니저", "⚖️ 변호사"],
    "ENTP": ["🚀 창업가", "🎯 광고기획자", "🛠️ 기술 개발자"],
    "INFJ": ["💬 상담사", "✍️ 작가", "🧘‍♀️ 심리학자"],
    "INFP": ["🎨 예술가", "📝 시인", "🎥 콘텐츠 제작자"],
    "ENFJ": ["👩‍🏫 교사", "🧭 리더십 코치", "🧑‍💼 HR매니저"],
    "ENFP": ["📣 마케터", "🧃 기획자", "🎙️ 방송인"],
    "ISTJ": ["📒 회계사", "🏛️ 공무원", "🧰 엔지니어"],
    "ISFJ": ["💉 간호사", "🤝 사회복지사", "👶 보조 교사"],
    "ESTJ": ["🏗️ 관리자", "🪖 군인", "🧾 감독관"],
    "ESFJ": ["🗂️ 행정직", "📞 고객 서비스", "🎉 이벤트 플래너"],
    "ISTP": ["🔧 기술자", "🛩️ 파일럿", "🔩 메카닉"],
    "ISFP": ["🎨 디자이너", "👩‍🍳 요리사", "💐 플로리스트"],
    "ESTP": ["🗣️ 세일즈", "🚑 응급구조사", "🤸 스턴트맨"],
    "ESFP": ["🎤 연예인", "🎭 공연기획자", "🌍 여행가이드"]
}

# 페이지 설정
st.set_page_config(page_title="MBTI 작업 추천기 ✨", page_icon="💼", layout="centered")

# 헤더
st.title("💼 MBTI 기반 작업 추천기")
st.markdown("당신의 **MBTI**를 입력하면 💡 어울리는 작업을 🎯 추천해드릴게요!")
st.markdown("👇 아래에 MBTI를 입력해주세요!")

# 사용자 입력
user_mbti = st.text_input("✏️ MBTI (예: INFP, ESTJ)").upper()

# 추천 결과 출력
if user_mbti:
    if user_mbti in mbti_jobs:
        st.success(f"✅ {user_mbti} 유형을 분석했어요!")
        st.balloons()  # 풍선 효과
        st.subheader(f"🌟 {user_mbti} 유형에게 어울리는 작업은...")

        for job in mbti_jobs[user_mbti]:
            st.markdown(f"- {job}")

        st.markdown("---")
        st.markdown("🧠 더 알고 싶다면 다른 MBTI도 입력해보세요!")
    else:
        st.error("❌ 유효한 MBTI 유형을 입력해주세요 (예: ENFP, ISTJ 등 16가지 중 하나).")
