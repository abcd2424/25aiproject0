import streamlit as st

# 반드시 이 부분이 가장 먼저 와야 합니다.
st.set_page_config(page_title="MBTI 성격 추천기", page_icon="🧠")
# --- MBTI 알파벳 쌍 설명 ---
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

# --- MBTI 유형별 데이터 ---
mbti_data = {
    "INTJ": {
        "jobs": ["전략기획가", "데이터 과학자", "기술 분석가", "시스템 설계자", "AI 연구원"],
        "similar": "INFJ, ENTJ",
        "opposite": "ESFP",
        "books": ["『이기적 유전자』", "『생각의 기술』"],
        "movies": ["🎥 인터스텔라", "🎥 소셜 네트워크"]
    },
    "INFP": {
        "jobs": ["소설가", "시인", "상담가", "애니메이터", "UX 디자이너"],
        "similar": "INFJ, ENFP",
        "opposite": "ESTJ",
        "books": ["『어린 왕자』", "『나미야 잡화점의 기적』"],
        "movies": ["🎥 월플라워", "🎥 인사이드 아웃"]
    },
    "ENTP": {
        "jobs": ["창업가", "마케팅 전문가", "기획자", "디자이너", "기술 혁신가"],
        "similar": "ENFP, ENTP",
        "opposite": "ISFJ",
        "books": ["『제로 투 원』", "『스티브 잡스』"],
        "movies": ["🎥 인셉션", "🎥 아이언맨"]
    },
    "ISFJ": {
        "jobs": ["간호사", "교사", "사회복지사", "도서관 사서", "행정직"],
        "similar": "ESFJ, ISTJ",
        "opposite": "ENTP",
        "books": ["『비밀의 화원』", "『책 읽어주는 남자』"],
        "movies": ["🎥 업", "🎥 포레스트 검프"]
    },
    "INFJ": {
        "jobs": ["상담심리사", "작가", "인문학 연구자", "컨텐츠 디렉터", "비영리 단체 활동가"],
        "similar": "INFP, INTJ",
        "opposite": "ESTP",
        "books": ["『모모』", "『데미안』"],
        "movies": ["🎥 사운드 오브 메탈", "🎥 빅피쉬"]
    },
    "ENFP": {
        "jobs": ["마케터", "기획자", "영상 크리에이터", "스타트업 창업가", "여행 작가"],
        "similar": "INFP, ENTP",
        "opposite": "ISTJ",
        "books": ["『가벼움의 시대』", "『내 안의 너에게』"],
        "movies": ["🎥 예스맨", "🎥 미드나잇 인 파리"]
    },
    "ISTJ": {
        "jobs": ["회계사", "법무사", "공무원", "데이터 관리자", "품질 관리자"],
        "similar": "ISFJ, ESTJ",
        "opposite": "ENFP",
        "books": ["『원칙』", "『회계의 신』"],
        "movies": ["🎥 머니볼", "🎥 캐치 미 이프 유 캔"]
    },
    "ESFP": {
        "jobs": ["공연 예술가", "이벤트 기획자", "배우", "유튜버", "브랜드 매니저"],
        "similar": "ISFP, ESTP",
        "opposite": "INTJ",
        "books": ["『파울로 코엘료의 연금술사』"],
        "movies": ["🎥 라라랜드", "🎥 그레이티스트 쇼맨"]
    },
    "ESTP": {
        "jobs": ["기업 영업", "스포츠 트레이너", "경찰관", "스타트업 운영자", "모험 여행 가이드"],
        "similar": "ISTP, ESTP",
        "opposite": "INFJ",
        "books": ["『무조건 달려』"],
        "movies": ["🎥 분노의 질주", "🎥 미션 임파서블"]
    },
    "ISFP": {
        "jobs": ["그래픽 디자이너", "사진작가", "물리치료사", "조용한 예술가", "반려동물 훈련사"],
        "similar": "INFP, ESFP",
        "opposite": "ENTJ",
        "books": ["『나의 라임 오렌지 나무』", "『보노보노처럼 살다니 다행이야』"],
        "movies": ["🎥 리틀 포레스트", "🎥 허(Her)"]
    },
    "ENTJ": {
        "jobs": ["CEO", "전략 컨설턴트", "벤처 투자자", "정치 분석가", "경영 지도자"],
        "similar": "INTJ, ESTJ",
        "opposite": "ISFP",
        "books": ["『그로우』", "『하드씽』"],
        "movies": ["🎥 울프 오브 월스트리트", "🎥 글래디에이터"]
    },
    "ESTJ": {
        "jobs": ["프로젝트 매니저", "군 간부", "경영자", "행정 공무원", "공장 관리자"],
        "similar": "ISTJ, ENTJ",
        "opposite": "INFP",
        "books": ["『철학은 어떻게 삶의 무기가 되는가』"],
        "movies": ["🎥 체르노빌", "🎥 설국열차"]
    },
    "ENFJ": {
        "jobs": ["심리상담가", "강연가", "학교 교사", "비전 리더", "HR 전문가"],
        "similar": "INFJ, ENFP",
        "opposite": "ISTP",
        "books": ["『말의 품격』", "『사람은 왜 모여 살까』"],
        "movies": ["🎥 굿 윌 헌팅", "🎥 원더"]
    },
    "ISTP": {
        "jobs": ["기계 기술자", "소방관", "비행기 정비사", "엔지니어", "오토바이 수리사"],
        "similar": "ESTP, INTP",
        "opposite": "ENFJ",
        "books": ["『닥치고 공작소』"],
        "movies": ["🎥 매드 맥스", "🎥 본 아이덴티티"]
    },
    "ESFJ": {
        "jobs": ["초등교사", "서비스 매니저", "이벤트 코디네이터", "간호조무사", "케어매니저"],
        "similar": "ISFJ, ENFJ",
        "opposite": "INTP",
        "books": ["『선량한 차별주의자』"],
        "movies": ["🎥 인턴", "🎥 굿닥터"]
    },
    "INTP": {
        "jobs": ["프로그래머", "이론 과학자", "철학자", "시스템 개발자", "AI 윤리 연구자"],
        "similar": "ISTP, ENTP",
        "opposite": "ESFJ",
        "books": ["『코스모스』", "『프로그래머, 수학을 만나다』"],
        "movies": ["🎥 어벤져스: 에이지 오브 울트론", "🎥 굿 윌 헌팅"]
    }
}


st.title("💼 MBTI 기반 성격 & 직업 추천기")
st.markdown("MBTI를 선택하면 성격 분석과 어울리는 직업, 추천 책/영화, 유사 MBTI까지 알려드려요!")

# 알파벳 의미 묶어서 표시
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
