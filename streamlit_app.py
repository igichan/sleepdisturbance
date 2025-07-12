import streamlit as st

st.set_page_config(page_title="수면 장애 자가 진단", layout="centered")

st.title("🛏️ 수면장애 자가 진단법")
st.write("")
st.write("""
최근 한 달간 일주일에 몇 번이나 아래 보기 항목에 해당했는지 체크해보세요.
""")

st.write("")

symptoms = [
    "잠들기까지 30분 이상 걸린다.",
    "잠드는 시간에 대한 강박증이 있다.",
    "조금만 신경 쓰이는 일이 있으면 잠들기가 어렵다.",
    "화장실을 자주 간다.",
    "자면서도 악몽 같은 복잡한 꿈을 자주 꾼다.",
    "이른 새벽에 이유 없이 깨고 다시 잠들기 어렵다.",
    "자다가 숨이 막히거나 질식할 것 같은 느낌이 들어 깬다.",
    "꿈을 꾸면 항상 기억한다.",
    "오랫동안 심하게 코를 곤다.",
    "너무 춥거나 더워서 잠을 잘 수 없다.",
    "하루 중 정오까지 정신이 들지 않는다.",
    "낮에 무의식적으로 눈이 감긴다.",
    "자다가 머리가 아파서 깬다."
]

st.subheader("🔍 증상 체크")
selected = []
for symptom in symptoms:
    if st.checkbox(symptom):
        selected.append(symptom)

count = len(selected)

st.write("")

# 선택된 증상 개수 표시 (결과확인 버튼 위에)
st.write(f"총 결과 개수: {count}")

st.write("")

# 결과확인 버튼 및 결과 분석
if st.button("결과확인"):
    st.subheader("🧠 결과 분석")
    if count >= 6:
        st.error("🚨 위험!    보기 중 6개 이상 해당되면 전문 병원 상담이 필요합니다.")
    elif count >= 4:
        st.warning("⚠️ 경고!    보기 중 4개 이상 해당되면 수면 장애로 발전하고 있는 단계. 생활 습관 개선과 병원 상담이 권장됩니다.")
    elif count >= 2:
        st.info("🔎 주의!    보기 중 2~3개 해당되면 생활 습관 점검이 필요합니다.")
    else:
        st.success("✅ 안심!    2개 미만 해당되면 수면에 큰 문제가 없어 보입니다.")
