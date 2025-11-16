import streamlit as st
from core.router import PageRouter
from pages.home import HomePage
from pages.mannschaften import MannschaftenPage
from pages.neuigkeiten import NeuigkeitenPage
from pages.geschichte import GeschichtePage


def main():
    st.set_page_config(
        page_title="Tischtennis Bad Aibling",
        page_icon="🏓",
        layout="wide",
    )

    # You can keep this or comment it out; it won't affect centering.
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {display:none !important;}
            [data-testid="stSidebarToggle"] {display:none !important;}
            [data-testid="collapsedControl"] {display:none !important;}
        </style>
    """, unsafe_allow_html=True)

    pages = [
        HomePage(),
        MannschaftenPage(),
        NeuigkeitenPage(),
        GeschichtePage(),
    ]

    router = PageRouter(
        club_name="Tischtennis Bad Aibling",
        logo_path="assets/logo.png",
        pages=pages,
    )
    router.run()


if __name__ == "__main__":
    main()
