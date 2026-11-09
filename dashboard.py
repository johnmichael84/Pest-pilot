import streamlit as st

st.title("Pest Pilot")

if "treatment_started" not in st.session_state:
    st.session_state.treatment_started = False
    
if st.button("Start Treatment"):
    st.session_state.treatment_started = True

if st.session_state.treatment_started:
    pest = st.selectbox("Select Pest", ["German Roaches", "Ants", "Mosquitoes", "Spiders"])
    severity = st.selectbox("Infestation Severity", ["Low", "Moderate", "Severe", "Infestation"])

    st.write("Selected Pest:", pest)
    st.write("Infestation Severity:", severity)

    if pest == "Ants":
        st.subheader("Ant Treatment Guidance")
        st.write("Inspect and trails and entry points")
        st.write("Identify the and species before treatment")
        st.write("Choose a treatment based on inspection")
    if severity == "Low":
        st.success("Low infestation: Inspect thoroughly and treat targeted areas")

    elif severity == "Moderate":
        st.warning("Moderate infestation: Inspect thoroughly and develop a treatment plan")

    elif severity == "Severe":
        st.error("Severe infestation: Intensive treatment and follow-up may be needed")

    elif severity == "Infestation":
        st.error("Heavy infestation: Conduct a detailed inspection and plan multiple visits")
        