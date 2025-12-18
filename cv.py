import streamlit as st
import pandas as pd
import altair as alt
import os

# =====================================================
# CONFIGURATION PAGE
# =====================================================
st.set_page_config(
    page_title="Tom Artigues | CV",
    page_icon="📄",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================
col_left, col_right = st.columns([4, 1])

with col_left:
    st.title("Tom Artigues")
    st.subheader("Bachelor Ingénierie Data & Marketing Digital – Alternant Responsable e-commerce")
    st.write("""
📍 Ablon-sur-Seine (94)  
📧 tom.artigues94@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/tom-artigues-619557292/)
""")

with col_right:
    logo = "efrei_logo.jpg"
    if os.path.exists(logo):
        st.image(logo, width=120)
    else:
        st.markdown("**EFREI Paris**")

st.divider()

# =====================================================
# PROFIL
# =====================================================
st.markdown("## PROFIL")

st.write("""
Étudiant en **3ᵉ et dernière année de Bachelor Ingénierie Data & Marketing Digital** à l’EFREI Paris,  
actuellement **en alternance en tant que Responsable e-commerce**.

Cette expérience m’a permis de développer une forte expertise en **pilotage de la performance**,  
**analyse de données**, **gestion de KPI**, **SEO / SEA** et **optimisation des canaux digitaux**.

Je souhaite désormais m’orienter vers un **master à dominante data** afin de renforcer mes compétences  
en **Business Intelligence, analyse décisionnelle et data analytics**.

Profil **orienté analyse, performance et résultats**, avec une forte culture **indicateurs & optimisation**.
""")

st.divider()

# =====================================================
# INDICATEURS CLÉS (KPI)
# =====================================================
k1, k2, k3, k4 = st.columns(4)
k1.metric("🎓 Niveau", "Bac +3")
k2.metric("💼 Expériences", "2 stages + 1 alternance")
k3.metric("📊 Orientation", "Data & Marketing")
k4.metric("🌍 Mobilité", "International")

st.divider()

# =====================================================
# COMPÉTENCES – DOT PLOT (ENTIERS UNIQUEMENT)
# =====================================================
st.markdown("## COMPÉTENCES CLÉS")

skills = pd.DataFrame({
    "Compétence": [
        "Marketing Digital",
        "SEO",
        "Analyse & Visualisation Data",
        "Python",
        "SQL",
        "Power BI / Excel",
        "Développement Web",
        "Gestion de projet"
    ],
    "Niveau": [4, 4, 5, 3, 4, 4, 3, 3]
})

dot_chart = (
    alt.Chart(skills)
    .mark_circle(size=300)
    .encode(
        x=alt.X(
            "Niveau:Q",
            scale=alt.Scale(domain=[0, 5]),
            axis=alt.Axis(
                values=[0, 1, 2, 3, 4, 5],
                format="d",
                tickMinStep=1,
                title="Niveau (1 = bas / 5 = élevé)"
            )
        ),
        y=alt.Y("Compétence:N", sort="-x", title=""),
        tooltip=["Compétence", "Niveau"]
    )
)

st.altair_chart(dot_chart, use_container_width=True)

st.divider()

# =====================================================
# LANGUES – BARRES HORIZONTALES
# =====================================================
st.markdown("## LANGUES")

languages = pd.DataFrame({
    "Langue": ["Anglais", "Espagnol"],
    "Niveau": [75, 50]
})

lang_chart = (
    alt.Chart(languages)
    .mark_bar()
    .encode(
        x=alt.X(
            "Niveau:Q",
            scale=alt.Scale(domain=[0, 100]),
            axis=alt.Axis(
                values=[0, 20, 40, 60, 80, 100],
                format="d",
                tickMinStep=10,
                title="Maîtrise (%)"
            )
        ),
        y=alt.Y("Langue:N", title=""),
        tooltip=["Langue", "Niveau"]
    )
)

st.altair_chart(lang_chart, use_container_width=True)

st.divider()

# =====================================================
# SOFT SKILLS – PROGRESS BARS
# =====================================================
st.markdown("## SOFT SKILLS")

soft_skills = {
    "Sérieux": 90,
    "Motivation": 95,
    "Curiosité": 90,
    "Esprit d’équipe": 85
}

for skill, value in soft_skills.items():
    st.write(f"{skill}")
    st.progress(value)

st.divider()

# =====================================================
# EXPÉRIENCE PROFESSIONNELLE
# =====================================================
st.markdown("## EXPÉRIENCE PROFESSIONNELLE")

st.write("""
**2025 – Stage SEO & Optimisation Web (2 mois)**  
**Atelier du Ride – Bobigny**  
• Optimisation SEO (on-page & technique)  
• Maintenance du site et amélioration UX  
• Création de fiches produits et contenus  
**Résultat :** augmentation significative du trafic organique

---

**2024 – Stage Marketing Digital (3 mois)**  
**Startup Solutions Données – Paris**  
• Campagnes d’email marketing & newsletters  
• CRM : HubSpot, Pipedrive  
• Analyse des performances & conversion  
**Résultat :** amélioration des taux d’ouverture et de clics

---

**2025 – Alternance – Wilift / Vertical l’Accessoire**  
**Responsable e-commerce**  
• Gestion complète du site e-commerce  
• SEO, SEA, Amazon Ads, Google Ads  
• Gestion CRM et tunnels de conversion  
• Analyse des performances et KPI
""")

st.divider()

# =====================================================
# FORMATION
# =====================================================
st.markdown("## FORMATION")

st.write("""
**EFREI Paris** – Bachelor Ingénierie Data & Marketing Digital *(2023–2026)* 

Cette formation combine une double expertise en **marketing digital** et en **analyse de données**,
avec un focus sur l’utilisation pratique des données et de l’intelligence artificielle dans un
contexte business.

**Matières et compétences clés :**
 Marketing digital avancé – stratégie multicanale, campagnes, CRM  
 SEO / SEA & Analytics – référencement, mesure de performance  
 Data & IA appliquée au marketing – Python, SQL, segmentation, insights  
 Business Intelligence & tableaux de bord – reporting et décisionnel  
 Projets concrets en entreprise liés à l’exploitation de données

**Module clé : Business Intelligence**  
• Tableaux de bord & KPI  
• Analyse décisionnelle  
• Aide à la décision par la donnée  

👨‍🏫 Professeur : Mathew Mano Joseph  
🔗 https://www.linkedin.com/in/manomathew/

---

**Asia Pacific University of Technology & Innovation (APU)** – Kuala Lumpur *(2025)*  
Mobilité internationale – IA, Business Intelligence & Digital
""")

st.divider()

# =====================================================
# INTÉRÊTS & VOYAGES
# =====================================================
st.markdown("## INTÉRÊTS & VOYAGES")

st.write("""
**Centres d’intérêt :** Sport, mode, musique, technologie, voyage  

**Pays visités :**  
Italie, Espagne, Belgique, Royaume-Uni, Canada,  
Cambodge, Thaïlande, Corée du Sud, Malaisie, Singapour
""")

st.caption("CV interactif – Streamlit | Tom Artigues")
