# streamlit run Home.py

import streamlit as st

st.set_page_config(page_title="Fatim Diagne — Data Visualization Portfolio", layout="wide")

st.markdown("""
<style>
    h1 {
        color: #1a1a2e;
        font-weight: 700;
    }
    .project-card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 12px;
        border-left: 4px solid #0f766e;
    }
    .project-card h3 {
        margin-top: 0;
        color: #1a1a2e;
    }
    .project-card p {
        color: #444;
    }
</style>
""", unsafe_allow_html=True)

st.title("Data Visualization Portfolio")

st.write("""
Welcome! This site showcases data visualization projects exploring economic development, 
demographic trends, and public policy questions using public datasets from the World Bank 
and other open sources.
""")

st.divider()
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h3>GDP & Water Access in Senegal</h3>
        <p>Exploring the relationship between economic growth and basic water access in Senegal (2000–2024)</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_Senegal_Project.py", label="View project →")

with col2:
    st.markdown("""
    <div class="project-card">
        <h3>World Population Analysis</h3>
        <p>Visualizing global population distribution, growth trends, and demographic shifts across continents.</p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/2_World_Population_Project.py", label="View project →")

st.divider()

st.subheader("About Me")

st.markdown("""
My name is **Fatim Diagne**, a Master's student in Public and International Affairs at the University of Ottawa, specializing in data analysis for Public Policy.
This portfolio showcases interactive Python-based visualizations to explore development and policy questions.
""")

st.markdown("[LinkedIn](https://www.linkedin.com/in/fatim-d-a98933257/?skipRedirect=true) · [Email](mailto:diagnefatim28@gmail.com)")


