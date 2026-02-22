import streamlit as st
import datetime as dt

st.set_page_config(page_title="KU Radiation Committee Dashboard", page_icon="🛡️", layout="wide")

# =========================
# HEADER
# =========================
st.title("🛡 Kuwait University Radiation Safety Dashboard")
st.markdown("### For University Radiation Committee Oversight")

st.markdown(
"**Institutional Commitment:** Kuwait University operates under centralized radiation governance aligned with MOH/RPD regulations and international standards."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("License Status", "Active")
with col2:
    st.metric("University Compliance", "Full")
with col3:
    st.metric("Last Policy Review", "2026")
with col4:
    st.metric("Regulatory Authority", "MOH / RPD")

st.caption(f"Updated: {dt.datetime.now().strftime('%Y-%m-%d')}")

st.divider()

# =========================
# OCCUPATIONAL DOSE SUMMARY
# =========================
st.subheader("📊 University-Wide Occupational Exposure")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Monitored Staff", "100%")
with c2:
    st.metric("Average Annual Dose", "0.5 mSv")
with c3:
    st.metric("Regulatory Limit", "20 mSv/year")
with c4:
    st.metric("Investigation Cases", "0")

st.success("ALARA performance demonstrated. Exposure levels remain <3% of regulatory limit.")

st.divider()

# =========================
# FACULTY STATUS
# =========================
st.subheader("🏛 Faculty Radiation Safety Status")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.info("🏥 Medicine\n\nRadiopharmacy controls\nTherapy safeguards\nAnimal research controls\nGamma irradiator secured")

with f2:
    st.info("🔬 Science\n\nIsotope lab controls\nMonthly monitoring\nSupervised teaching use")

with f3:
    st.info("⚙ Engineering\n\nX-ray registration\nInterlock verification\nCalibration source control")

with f4:
    st.info("🦷 Dentistry\n\nDiagnostic optimization\nAnnual QA\nSupervised student imaging")

st.divider()

# =========================
# GOVERNANCE & RISK
# =========================
st.subheader("🔎 Governance & Risk Oversight")

g1, g2, g3, g4 = st.columns(4)

with g1:
    st.metric("Annual Audit", "Completed")
with g2:
    st.metric("Training Coverage", "100%")
with g3:
    st.metric("Inventory Compliance", "100%")
with g4:
    st.metric("Reportable Incidents", "0")

st.success("Institutional Risk Level: LOW")

st.divider()

st.markdown("## 🟢 OVERALL STATUS: FULL CONFORMANCE")
