# === AccessFlow MVP (Streamlit Starter) ===
# accessflow_app.py

import streamlit as st
import datetime

st.set_page_config(page_title="AccessFlow - Permission Manager", layout="centered")

st.title("AccessFlow 🔐")
st.markdown("""
A lightweight mock to simulate how creators and teams manage access to promotion tools on platforms like Spotify for Artists.
""")

# Simulate user roles
st.subheader("🔍 User Role")
role = st.selectbox("Select your role:", ["Artist", "Label Rep", "Manager", "Collaborator"])

# Simulate tool access matrix
st.subheader("🛠️ Promotion Tool Access")
showcase_access = st.checkbox("Showcase Access")
discovery_access = st.checkbox("Discovery Mode")
marquee_access = st.checkbox("Marquee")

# Conditional logic
if role == "Artist" and not showcase_access:
    st.info("Artists can request Showcase access after one verified release.")

if role == "Collaborator" and (discovery_access or marquee_access):
    st.warning("Collaborators require manager approval for Discovery Mode and Marquee access.")

# Request access button
if st.button("Request Access Review"):
    st.success("Request submitted to the Admin team. You'll be notified by email.")

# Admin view (mocked)
st.markdown("---")
st.subheader("🔐 Admin Panel (Demo Only)")
st.write("Last access review: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
st.button("Simulate Admin Approval")

# To run this app:
# 1. Save as accessflow_app.py
# 2. Run: streamlit run accessflow_app.py
