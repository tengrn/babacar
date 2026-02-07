import streamlit as st


st.set_page_config(page_title="CV - Babacar Ndiaye", page_icon="👤", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stHeader {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.image("https://via.placeholder.com/15", caption="Babacar Ndiaye") 
    st.title("📌Contact")
    st.write("📍 Dakar, Sénégal")
    st.write("📧 babacar.ndiaye@email.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com)")
    
    st.divider()
    st.subheader("🌏Langues")
    st.write("- Français (Natif)")
    st.write("- Anglais (Avancé)")
    st.write("- Wolof (Natif)")


col1, col2 = st.columns([2, 1], vertical_alignment="center")
with col1:
    st.title("Babacar Ndiaye")
    st.subheader("Ingénieur Data & Développeur Python")
    st.write("Passionné par l'exploitation des données et la création d'outils d'aide à la décision.")


tab1, tab2, tab3 = st.tabs(["Expériences", "Formation", "Compétences"])

with tab1:
    st.header("✨Expériences Professionnelles")
    
    with st.expander("Senior Data Analyst - Tech Lab (2022 - Présent)"):
        st.write("*Missions :*")
        st.write("- Analyse des KPIs de performance via des dashboards interactifs.")
        st.write("- Automatisation des rapports mensuels avec Python.")
        st.write("- Management d'une équipe de 3 stagiaires.")

    with st.expander("Développeur Python Junior - Startup X (2020 - 2022)"):
        st.write("- Développement d'APIs REST avec FastAPI.")
        st.write("- Nettoyage et prétraitement de bases de données SQL.")

with tab2:
    st.header("📚Formation")
    st.write("*Master en Informatique* - Université Cheikh Anta Diop (UCAD)")
    st.caption("Spécialité Intelligence Artificielle | 2020")
    
    st.write("*Licence en Mathématiques et Informatique* - École Polytechnique")
    st.caption("2018")

with tab3:
    st.header("🪄Hard Skills")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("*Langages :* Python, SQL, R")
        st.write("*Outils :* Streamlit, Docker, Git")

        